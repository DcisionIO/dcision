<p align="center">
  <a href="https://dcision.io">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DcisionIO/.github/main/assets/banner-dark.png">
      <img alt="Dcision — the decision layer for AI" src="https://raw.githubusercontent.com/DcisionIO/.github/main/assets/banner-light.png" width="100%">
    </picture>
  </a>
</p>

<p align="center">
  <a href="https://app.dcision.io"><img alt="Start free" src="https://img.shields.io/badge/start%20free-1M%20decisions%2Fmonth-34d399?style=flat-square"></a>
  <a href="https://docs.dcision.io"><img alt="Docs" src="https://img.shields.io/badge/docs-docs.dcision.io-111827?style=flat-square"></a>
  <a href="LICENSE"><img alt="MIT" src="https://img.shields.io/badge/license-MIT-111827?style=flat-square"></a>
</p>

# Dcision examples

Ready-to-use **Decision Schemas** and API calls for [Dcision](https://dcision.io) — the decision layer for AI.
Send any state, get typed answers (choice, score, probability) with a confidence for each, and a next action —
before your agent or LLM runs.

- Docs: <https://docs.dcision.io>
- App (free Genesis plan, 1M decisions a month): <https://app.dcision.io>
- X: [@dcisionio](https://x.com/dcisionio)

## 🚀 Run a decision in 3 steps

1. In the app, create a decision from a template (or paste one of the schemas below into the editor) and **Deploy** it.
2. Create an API key (**API keys → New key**) and export it: `export DCISION_API_KEY=dcs_live_...`
3. Call it — [cURL](curl/run-decision.sh), [Node.js](node/run-decision.mjs) or [Python](python/run_decision.py):

```bash
curl -X POST https://api.dcision.io/v1/decisions/lead-qualification \
  -H "Authorization: Bearer $DCISION_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"state": {"message": "We need pricing for 500 users and want to start next month.", "company_size": 500, "source": "website"}}'
```

The answer has the typed `result`, a `confidence` per question and the `action` (`continue`, `block`,
`escalate` or `fallback`) with its reason. See [Run a decision](https://docs.dcision.io/docs/api/run-decision).

## 🧩 Schemas

Each file has the schema (`stateSchema`, `questions`, `policies`…) and a `sampleState` to try in the Playground.

| Schema | What it decides | Patterns |
| --- | --- | --- |
| [Lead Qualification](schemas/lead-qualification.json) | Score purchase intent, set priority and route an inbound lead. | intent-routing, confidence-routing, composite-scoring |
| [Support Routing](schemas/support-routing.json) | Pick the department, the urgency and whether a human is needed. | intent-routing, confidence-routing |
| [Spam Detection](schemas/spam-detection.json) | Estimate spam probability and decide whether to allow, review or block. | intent-routing |
| [Agent Routing](schemas/agent-routing.json) | Choose the tool an AI agent should use and whether it needs an LLM. | intent-routing |
| [RAG Relevance](schemas/rag-relevance.json) | Check whether a retrieved chunk answers the query before calling the LLM. |  |
| [Support Ticket Triage (fan-out)](schemas/ticket-triage.json) | One call answers category, bug severity, repro steps, refund and frustration; AND rules decide which answers matter. | fan-out, intent-routing |
| [Voice Banking Commands (confidence-gated)](schemas/voice-banking.json) | Classify a spoken banking command; risky actions need more confidence than read-only ones before acting. | confidence-routing, intent-routing |
| [Resume Screening (composite scoring)](schemas/resume-screening.json) | Score each skill on its own rubric and combine them with role-specific weights — Senior IC vs Engineering Manager. | composite-scoring |
| [Customer Service Router (intent routing)](schemas/customer-service-router.json) | Classify intent and complexity in one call: lookups go to code, billing/tech to specialist LLMs, complaints and hard cases to humans. | intent-routing, confidence-routing |

## 🔌 Other ways to call a decision

- **Webhook URL** (no API key — forms, CRMs, n8n, Make, Zapier): [docs](https://docs.dcision.io/docs/api/webhook-trigger)
- **MCP server** for AI agents: `https://api.dcision.io/mcp` — [docs](https://docs.dcision.io/docs/mcp)
- **Claude Code skill**: [docs](https://docs.dcision.io/docs/claude-code)

```bash
# Claude Code: connect the MCP server and install the skill
claude mcp add --transport http dcision https://api.dcision.io/mcp \
  --header "Authorization: Bearer $DCISION_API_KEY" --scope user
mkdir -p ~/.claude/skills/dcision
curl -fsSL https://docs.dcision.io/skills/dcision/SKILL.md -o ~/.claude/skills/dcision/SKILL.md
```

## 📄 License

MIT — see [LICENSE](LICENSE).
