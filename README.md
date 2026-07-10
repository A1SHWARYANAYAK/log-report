# Log Report

A benchmark task for evaluating autonomous AI agents on log parsing and structured report generation.

The task requires an AI agent to parse an Apache-style access log, compute summary statistics, and generate a deterministic JSON report that satisfies a predefined schema.

This project was developed as part of the Handshake AI Dynamo benchmark suite for evaluating software engineering and data-processing capabilities of autonomous coding agents.

---

## Problem Overview

Given an Apache access log, the agent must generate:

- Total number of requests
- Number of unique client IP addresses
- Most frequently requested endpoint

The final report is written as:

```
/app/report.json
```

and is automatically validated against a deterministic test suite.

---

## Repository Structure

```
task/
├── instruction.md          # Task specification
├── task.toml               # Harbor task metadata
├── environment/
│   ├── Dockerfile
│   └── access.log
├── solution/
│   ├── solve.py
│   └── solve.sh
└── tests/
    ├── test.sh
    └── test_outputs.py
```

---

## Technologies

- Python
- Regular Expressions
- JSON
- Docker
- Harbor
- Pytest

---

## Evaluation Pipeline

```
Apache Access Log
        │
        ▼
Parse Log Entries
        │
        ▼
Compute Statistics
        │
        ▼
Generate report.json
        │
        ▼
Automated Pytest Verification
```

---

## Learning Objectives

This benchmark evaluates an agent's ability to:

- Parse semi-structured log files
- Extract structured information
- Perform deterministic aggregation
- Generate schema-compliant JSON
- Produce reproducible outputs

---

## Part of

Handshake AI — Project Dynamo

Benchmark Engineering for Autonomous AI Agents.
