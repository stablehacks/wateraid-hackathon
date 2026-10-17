# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import date

class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Household & Constituent Types
    is_nonprofit_constituent = fields.Boolean(string="Is Donor / Constituent", default=True, index=True)
    is_household = fields.Boolean(string="Is Household Record", default=False)
    household_id = fields.Many2one('res.partner', string="Belongs to Household", domain=[('is_household', '=', True)])
    household_member_ids = fields.One2many('res.partner', 'household_id', string="Household Members")

    # Giving Statistics (RFM Analysis)
    donation_ids = fields.One2many('wateraid.donation', 'donor_id', string="Donations (Hard Credit)")
    soft_credit_donation_ids = fields.One2many('wateraid.donation', 'soft_credit_id', string="Donations (Soft Credit)")
    pledge_ids = fields.One2many('wateraid.pledge', 'donor_id', string="Pledges")

    lifetime_giving_amount = fields.Monetary(string="Lifetime Giving (CAD)", compute='_compute_giving_stats', store=True)
    first_gift_date = fields.Date(string="First Gift Date", compute='_compute_giving_stats', store=True)
    last_gift_date = fields.Date(string="Last Gift Date", compute='_compute_giving_stats', store=True)
    largest_gift_amount = fields.Monetary(string="Largest Gift (CAD)", compute='_compute_giving_stats', store=True)
    total_gift_count = fields.Integer(string="Total Number of Gifts", compute='_compute_giving_stats', store=True)

    # Lapsed Donor Analytics (LYBUNT / SYBUNT)
    is_lybunt = fields.Boolean(string="LYBUNT Donor (Gave Last Year, Not This Year)", compute='_compute_lapsed_status', store=True)
    is_sybunt = fields.Boolean(string="SYBUNT Donor (Gave Some Year, Not This Year)", compute='_compute_lapsed_status', store=True)

    # WASH Specific Preferences
    preferred_wash_cause = fields.Selection([
        ('boreholes', 'Solar Powered Deep Wells & Boreholes'),
        ('schools', 'Clean Water & Hygiene in Schools'),
        ('climate', 'Climate Resilient Water Infrastructure'),
        ('maternal', 'Healthcare Facility WASH & Maternal Health'),
        ('unrestricted', 'Greatest Need / Unrestricted')
    ], string="Preferred WASH Initiative", default='unrestricted')

    donor_tier = fields.Selection([
        ('grassroots', 'Grassroots ($1 - $499)'),
        ('midlevel', 'Mid-Level ($500 - $4,999)'),
        ('major', 'Major Donor ($5,000 - $24,999)'),
        ('principal', 'Principal / Institutional ($25,000+)'),
    ], string="Donor Tier", compute='_compute_donor_tier', store=True)

    @api.depends('donation_ids.state', 'donation_ids.amount')
    def _compute_giving_stats(self):
        for partner in self:
            confirmed_donations = partner.donation_ids.filtered(lambda d: d.state in ('confirmed', 'receipted'))
            amounts = confirmed_donations.mapped('amount')
            dates = confirmed_donations.mapped('donation_date')

            partner.lifetime_giving_amount = sum(amounts) if amounts else 0.0
            partner.largest_gift_amount = max(amounts) if amounts else 0.0
            partner.total_gift_count = len(amounts)
            partner.first_gift_date = min(dates) if dates else False
            partner.last_gift_date = max(dates) if dates else False

    @api.depends('lifetime_giving_amount', 'largest_gift_amount')
    def _compute_donor_tier(self):
        for partner in self:
            gift = partner.largest_gift_amount
            if gift >= 25000:
                partner.donor_tier = 'principal'
            elif gift >= 5000:
                partner.donor_tier = 'major'
            elif gift >= 5000:
                partner.donor_tier = 'midlevel'
            elif gift >= 500:
                partner.donor_tier = 'midlevel'
            else:
                partner.donor_tier = 'grassroots'

    @api.depends('donation_ids.donation_date', 'donation_ids.state')
    def _compute_lapsed_status(self):
        current_year = date.today().year
        last_year = current_year - 1

        for partner in self:
            confirmed = partner.donation_ids.filtered(lambda d: d.state in ('confirmed', 'receipted'))
            years_given = set(d.donation_date.year for d in confirmed if d.donation_date)

            gave_this_year = current_year in years_given
            gave_last_year = last_year in years_given
            gave_prior_years = any(y < last_year for y in years_given)

            partner.is_lybunt = (gave_last_year and not gave_this_year)
            partner.is_sybunt = (gave_prior_years and not gave_this_year and not gave_last_year)
