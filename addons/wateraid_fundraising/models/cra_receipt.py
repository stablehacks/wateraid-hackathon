# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CraTaxReceipt(models.Model):
    _name = 'cra.tax.receipt'
    _description = 'Canadian Official Charitable Donation Tax Receipt (CRA Reg. 3501)'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'name desc'

    name = fields.Char(string="CRA Receipt Number", required=True, copy=False, readonly=True, default=lambda self: self.env['ir.sequence'].next_by_code('cra.tax.receipt') or 'NEW')
    donor_id = fields.Many2one('res.partner', string="Donor (Taxpayer Name)", required=True, tracking=True)
    donor_address = fields.Text(string="Donor Canadian Address", compute='_compute_donor_address', store=True)
    
    donation_id = fields.Many2one('wateraid.donation', string="Linked Donation", required=True, ondelete='restrict')
    
    gross_amount = fields.Monetary(string="Total Amount Received", required=True, tracking=True)
    advantage_amount = fields.Monetary(string="Advantage / Benefit to Donor", default=0.0, tracking=True,
                                      help="Value of any goods, services, or entertainment provided to the donor in exchange for the gift (e.g. Gala dinner value).")
    eligible_amount = fields.Monetary(string="Eligible Amount of Gift for Tax Purposes", compute='_compute_eligible_amount', store=True)
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id)

    charity_name = fields.Char(string="Charity Name", default="WaterAid Canada")
    charity_bn = fields.Char(string="Charity Registration BN", default="119287595 RR 0001", readonly=True)
    charity_address = fields.Text(string="Charity Address", default="WaterAid Canada\n321 Slater Street, Suite 200\nOttawa, ON K1P 5H9\nCanada")

    receipt_date = fields.Date(string="Date Issued", default=fields.Date.context_today, required=True, readonly=True)
    gift_date = fields.Date(string="Date Donation Received", required=True, readonly=True)
    tax_year = fields.Integer(string="Tax Year", compute='_compute_tax_year', store=True)

    state = fields.Selection([
        ('issued', 'Issued'),
        ('reissued', 'Re-Issued (Replacement)'),
        ('cancelled', 'Cancelled / Revoked')
    ], string="Receipt Status", default='issued', tracking=True)

    replaces_receipt_id = fields.Many2one('cra.tax.receipt', string="Replaces Cancelled Receipt Number",
                                         help="Mandated by CRA Reg. 3501 when replacing a lost or revised receipt.")
    cancellation_reason = fields.Char(string="Cancellation Reason")
    authorized_signatory = fields.Char(string="Authorized Signatory", default="Director of Finance, WaterAid Canada")

    @api.depends('gross_amount', 'advantage_amount')
    def _compute_eligible_amount(self):
        for rec in self:
            rec.eligible_amount = max(0.0, rec.gross_amount - rec.advantage_amount)

    @api.depends('donor_id')
    def _compute_donor_address(self):
        for rec in self:
            rec.donor_address = rec.donor_id._display_address() if rec.donor_id else ""

    @api.depends('gift_date')
    def _compute_tax_year(self):
        for rec in self:
            rec.tax_year = rec.gift_date.year if rec.gift_date else fields.Date.today().year

    def action_cancel_receipt(self):
        self.ensure_one()
        self.state = 'cancelled'

    def action_reissue_receipt(self):
        self.ensure_one()
        # Mark original as cancelled
        old_num = self.name
        self.state = 'cancelled'
        self.cancellation_reason = f"Cancelled and replaced by revised receipt."

        # Create replacement receipt referencing old number
        new_receipt = self.copy({
            'name': self.env['ir.sequence'].next_by_code('cra.tax.receipt'),
            'state': 'reissued',
            'replaces_receipt_id': self.id,
            'receipt_date': fields.Date.today(),
        })
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'cra.tax.receipt',
            'res_id': new_receipt.id,
            'view_mode': 'form',
            'target': 'current',
        }
