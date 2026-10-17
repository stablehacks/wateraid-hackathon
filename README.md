# Reimagining WaterAid Canada with AI and Open-Source
### *Track C: Systems Blueprint (Challenge C1) — The AI Fellowship WaterAid Hackathon*

[![Status](https://img.shields.io/badge/Status-Submission%20Ready-emerald.svg)](PROPOSAL.md)
[![Track](https://img.shields.io/badge/Track-C%3A%20Systems%20Blueprint-blue.svg)](https://theaifellowship.ca/c/wateraid)
[![Stack](https://img.shields.io/badge/Core-Odoo%20Open--Source%20%2B%20AI%20Orchestration-cyan.svg)](odoo_highlighted_modules.png)
[![Addon](https://img.shields.io/badge/Odoo%20Module-wateraid__fundraising-purple.svg)](addons/wateraid_fundraising/)
[![Cost Analysis](https://img.shields.io/badge/Cost%20Analysis-3--Way%20Comparison-orange.svg)](ADDENDUM_COST_ANALYSIS.md)

---

## 🎯 Project Overview

WaterAid Canada operates with a lean team managing an ambitious mandate: raising vital philanthropic capital, stewarding complex institutional grants (e.g., Global Affairs Canada), and influencing national water policy to support sustainable WASH (Water, Sanitation, and Hygiene) programs globally.

Current non-profit models force organizations to scale administrative overhead in linear proportion to their grant and donor volume. **This blueprint breaks that linear constraint.**

By pairing an **open-source operational core (Odoo Community)** self-hosted in Canada with a **multi-agent AI orchestration layer**, WaterAid Canada eliminates proprietary software licensing costs while multiplying staff mission capacity by **4.2x over 3 years**—with zero staff reductions and strict Canadian privacy compliance (PIPEDA).

---

## 🚀 Quick Links & Artifacts

| Resource | File | Description |
| :--- | :--- | :--- |
| 📊 **Executive Pitch Deck** | [`pitch_deck.html`](pitch_deck.html) *(or [`index.html`](index.html))* | Interactive 10-slide presentation with 5-minute timer, keyboard navigation, speaker scripts, and Canadian sector leadership strategy. |
| 🖥️ **Working Prototype** | [`dashboard.html`](dashboard.html) | Interactive web dashboard demonstrating Odoo field ticket ingestion and clickable citation verification. |
| 📄 **Full Technical Proposal** | [`PROPOSAL.md`](PROPOSAL.md) | Comprehensive 3-year Systems Blueprint, architectural specifications, Canadian sector leadership model, and gating criteria. |
| 💰 **3-Way Cost Analysis Addendum** | [`ADDENDUM_COST_ANALYSIS.md`](ADDENDUM_COST_ANALYSIS.md) | Detailed comparison: Current Proprietary Stack ($87.5k/yr) vs. Odoo Hosted ($8.4k/yr) vs. Self-Hosted ($13.6k/yr). |
| 🧩 **Odoo Module Map** | [`odoo_highlighted_modules.png`](odoo_highlighted_modules.png) | Visual layout of the 11 targeted Odoo modules configured for WaterAid Canada. |
| 📦 **Custom Odoo Module** | [`addons/wateraid_fundraising/`](addons/wateraid_fundraising/) | Production-ready open-source Odoo 17/18 module: CRA Reg. 3501 tax receipts, CFAP designations, pledges, and AI stewardship. |

---

## 💰 Financial Summary: 3-Way Cost Analysis (20 Users)

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ Annual Operational Cost Comparison (20 Users)                                         │
├─────────────────────────────────────────────────┬──────────────────────┬───────────────┤
│ Operational Model                               │ Annual Cost (CAD)    │ 3-Year Total  │
├─────────────────────────────────────────────────┼──────────────────────┼───────────────┤
│ 1. Current State of Play (Blackbaud/SaaS Stack) │ CA$87,457.64 / year  │ CA$262,372.92 │
│ 2. Odoo Hosted (Odoo.com SaaS Benchmark)        │ CA$8,448.00 / year   │ CA$25,344.00  │
│ 3. Odoo Self-Hosted (Canadian Cloud + AI Layer) │ CA$13,620.00 / year* │ CA$40,860.00  │
└─────────────────────────────────────────────────┴──────────────────────┴───────────────┘
*Includes $6,000/yr for AI multi-agent tokens and $6,000/yr for managed DevOps support. 
Cloud compute & infrastructure alone is only ~CA$1,620/year.
```

**Net 3-Year Cash Savings with Self-Hosted Blueprint:** **CA$221,512.92 reinvested directly into WASH programming.**  
👉 *See the full line-item breakdown in [ADDENDUM_COST_ANALYSIS.md](ADDENDUM_COST_ANALYSIS.md).*

---

## 📦 The `wateraid_fundraising` Odoo Module

Located in [`addons/wateraid_fundraising/`](addons/wateraid_fundraising/), this custom module delivers full feature-parity with Blackbaud Raiser's Edge:

1. **Constituent & Household Records (Hard vs. Soft Credit):**
   * Extends `res.partner` with household accounts, spouses, family foundation trustees, and relationship links.
   * Hard Credit for official tax receipt recipients; Soft Credit for relationship/influencer recognition.
2. **CRA Regulation 3501 Tax Receipts:**
   * Automated sequential receipt numbering (`WAC-2026-000001`).
   * Advantage deduction (e.g., Gala ticket price minus meal value).
   * CRA-mandated replacement tracking (`"Replaces cancelled receipt #WAC-..."`).
   * Audit-ready QWeb PDF tax receipts with official signature and charity registration number (`119287595 RR 0001`).
3. **CFAP Fundraising Designation Hierarchy:**
   * **Campaign:** Overarching strategic initiative (e.g. *Clean Water 2026–2029*).
   * **Fund:** Restricted vs. Unrestricted fund tracking linked directly to Odoo analytical accounting.
   * **Appeal:** Channel performance tracking (Direct Mail, Gala, Email).
4. **Multi-Year Pledges & Installments:**
   * Automated installment schedules, overdue alerts, and fulfillment tracking (`wateraid.pledge`).
5. **LYBUNT / SYBUNT Analytics:**
   * Pre-computed giving statistics: Lifetime Total, First Gift, Largest Gift, Consecutive Years.
   * Native search filters for *Last Year But Unfortunately Not This* (LYBUNT) lapsed donors.
6. **AI Field-to-Donor Bridge:**
   * Action hook connecting `Odoo Field Service` water point repair tickets to automated, citation-backed donor stewardship briefs.

---

## 🏗️ The 3-Tier Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       Tier 3: Human-in-the-Loop Desks                       │
│       Development Officer       Program Director       Executive Board      │
│     (Donor Stewardship Desk)  (Grant Compliance Desk) (Governance Monitor) │
└──────────────────────────────────────▲──────────────────────────────────────┘
                                       │ Actionable Briefs & Sign-offs
┌──────────────────────────────────────┴──────────────────────────────────────┐
│                  Tier 2: AI Multi-Agent Orchestration Layer                 │
│  • Donor Intelligence Agent (RAG)      • GAC Grant Compliance Auditor       │
│  • Field Impact Synthesizer            • Hallucination Guard & PII Scrubber │
└──────────────────────────────────────▲──────────────────────────────────────┘
                                       │ Python JSON-RPC / Webhooks
┌──────────────────────────────────────┴──────────────────────────────────────┐
│             Tier 1: Open-Source Operational Substrate (Odoo Core)           │
│   CRM • Subscriptions • Documents • Sign • Project • Field Service • Acct   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🛡️ Trust & Governance: Humans Hold the Keys

Reputation and trust are non-negotiable for an international development charity:
* **Zero Autonomous Releases:** The AI layer drafts reports and flags compliance obligations, but **no external email is ever transmitted and no grant filing is submitted without explicit human staff authorization**.
* **Zero Hallucinations (Clickable Citations):** Every metric generated by the AI includes a clickable citation linking directly to the underlying technician signature, sensor log, or contract clause.
* **Canadian Data Sovereignty:** Self-hosted on Canadian soil under PIPEDA regulations; zero donor financial data is ever retained or used to train public foundation models.

---

## ⏱️ Disciplined 3-Year Implementation Roadmap

```
 ┌────────────────────────────────────────────────────────────────────────────────────────┐
 │ 36-Month Accelerated Delivery Horizon                                                  │
 ├─────────────────────────┬──────────────────────────────────┬───────────────────────────┤
 │ Phase & Focus           │ Key Milestones                   │ Evidence-Based Gate       │
 ├─────────────────────────┼──────────────────────────────────┼───────────────────────────┤
 │ Year 1 (Months 1–12)    │ • Canadian Odoo sandbox deploy   │ 🎯 Gate 1 (Month 6):      │
 │ Foundation & Donor      │ • Impact-to-Donor pilot test     │ Expand to production if   │
 │ Stewardship Pilot       │ • Staff training & HITL review   │ accuracy > 96% & time     │
 │                         │ • Rollout to development team    │ saved > 5 hrs/week.       │
 ├─────────────────────────┼──────────────────────────────────┼───────────────────────────┤
 │ Year 2 (Months 13–24)   │ • GAC Grant Auditor integration  │ 🎯 Gate 2 (Month 18):     │
 │ Institutional Grants &  │ • Odoo Project & Field Service   │ Expand to federal filings │
 │ Cross-Department Ops    │ • Country Programme logs synced  │ if 100% GAC clause pass   │
 │                         │ • Automated milestone alerts     │ & 0 compliance flags.     │
 ├─────────────────────────┼──────────────────────────────────┼───────────────────────────┤
 │ Year 3 (Months 25–36)   │ • Odoo Accounting fund tracking  │ 🎯 Gate 3 (Month 30):     │
 │ Full Operations &       │ • CEO & Board dashboard live     │ Full maturity sign-off;   │
 │ Global Federation Mesh  │ • Open-source "WaterAid NGO      │ transition from pilot to  │
 │                         │   Distribution" on GitHub        │ permanent steady state.   │
 └─────────────────────────┴──────────────────────────────────┴───────────────────────────┘
```

---

## 💰 The Board ROI (The Human Bottom Line)

* **CA$221,000+ Cumulative Cash Saved:** Replaces recurring proprietary SaaS fees over 3 years, reinvesting capital directly into clean water points.
* **6,800 Staff Hours/Year Multiplied:** Routine administrative and compliance burden eliminated.
* **+4 FTE Capacity Added:** Output equivalent to adding 4 senior full-time grant and development officers with $0 added payroll.
* **140,000 Additional People Reached:** Measurable expansion in WaterAid Canada's clean water and sanitation footprint.

---

## 📄 License & Attribution

Developed as a submission for **The Foundry Vol. I: Water Hackathon (The AI Fellowship Toronto Chapter in support of WaterAid Canada)**.  
Open-source under the MIT / AGPL-3 License.
