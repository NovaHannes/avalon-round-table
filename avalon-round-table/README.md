# ARTE – Avalon Round Table Engine

**ARTE** is an open-source framework for building **multi-agent AI councils** that deliberate, dissent, and converge on more robust, transparent conclusions than any single LLM can achieve alone.

> “Single LLMs are brilliant, but brittle. ARTE replaces solitary oracles with automated peer review.”

---

## 🌟 Vision

ARTE is a framework to orchestrate structured deliberation between multiple large language models (LLMs) — like GPT-4, Gemini, Grok, Claude — each playing a unique epistemic role (e.g. Synthesizer, Contrarian, Ethicist, Fact-Checker). It is built on a protocol of contestation and consensus.

---

## 🧠 What Does It Do?

- **Combats hallucination** via inter-agent critique and arbitration  
- **Promotes transparency** by exposing reasoning paths and disagreements  
- **Encourages emergence** via structured dissent  
- **Automates complex decisions** with modular agent logic

---

## 🔨 Help Us Build the First Module

### 👇 The Immediate Challenge

> **We need your help to automate the deliberation process.**

The current workflow involves manual copy-paste between models. Your first mission is to build the **Scribe Automator** — a core module that uses APIs to simulate a round-table discussion between agents.

---

### 🎯 First Bounty: `scribe_automator.py`

Help us create the orchestrator that:
- Takes a user prompt
- Dispatches it to 3–4 agents (e.g. GPT-4, Gemini, Grok)
- Collects their initial responses
- Dispatches critiques between agents
- Collects verdicts or synthesizes the outcome

---

## 🏗️ Project Structure

```bash
arte/
├── agents/
│   ├── base_agent.py
│   ├── sir_nexus.py         # Synthesizer (GPT-4)
│   ├── sir_lancelot.py      # Contrarian (Grok)
│   └── sir_cadmus.py        # Fact & Info (Gemini)
├── core/
│   ├── orchestrator.py      # Manages deliberation rounds
│   └── schema.py            # Shared data types (Prompt, Critique, Verdict)
├── scribe_automator.py      # CLI entrypoint for running a trial
├── README.md
├── CONTRIBUTING.md
└── requirements.txt

