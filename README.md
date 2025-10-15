# AI-Powered Legal Research System

> Advanced RAG-based legal intelligence platform for SRM VDP HackElite Hackathon

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/) [![PyTorch](https://img.shields.io/badge/PyTorch-2.8.0-red.svg)](https://pytorch.org/) [![Streamlit](https://img.shields.io/badge/Streamlit-1.48.1-FF4B4B.svg)](https://streamlit.io/) [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## Overview

A Retrieval-Augmented Generation (RAG) system that accelerates legal research by combining trusted legal PDFs with state-of-the-art language models. Delivers comprehensive, source-backed answers in seconds with confidence scores and caching.

### Key Features

- **Two-Stage Retrieval**: FAISS dense vector search + cross-encoder re-ranking
- **Comprehensive Answers**: 150-300 word responses with legal principles and examples
- **Confidence Scoring**: Transparent 0-100% reliability estimates
- **Smart Caching**: Reduces repeat query latency to <0.1 seconds
- **Web Interface**: Streamlit dashboard for easy interaction

---

## Technology Stack

| Component       | Technology                     | Purpose                        |
|-----------------|---------------------------------|--------------------------------|
| Language        | Python 3.13                    | Core programming language      |
| Framework       | Streamlit 1.48.1               | Web interface                  |
| Embeddings      | SentenceTransformers all-MiniLM-L6-v2 | Semantic vector generation    |
| Re-ranker       | Cross-Encoder ms-marco-MiniLM-L-6-v2 | Improves retrieval precision  |
| Generator       | google/flan-t5-small           | Generates detailed answers     |
| Vector Database | FAISS (IndexFlatL2)            | Fast similarity search         |
| PDF Processing  | PyPDF2                         | Extracts text from legal PDFs  |

## Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/Sanjaykrishnaob/AI-Powered-Justice-System.git
   cd AI-Powered-Justice-System
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the Streamlit app**
   ```bash
   python launch.py
   # Or: streamlit run app.py
   ```

4. **Open the app**: Visit `http://localhost:8501` in your browser.

---

## Sample Queries

- What are the fundamental rights guaranteed by the Indian Constitution?
- What legal challenges exist around AI in the judiciary?
- How can a Public Interest Litigation be filed in India?

---

## Project Structure

```
AI-Powered-Justice-System/
├── app.py               # Streamlit application
├── launch.py            # Convenience launcher
├── VDP.ipynb            # Jupyter notebook workflow
├── Docs/                # Source PDFs (user supplied)
├── rag_cache/           # Persistent caches
├── faiss.index          # FAISS vector store
├── requirements.txt     # Python dependencies
└── .streamlit/config.toml
```

---

## Hackathon Context

- **Event**: SRM VDP HackElite Hackathon (October 2025)
- **Challenge**: AI-Powered Justice System
- **Objective**: Build a legal research engine to improve speed, accuracy, and accessibility

---

