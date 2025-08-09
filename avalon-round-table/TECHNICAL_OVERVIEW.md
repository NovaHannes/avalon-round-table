# 🧠 Avalon Round Table Engine – Technical Overview

**Version:** 0.1.0  
**Last Updated:** 2025-08-08

---

## 🚀 Overview

This document provides a technical breakdown of the Avalon Round Table Engine (ARTE), a modular, schema-driven, multi-agent deliberation system. It is designed to allow structured disagreement, refinement, and consensus-building between autonomous agents.

---

## 📁 Project Structure

```bash
avalon-round-table/
├── arte/
│   ├── agents/                 # Individual agents (logic, responses)
│   │   ├── base_agent.py       # Abstract base class for all agents
│   │   └── agent_interface.py  # Interface contract for agent methods
│   ├── core/
│   │   └── orchestrator.py     # Orchestration logic for coordinating agents
│   ├── schemas/
│   │   └── deliberation.py     # Pydantic models for Prompt, Response, Critique, Verdict
├── arte_modules/
│   ├── concord.py              # Verdict synthesis engine
│   ├── deliberation_engine.py  # Step-by-step deliberation rounds
│   ├── signal_relay.py         # Communication between agents
├── data/
│   └── sample_roundtable_config.json  # Example input config for a roundtable session
├── main.py                     # CLI entry point for running a deliberation
├── CHANGELOG.md
├── README.md
├── TECHNICAL_OVERVIEW.md       # (This file)
└── requirements.txt
```

---

## 🧩 Core Modules

### `arte/agents/`
- **`base_agent.py`**: Defines the base class all agents inherit from.
- **`agent_interface.py`**: Agent interface defining required methods.

### `arte/core/orchestrator.py`
Handles initialization and delegation logic for agents in a deliberation round. Key responsibilities:
- Loading agent modules dynamically
- Coordinating prompt -> response -> critique -> verdict phases

### `arte_modules/deliberation_engine.py`
The core driver of structured deliberation. It manages:
- Dispatching the initial prompt
- Collecting responses
- Exchanging critiques
- Synthesizing or arbitrating a final verdict

### `arte_modules/signal_relay.py`
Acts as a communication bus between agents and the orchestrator.

---

## 📐 Data Schemas

Defined in `arte/schemas/deliberation.py` using Pydantic:

- `Prompt`: Initial user query
- `AgentResponse`: Each agent's answer
- `Critique`: One agent's review of another's response
- `Verdict`: Final output or consensus

These schemas are passed between functions and ensure data validation at every stage.

---

## 🧪 How to Run

```bash
cd avalon-round-table
export PYTHONPATH=.
python main.py
```

This executes the orchestrator using `sample_roundtable_config.json` and writes the final log to disk.

---

## 🔧 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

---

## 📌 Versioning

This documentation corresponds to release `0.1.0`, the “Genesis Commit”:
- Basic prompt dispatch and response cycle
- Static agent behavior (LLM calls mocked or stubbed)
- Modular architecture established

---

## 🧭 Next Steps

- Plug in real LLM APIs (e.g. OpenAI, Anthropic)
- Add critique weighting and verdict scoring
- Implement live streaming or WebSocket relay for UI integration

---

