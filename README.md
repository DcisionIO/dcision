<p align="center">
  <a href="https://dcision.io">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DcisionIO/.github/main/assets/banner-dark.png">
      <img alt="Dcision — the decision layer for AI" src="https://raw.githubusercontent.com/DcisionIO/.github/main/assets/banner-light.png" width="100%">
    </picture>
  </a>
</p>

<p align="center">
  <a href="https://app.dcision.io"><img alt="Start free" src="https://img.shields.io/badge/start%20free-1M%20decisions%2Fmonth-34d399?style=for-the-badge"></a>
  <a href="https://docs.dcision.io"><img alt="Docs" src="https://img.shields.io/badge/docs-docs.dcision.io-111827?style=for-the-badge"></a>
  <a href="https://x.com/dcisionio"><img alt="Follow on X" src="https://img.shields.io/badge/follow-%40dcisionio-111827?style=for-the-badge&logo=x"></a>
  <a href="LICENSE"><img alt="MIT" src="https://img.shields.io/badge/license-MIT-111827?style=for-the-badge"></a>
</p>

<h3 align="center">Decide first. Reason when it matters.</h3>

---

## 🔥 The problem: most LLM answers are money burned

AI applications send **small decisions to large models**: *route this ticket*, *is this spam?*, *does this lead want
to buy?*, *escalate to a human?* Each one becomes an LLM call that:

- **costs tokens** — on every event, even the trivial ones;
- **adds latency** — the model writes text before anything happens;
- **returns free text** — your code has to parse it, and it can come back in a format you didn't expect;
- **can hallucinate** — a label that isn't in your list, a field that's missing, an action that doesn't exist.

**Dcision is the decision layer that sits before your agent or LLM.** You declare the questions once, in a schema.
Every call returns **typed answers with a confidence for each** — validated against your schema — and the **next
action**. The expensive reasoning only runs on the cases that actually need it.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DcisionIO/.github/main/assets/flow-dark.png">
  <img alt="Without Dcision an agent spends an LLM call and parses free text to pick the next action; with Dcision a typed answer with confidence picks it" src="https://raw.githubusercontent.com/DcisionIO/.github/main/assets/flow-light.png" width="100%">
</picture>

## ⚖️ LLM vs Dcision for micro-decisions

| Capability | LLM | **Dcision** |
| --- | --- | --- |
| Cost / 1M decisions | $300 and up | **~$24 incl. fallback\*** |
| Output | Unstructured text | **JSON validated against your schema** |
| Confidence | Not built in | **A confidence for every answer** |
| Next step | Parsed from free text | **Policies: `continue`, `block`, `escalate` or `fallback`** |
| Audit trail | Prompts and free text | **Version, action and reason for every execution** |

<sub>\* Illustrative example on the Growth plan, assuming 5% of decisions fall back to your own LLM — not a performance claim.</sub>

## 🧰 Jev alone vs Dcision — everything the engine leaves to you

