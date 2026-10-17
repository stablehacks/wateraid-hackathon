# -*- coding: utf-8 -*-
{
    'name': 'WaterAid Canada — Non-Profit Fundraising & Donor Management',
    'version': '17.0.1.0.1',
    'category': 'Non-Profit / Fundraising',
    'summary': 'Constituent management, CRA Regulation 3501 tax receipts, CFAP designations, and AI field-to-donor stewardship.',
    'description': """
WaterAid Canada Fundraising & Donor Management Module
=====================================================
An open-source non-profit constituent management and fundraising module built to replace proprietary tools like Blackbaud Raiser's Edge.

Key Capabilities:
-----------------
* **Constituent & Household Management:** Hard vs. Soft Credit tracking, family foundations, and relationship links.
* **CRA Regulation 3501 Tax Receipts:** Sequential receipt numbering, advantage calculation (split-receipting), and replacement receipt tracking.
* **Non-Profit CFAP Hierarchy:** Campaign, Fund (Restricted vs. Unrestricted general ledger linking), Appeal, and Package.
* **Multi-Year Pledges & Installments:** Automated installment schedules and payment tracking.
* **LYBUNT / SYBUNT Analytics:** Pre-computed giving metrics and lapsed donor filters.
* **AI Field-to-Donor Bridge:** Connects Odoo Field Service water point repairs directly to donor stewardship briefs.
    """,
    'author': 'WaterAid Canada / The AI Fellowship (stablehacks)',
    'website': 'https://github.com/stablehacks/wateraid-hackathon',
    'license': 'AGPL-3',
    'depends': ['base', 'mail', 'crm', 'account', 'project'],
    'data': [
        'security/security_groups.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/fund_views.xml',
        'views/donation_views.xml',
        'views/cra_receipt_views.xml',
        'views/pledge_views.xml',
        'views/constituent_views.xml',
        'views/menus.xml',
        'report/cra_receipt_report.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
