# WaterAid Canada — Non-Profit Fundraising & Donor Management (`wateraid_fundraising`)

An open-source custom module for **Odoo 17 / 18** developed to replace proprietary platforms like Blackbaud Raiser's Edge.

---

## 🌟 Key Features

1. **Constituent & Household Records (Hard vs. Soft Credit):**
   * Link individuals to Family Foundations, Spouses, and Corporate Matching donors.
   * Tracks who gets the tax receipt (Hard Credit) vs who gets relationship recognition (Soft Credit).

2. **CRA Regulation 3501 Tax Receipts:**
   * Automated sequential receipt numbering (`WAC-2026-000001`).
   * Advantage deduction (e.g., Gala ticket price minus meal value).
   * CRA-mandated replacement tracking (`"Replaces cancelled receipt #WAC-..."`).
   * Audit-ready PDF tax receipts with official signature and charity registration number (`119287595 RR 0001`).

3. **CFAP Fundraising Designation Hierarchy:**
   * **Campaign:** Overarching strategic initiative.
   * **Fund:** Restricted vs. Unrestricted fund tracking linked to Odoo's analytical accounting.
   * **Appeal:** Channel performance tracking (Direct Mail, Gala, Email).

4. **Multi-Year Pledges & Installments:**
   * Automated installment schedules, overdue alerts, and fulfillment tracking.

5. **LYBUNT / SYBUNT Analytics:**
   * Pre-computed giving statistics: Lifetime Total, First Gift, Largest Gift, Consecutive Years.
   * Native search filters for *Last Year But Unfortunately Not This* (LYBUNT) lapsed donors.

6. **AI Field-to-Donor Bridge:**
   * Integrates with `Odoo Field Service` to automatically draft donor stewardship briefs with verifiable provenance citations when water points are completed.

---

## 🛠️ Installation

1. Copy the `wateraid_fundraising` folder into your Odoo `addons/` directory.
2. In Odoo, activate **Developer Mode**.
3. Go to **Apps → Update Apps List**.
4. Search for `WaterAid Canada — Non-Profit Fundraising` and click **Activate**.