Dcision runs your decisions on **Jev** (TypeSafe's decision model) or **Laya** (open source, on your own server). The
engine is the same — the difference is everything you don't have to build, maintain and monitor.

| | Engine API alone | **Dcision** |
| --- | --- | --- |
| **Actions per result** | You wire each result to the next system | **8 destination types** per option, level or threshold: fixed reply, structured JSON, LLM, agent, workflow, webhook, API request or function — signed deliveries with retries |
| **Webhook trigger** | You expose an endpoint and call the engine | **One URL per decision** — forms, CRMs, n8n, Make or Zapier run it without an API key |
| **Dashboard** | Questions live in your code | **Every decision in one place**, with immutable versions and full history |
| **Decoupled** | Decision logic mixed into the app | **Change decisions without redeploying your app** |
| **Visual builder** | Questions written by hand | **Form and visual editors, JSON preview and a Playground** |
| **Templates** | Start from a blank page | **Ready-made decisions** — lead qualification, support routing, spam, agent routing, RAG relevance… |
| **Fallback per question** | You read the confidence yourself | **Minimum confidence per question** and a reserved `other` option; below it, your policy acts |
| **Monitoring** | You build logs and metrics | **Overview** with volume, p50/p95 latency, errors, estimated cost and calibration suggestions |
| **MCP** | — | **Remote MCP server** for agents, plus a Claude Code skill |
| **CLI and SDKs** | — | Coming soon |

## 🚀 Get started in 5 minutes

**1. Create your account** at [app.dcision.io](https://app.dcision.io) — Google or an e-mail code. You start on the free
**Genesis** plan: 1M decisions a month.

**2. Create a decision** from a template (*Lead Qualification*, *Support Routing*, *Spam Detection*…) or paste one of the
[schemas in this repo](#-ready-made-decisions) into the editor. Try it in the **Playground** — Playground runs are free.

**3. Deploy** it and create an **API key** (`API keys → New key`):

```bash
export DCISION_API_KEY=dcs_live_...
```

**4. Call it** — [cURL](curl/run-decision.sh), [Node.js](node/run-decision.mjs) or [Python](python/run_decision.py):

```bash
curl -X POST https://api.dcision.io/v1/decisions/lead-qualification \
  -H "Authorization: Bearer $DCISION_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"state": {"message": "We need pricing for 500 users and want to start next month.", "company_size": 500, "source": "website"}}'
```

```jsonc
{
  "result":     { "purchase_intent": 0.9412, "priority": "high", "route": "sales" },
  "confidence": { "purchase_intent": 0.8824, "priority": 0.69, "route": 0.85 },
  "action": "continue",
  "action_reason": { "type": "default" }
  // + decision_id, execution_id, version, composites, metrics…
}
```

Route on `result` and `action` — there's no text to parse. See [Run a decision](https://docs.dcision.io/docs/api/run-decision).

## 🔌 Call it from anywhere

| Where | How |
| --- | --- |
| **Any language** | `POST https://api.dcision.io/v1/decisions/{slug}` with your API key ([examples](#-get-started-in-5-minutes)) |
| **No-code, CRMs, forms** | Turn on the decision's **webhook URL** — n8n, Make, Zapier, any form. [Docs](https://docs.dcision.io/docs/api/webhook-trigger) |
| **AI agents** | Remote MCP server at `https://api.dcision.io/mcp`. [Docs](https://docs.dcision.io/docs/mcp) |
| **Claude Code** | MCP + the Dcision skill: |

```bash
claude mcp add --transport http dcision https://api.dcision.io/mcp \
  --header "Authorization: Bearer $DCISION_API_KEY" --scope user

mkdir -p ~/.claude/skills/dcision
curl -fsSL https://docs.dcision.io/skills/dcision/SKILL.md -o ~/.claude/skills/dcision/SKILL.md
```

## 🧩 Ready-made decisions

Each file has the Decision Schema (`stateSchema`, `questions`, `policies`…) and a `sampleState` to try in the Playground.

| Decision | What it decides |
| --- | --- |
| [Agent Routing](schemas/agent-routing.json) | Choose the tool an AI agent should use and whether it needs an LLM. |
| [Customer Service Router (intent routing)](schemas/customer-service-router.json) | Classify intent and complexity in one call: lookups go to code, billing/tech to specialist LLMs, complaints and hard cases to humans. |
| [Lead Qualification](schemas/lead-qualification.json) | Score purchase intent, set priority and route an inbound lead. |
| [RAG Relevance](schemas/rag-relevance.json) | Check whether a retrieved chunk answers the query before calling the LLM. |
| [Resume Screening (composite scoring)](schemas/resume-screening.json) | Score each skill on its own rubric and combine them with role-specific weights — Senior IC vs Engineering Manager. |
| [Spam Detection](schemas/spam-detection.json) | Estimate spam probability and decide whether to allow, review or block. |
| [Support Routing](schemas/support-routing.json) | Pick the department, the urgency and whether a human is needed. |
| [Support Ticket Triage (fan-out)](schemas/ticket-triage.json) | One call answers category, bug severity, repro steps, refund and frustration; AND rules decide which answers matter. |
| [Voice Banking Commands (confidence-gated)](schemas/voice-banking.json) | Classify a spoken banking command; risky actions need more confidence than read-only ones before acting. |

## 💳 Pricing

**Genesis is free** — 1M decisions a month. Past the included volume, every plan keeps running on **prepaid credits**,
and adding a card gives you **$20 in free credits** (valid 90 days). Plans and prices at [dcision.io](https://dcision.io/en#pricing).

---

<p align="center">
  <a href="https://dcision.io"><b>dcision.io</b></a> · <a href="https://docs.dcision.io">Docs</a> · <a href="https://app.dcision.io">App</a> · <a href="https://x.com/dcisionio">X</a> · <a href="mailto:contact@dcision.io">contact@dcision.io</a><br>
  <sub>Examples in this repository are MIT-licensed.</sub>
</p>
