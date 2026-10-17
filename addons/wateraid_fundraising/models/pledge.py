# -*- coding: utf-8 -*-
from odoo import models, fields, api

class WaterAidPledge(models.Model):
    _name = 'wateraid.pledge'
    _description = 'Multi-Year Non-Profit Major Gift Pledge'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Pledge Reference", required=True, copy=False, readonly=True, default=lambda self: self.env['ir.sequence'].next_by_code('wateraid.pledge') or 'NEW')
    donor_id = fields.Many2one('res.partner', string="Donor", required=True, tracking=True)
    campaign_id = fields.Many2one('fundraising.campaign', string="Campaign")
    fund_id = fields.Many2one('fundraising.fund', string="Designated Fund", required=True)

    total_amount = fields.Monetary(string="Total Pledged Amount", required=True, tracking=True)
    paid_amount = fields.Monetary(string="Amount Paid to Date", compute='_compute_pledge_balances', store=True)
    balance_amount = fields.Monetary(string="Remaining Balance", compute='_compute_pledge_balances', store=True)
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id)

    start_date = fields.Date(string="Pledge Start Date", default=fields.Date.context_today)
    end_date = fields.Date(string="Pledge End Date")
    installment_ids = fields.One2many('wateraid.pledge.installment', 'pledge_id', string="Scheduled Installments")

    state = fields.Selection([
        ('draft', 'Draft Commitment'),
        ('active', 'Active & Current'),
        ('fulfilled', 'Fully Fulfilled'),
        ('cancelled', 'Written Off / Cancelled')
    ], string="Pledge Status", default='active', tracking=True)

    @api.depends('installment_ids.state', 'installment_ids.amount')
    def _compute_pledge_balances(self):
        for pledge in self:
            paid = sum(pledge.installment_ids.filtered(lambda i: i.state == 'paid').mapped('amount'))
            pledge.paid_amount = paid
            pledge.balance_amount = max(0.0, pledge.total_amount - paid)
            if pledge.balance_amount == 0 and pledge.total_amount > 0:
                pledge.state = 'fulfilled'

class WaterAidPledgeInstallment(models.Model):
    _name = 'wateraid.pledge.installment'
    _description = 'Pledge Scheduled Installment'
    _order = 'due_date asc'

    pledge_id = fields.Many2one('wateraid.pledge', string="Pledge", required=True, ondelete='cascade')
    due_date = fields.Date(string="Payment Due Date", required=True)
    amount = fields.Monetary(string="Installment Amount", required=True)
    currency_id = fields.Many2one('res.currency', related='pledge_id.currency_id')
    donation_id = fields.Many2one('wateraid.donation', string="Fulfilled by Donation")
    state = fields.Selection([
        ('unpaid', 'Unpaid / Scheduled'),
        ('overdue', 'Overdue'),
        ('paid', 'Paid & Reconciled')
    ], string="Status", default='unpaid')
