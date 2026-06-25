# AIE Workshop: How Jmail Leveraged Reducto

This workshop walks through parsing real scanned documents with the Reducto CLI.

---

## Prerequisites

- A Reducto account → [studio.reducto.ai](https://studio.reducto.ai)

---

## Setup

```bash
pip3 install reducto-cli
reducto login          # opens Reducto Studio in your browser — one-time auth
```

---

## Part 1: Parse Documents with the Reducto CLI

The `/docs` folder contains 5 sample FBI FOIA documents. Parse them all with one command:

```bash
reducto parse ./docs
```

Each PDF is parsed and saved alongside the source as `<filename>.parse.md`. Open any of them to see Reducto's structured output.

Some flags worth trying:

```bash
reducto parse ./docs --agentic            # enhanced table + figure accuracy
reducto parse ./docs --hyperlinks         # include embedded links
reducto parse ./docs --agentic --hyperlinks --comments
```

---

## Resources

- Reducto CLI docs: [docs.reducto.ai/cli](https://docs.reducto.ai/cli)
- Reducto docs: [docs.reducto.ai](https://docs.reducto.ai)
- Jmail Data API: [data.jmail.world](https://data.jmail.world)
