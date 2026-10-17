# -*- coding: utf-8 -*-
from odoo import models, fields

class FundraisingCampaign(models.Model):
    _name = 'fundraising.campaign'
    _description = 'Fundraising Strategic Campaign'

    name = fields.Char(string="Campaign Name", required=True)
    code = fields.Char(string="Campaign Code", required=True)
    target_amount = fields.Monetary(string="Goal (CAD)")
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id)
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    active = fields.Boolean(default=True)
    fund_ids = fields.One2many('fundraising.fund', 'campaign_id', string="Designated Funds")
    description = fields.Text(string="Campaign Narrative")

class FundraisingFund(models.Model):
    _name = 'fundraising.fund'
    _description = 'Non-Profit Designated Fund (Restricted vs Unrestricted)'

    name = fields.Char(string="Fund Name", required=True)
    code = fields.Char(string="Fund Code", required=True)
    campaign_id = fields.Many2one('fundraising.campaign', string="Parent Campaign")
    fund_type = fields.Selection([
        ('unrestricted', 'Unrestricted (General Operating & Greatest Need)'),
        ('restricted_program', 'Program Restricted (Specific Country or Initiative)'),
        ('restricted_project', 'Project Restricted (e.g. Kijana Borehole Solar Pump)'),
        ('endowment', 'Capital Endowment'),
    ], string="Fund Restriction Type", required=True, default='unrestricted')
    analytic_account_id = fields.Many2one('account.analytic.account', string="GL Analytic Account (Accounting)")
    active = fields.Boolean(default=True)

class FundraisingAppeal(models.Model):
    _name = 'fundraising.appeal'
    _description = 'Solicitation Appeal Channel'

    name = fields.Char(string="Appeal Name", required=True)
    code = fields.Char(string="Appeal Code", required=True)
    channel = fields.Selection([
        ('direct_mail', 'Direct Mail / Post'),
        ('email', 'Email Marketing Appeal'),
        ('digital_ads', 'Digital Campaign / Social'),
        ('gala', 'In-Person Event / Gala'),
        ('major_proposal', 'Major Donor Bespoke Proposal'),
        ('gac_grant', 'Federal Multilateral Grant (GAC)')
    ], string="Appeal Channel", default='email')
    campaign_id = fields.Many2one('fundraising.campaign', string="Campaign")
    cost = fields.Monetary(string="Total Appeal Cost (CAD)")
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id)
