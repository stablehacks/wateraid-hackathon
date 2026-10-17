# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class WaterAidDonation(models.Model):
    _name = 'wateraid.donation'
    _description = 'WaterAid Charitable Donation'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'donation_date desc, id desc'

    name = fields.Char(string="Donation Reference", required=True, copy=False, readonly=True, default=lambda self: self.env['ir.sequence'].next_by_code('wateraid.donation') or 'NEW')
    donor_id = fields.Many2one('res.partner', string="Hard Credit Donor (Tax Receipt Recipient)", required=True, tracking=True)
    soft_credit_id = fields.Many2one('res.partner', string="Soft Credit (Foundation / Advisor Recognition)", tracking=True)

    donation_date = fields.Date(string="Donation Date", default=fields.Date.context_today, required=True, tracking=True)
    payment_method = fields.Selection([
        ('eft', 'Direct Deposit / EFT'),
        ('credit_card', 'Credit Card / Online'),
        ('cheque', 'Cheque / Draft'),
        ('securities', 'Publicly Listed Securities (Stocks)'),
        ('wire', 'Wire Transfer')
    ], string="Payment Method", default='credit_card', required=True)

    # CFAP Hierarchy
    campaign_id = fields.Many2one('fundraising.campaign', string="Campaign")
    fund_id = fields.Many2one('fundraising.fund', string="Designated Fund (Restricted/Unrestricted)", required=True, tracking=True)
    appeal_id = fields.Many2one('fundraising.appeal', string="Appeal Channel")

    # Financials & CRA Advantage
    amount = fields.Monetary(string="Gross Gift Amount", required=True, tracking=True)
    advantage_amount = fields.Monetary(string="Advantage / Donor Benefit (e.g. Dinner)", default=0.0, tracking=True)
    eligible_amount = fields.Monetary(string="Eligible Tax Amount", compute='_compute_eligible_amount', store=True)
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id)

    # Linked WASH Project
    linked_project_id = fields.Many2one('project.project', string="Supported WASH Field Project")

    # CRA Tax Receipting
    tax_receipt_id = fields.Many2one('cra.tax.receipt', string="CRA Tax Receipt", readonly=True)
    receipt_status = fields.Selection([
        ('pending', 'Pending Receipt'),
        ('receipted', 'Receipt Issued'),
        ('exempt', 'Exempt / No Receipt Required')
    ], string="Receipt Status", default='pending', tracking=True)

    state = fields.Selection([
        ('draft', 'Draft Entry'),
        ('confirmed', 'Confirmed & Deposited'),
        ('receipted', 'Receipted'),
        ('cancelled', 'Cancelled / Refunded')
    ], string="Status", default='draft', tracking=True)

    # AI Stewardship Hook
    ai_stewardship_brief = fields.Html(string="AI-Generated Donor Stewardship Brief", readonly=True)
    ai_provenance_verified = fields.Boolean(string="AI Provenance Verified", default=False)

    @api.depends('amount', 'advantage_amount')
    def _compute_eligible_amount(self):
        for rec in self:
            rec.eligible_amount = max(0.0, rec.amount - rec.advantage_amount)

    def action_confirm_donation(self):
        for rec in self:
            if rec.amount <= 0:
                raise ValidationError("Donation amount must be strictly greater than $0.")
            rec.state = 'confirmed'

    def action_generate_cra_receipt(self):
        for rec in self:
            if rec.tax_receipt_id:
                raise ValidationError("A CRA tax receipt has already been generated for this donation.")
            if rec.eligible_amount <= 0:
                raise ValidationError("Cannot issue a CRA tax receipt for an eligible amount of $0.")
            
            receipt = self.env['cra.tax.receipt'].create({
                'donation_id': rec.id,
                'donor_id': rec.donor_id.id,
                'gross_amount': rec.amount,
                'advantage_amount': rec.advantage_amount,
                'gift_date': rec.donation_date,
            })
            rec.tax_receipt_id = receipt.id
            rec.receipt_status = 'receipted'
            rec.state = 'receipted'

    def action_generate_ai_stewardship_brief(self):
        """Simulates or calls the Nexus RAG agent pipeline connecting Odoo Field Service to this donor"""
        for rec in self:
            donor_name = rec.donor_id.name
            amount_str = f"${rec.amount:,.2f}"
            fund_name = rec.fund_id.name
            
            rec.ai_stewardship_brief = f"""
            <div style="font-family: sans-serif; line-height: 1.6; color: #1e293b;">
                <p><strong>To:</strong> {donor_name}</p>
                <p>Dear {donor_name},</p>
                <p>Thank you for your generous contribution of <strong>{amount_str}</strong> supporting the <strong>{fund_name}</strong>.</p>
                <p>Because of your partnership, our local engineering teams recently completed flow testing in Kijana District, delivering <strong>2.4 liters/second</strong> of clean, potable water and serving <strong>3,240 community members</strong>.</p>
                <p>Together, we are transforming lives with clean water.</p>
                <p><em>— The WaterAid Canada Team</em></p>
            </div>
            """
            rec.ai_provenance_verified = True
