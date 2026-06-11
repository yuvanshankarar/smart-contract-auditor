# Smart Contract Auditor

AI-powered Smart Contract Security Auditor built with FastAPI, Next.js, LangGraph, and Slither.

## Features

* Real Slither vulnerability detection
* AI-generated security explanations
* Remediation recommendations
* Dynamic security scoring
* PDF audit report generation
* Scan history persistence with SQLite
* Interactive Next.js dashboard
* LangGraph multi-agent workflow

## Architecture

Frontend:

* Next.js
* TypeScript
* Tailwind CSS

Backend:

* FastAPI
* LangGraph
* SQLAlchemy
* SQLite

Security Analysis:

* Slither
* Custom scoring engine

Reporting:

* ReportLab PDF generation

## Workflow

1. Upload Solidity contract
2. Run Slither analysis
3. Parse findings
4. Calculate security score
5. Generate AI explanation
6. Generate remediation guidance
7. Create PDF audit report
8. Store results in SQLite
9. Display findings in dashboard

## Example Findings

* Reentrancy
* Low-level calls
* Solidity version issues
* Access control vulnerabilities
* Other Slither-supported detectors

## Screenshots

Add screenshots here:

* Dashboard
* Findings Table
* Scan History
* PDF Report

## Local Setup

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Future Improvements

* Docker deployment
* GitHub Actions CI/CD
* User authentication
* Multi-file project scanning
* Severity filtering
* Detailed scan pages
* Cloud deployment

## Tech Stack

* Python
* FastAPI
* LangGraph
* Slither
* SQLAlchemy
* SQLite
* Next.js
* TypeScript
* Tailwind CSS
* ReportLab
