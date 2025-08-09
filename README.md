# NutriAgent: Coordinator with 3 Specialized Agents

This project implements a coordinator–specialist multi‑agent system using Google's Agent Development Kit (ADK). The coordinator routes user queries to one of three specialized agents.

## System Architecture

1. **Coordinator Agent**: Central router analyzing the user's query.
2. **Specialized Agents (3 total)**:
   - **Research AI Agent**: Web research and latest nutrition facts.
   - **Nutritionist RAG Agent**: Grounded guidance using curated knowledge sources.
   - **Personal AI Agent**: User‑specific data via backend APIs.

```
                 ┌─────────────────────┐
                 │  Coordinator Agent  │
                 └──────────┬──────────┘
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
  Research Agent     Nutritionist RAG     Personal Agent
```

## Coordinator and Agents

- `app/agents/coordinator_agent.py`: Coordinator wired to exactly three sub‑agents.
- `app/agents/research_agent.py`: Retrieves up‑to‑date nutrition information from the web.
- `app/agents/nutritionist_rag_agent.py`: Provides grounded nutritional guidance using local/curated knowledge.
- `app/agents/personal_agent.py`: Handles user‑specific context and personalization via backend APIs.

Note: Additional agent files exist in `app/agents/` from an earlier, broader schema, but the coordinator currently delegates only to the three agents above.

## Usage

Interact with the system via the coordinator defined in `app/agents/coordinator_agent.py`.

Typical flow:
1. User sends a query.
2. Coordinator selects the most appropriate specialist based on routing rules.
3. Selected specialist handles the request and returns the response.

For an alternate entry point with the same three‑agent wiring, see `app/nutrisionist_agent/agent.py`.

## Tools

Agents may use search and local knowledge sources as configured in their implementations (e.g., web search for the Research agent, RAG for the Nutritionist agent).