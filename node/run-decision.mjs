// Node.js 18+ (global fetch). Server-side only: never ship an API key to a browser.
// Usage: DCISION_API_KEY=dcs_live_... node run-decision.mjs [slug]
const slug = process.argv[2] ?? "lead-qualification";
const state = {
  message: "We need pricing for 500 users and want to start next month.",
  company_size: 500,
  source: "website",
};

const response = await fetch(`https://api.dcision.io/v1/decisions/${slug}`, {
  method: "POST",
  headers: { Authorization: `Bearer ${process.env.DCISION_API_KEY}`, "Content-Type": "application/json" },
  body: JSON.stringify({ state }),
});
const decision = await response.json();
if (!response.ok) throw new Error(`${decision.error.code}: ${decision.error.message}`);

// Route on the typed answer and the action — no text to parse.
console.log(decision.action, decision.result, decision.confidence);
