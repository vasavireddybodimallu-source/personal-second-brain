# Personal Second Brain

A North-Star-driven information filter for AI/LLM learning and project building.

## North Star

By November 2026, I will build and launch 2 working AI/LLM applications
used by at least 50 real users, so I can demonstrate practical AI
development skills for internship opportunities.

## Problem

I consume information from GitHub, 100xEngineers, tutorials and my own
AI projects.

The problem is that collecting more information does not necessarily
move me closer to my goal.

This project filters incoming information against my North Star.

## Architecture

Raw Sources
    ↓
Deterministic Ingestion
    ↓
Markdown Second Brain
    ↓
LLM Personalization Engine
    ↓
Scoring + Prioritization
    ↓
Synthesized Notes
    ↓
Recommended Actions

## Folder Structure

personal-second-brain/
│
├── engine/
│   ├── prompt.md
│   ├── scoring-results.md
│   └── ingest.py
│
├── raw/
│   ├── item-01.md
│   ├── item-02.md
│   └── ...
│
├── synthesized/
│   ├── ingestion-batch.md
│   └── weekly-summary.md
│
├── north-star.md
├── sources.md
└── README.md

## How It Works

### 1. Ingestion

Python reads Markdown files from the `raw/` folder.

```bash
python engine/ingest.py