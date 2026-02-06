# RAG-Based IP Licensing & Royalty Extraction Pipeline

## Overview
This project is an AI-powered **Retrieval-Augmented Generation (RAG)** system designed to
automatically extract **IP licensing, royalty, and revenue share terms** from unstructured
legal documents (PDF, DOCX, TXT).

The system converts complex contracts into **structured, audit-ready JSON** suitable for
royalty accounting, compliance, and analytics.

---

## Business Problem
Organizations managing intellectual property often face:
- Manual contract review
- Royalty underpayment or overpayment
- Audit and compliance risks
- Delayed revenue reconciliation

Even a **1–2% royalty leakage** can result in **millions in lost revenue** annually.

---

## Solution
This pipeline:
- Ingests contract documents
- Uses RAG to preserve legal context
- Extracts key clauses with high accuracy
- Outputs structured JSON for downstream systems

---

## Supported Inputs
- PDF (.pdf)
- Word Documents (.docx)
- Plain Text (.txt)

---

## Output Format
Each processed contract produces a JSON file containing:

```json
{
  "ip_owner": "",
  "licensee": "",
  "royalty_percentage": "",
  "revenue_share": "",
  "territory": "",
  "duration": "",
  "payment_terms": ""
}
