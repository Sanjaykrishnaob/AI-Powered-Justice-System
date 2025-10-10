# AI-Powered Legal Research System

A sophisticated Retrieval-Augmented Generation (RAG) system designed to enhance legal research through AI, making judicial processes faster, fairer, and more transparent.

## 🎯 Project Overview

This project was developed for the **SRM VDP Hackathon** as a solution to the "AI-Powered Justice System" challenge. It demonstrates how artificial intelligence can revolutionize legal research by providing accurate, source-backed answers from legal documents.

### Key Features

- **Intelligent Document Processing**: Automatically extracts and processes text from legal PDF documents
- **Semantic Search**: Uses advanced embeddings to find relevant legal passages based on meaning, not just keywords
- **RAG Pipeline**: Combines retrieval and generation for accurate, context-aware legal analysis
- **Source Attribution**: Every answer includes citations to specific documents and sections
- **Optimized for Legal Domain**: Custom prompts and formatting tailored for legal research

## 🏗️ Architecture

The system consists of three main components:

1. **Document Ingestion Layer**
   - PDF text extraction using PyPDF2
   - Intelligent text chunking with overlap for context preservation
   - Batch processing for efficient handling of multiple documents

2. **Retrieval Engine**
   - Sentence-BERT embeddings (all-MiniLM-L6-v2) for semantic understanding
   - FAISS vector database for fast similarity search
   - Top-k retrieval with relevance scoring

3. **Generation Layer**
   - Google FLAN-T5 model for answer generation
   - Context-aware prompting for legal domain
   - Token optimization to prevent overflow

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Windows OS (adapted for local development)
- 4GB+ RAM recommended
- GPU optional (CPU-compatible)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/legal-ai-research.git
cd legal-ai-research
```

2. Install required packages:
```bash
pip install sentence-transformers faiss-cpu transformers PyPDF2 torch
```

3. Place your legal PDF documents in the `Docs/` folder

4. Open and run `VDP.ipynb` in Jupyter Notebook or VS Code

## 📊 Usage

### Basic Usage

1. **Setup**: Run cells 1-3 to install dependencies and initialize the RAG system
2. **Load Enhanced Functions**: Run cell 4 to enable optimized legal query processing
3. **Query**: Use cells 5-9 to test with pre-configured or custom legal questions

### Example Queries

```python
# Example 1: General legal overview
answer_query("What are the main legal challenges discussed regarding AI and justice?")

# Example 2: Specific legal analysis
answer_query("Explain the implications of AI in judicial decision making")

# Example 3: Ethical considerations
answer_query("What are the ethical considerations for AI in the legal system?")
```

### Sample Output

```
Question: What are the main legal challenges discussed regarding AI and justice?

Answer:
The main legal challenges include ensuring fairness and non-discrimination in AI 
systems used in judicial processes. The Constitution prohibits discrimination based 
on certain markers while also providing for positive discrimination through affirmative 
action.

AI systems must be transparent and explainable to maintain public trust in the 
justice system. There are concerns about algorithmic bias that could perpetuate 
existing inequalities in legal outcomes.

Sources Referenced:
  1. Responsible-AI-22022021.pdf (chunk 106)
  2. AI_and_India_Justice_CambridgeUPress.pdf (chunk 11)
  3. legal 3.pdf (chunk 16)
```

## 🛠️ Technical Details

### Technologies Used

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Embeddings | Sentence-BERT (all-MiniLM-L6-v2) | Semantic text understanding |
| Vector DB | FAISS | Fast similarity search |
| LLM | Google FLAN-T5-small | Answer generation |
| PDF Processing | PyPDF2 | Document text extraction |
| Deep Learning | PyTorch | Model backend |

### System Specifications

- **Chunk Size**: 800 characters with 150-character overlap
- **Embedding Dimension**: 384 (MiniLM)
- **Top-k Retrieval**: 4 most relevant chunks
- **Max Context**: 1800 characters
- **Max Generation**: 300 tokens
- **Index Type**: Flat L2 (FAISS)

## 📁 Project Structure

```
SRM VDP HACKATHON/
│
├── VDP.ipynb                 # Main Jupyter notebook
├── README.md                 # This file
├── faiss.index              # Vector database (generated)
├── rag_metas.pkl            # Metadata storage (generated)
│
└── Docs/                    # Legal documents folder
    ├── AI_and_India_Justice.pdf
    ├── Responsible-AI.pdf
    ├── legal1.pdf
    ├── legal2.pdf
    └── ...
```

## 🎓 Hackathon Context

### Problem Statement

**Challenge 13: AI-Powered Justice System**

Participants create a prototype highlighting one key function of their legal-AI system. This could be:
- Case-outcome prediction model
- Legal research engine ✓ (This project)
- Dashboard visualizing legal case data

### Solution Approach

This project focuses on the **Legal Research Engine** track, demonstrating AI's ability to:

1. **Speed**: Instant retrieval of relevant legal information from multiple documents
2. **Fairness**: Unbiased, fact-based answers sourced directly from legal texts
3. **Transparency**: Full source attribution and citation for every response

## 🔬 Performance Optimizations

- **Token Management**: Automatic context truncation to prevent overflow
- **Batch Processing**: Efficient embedding generation for large document sets
- **CPU Compatibility**: Runs without GPU requirement
- **Memory Efficiency**: Optimized chunk sizes and batch processing

## 📈 Future Enhancements

- [ ] Case outcome prediction using historical legal data
- [ ] Interactive web dashboard with Streamlit/Gradio
- [ ] Multi-language support for international legal systems
- [ ] Fine-tuned legal domain model
- [ ] Citation graph visualization
- [ ] Integration with legal databases and APIs

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Your Name** - *Initial work* - [YourGitHub](https://github.com/yourusername)

## 🙏 Acknowledgments

- SRM VDP Hackathon organizers
- Hugging Face for pre-trained models
- FAISS team for the vector search library
- The open-source AI community

## 📧 Contact

For questions or feedback, please reach out:

- Email: your.email@example.com
- LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)
- Project Link: [https://github.com/yourusername/legal-ai-research](https://github.com/yourusername/legal-ai-research)

---

**Note**: This is a hackathon prototype for educational and demonstration purposes. For production legal research systems, additional considerations around data security, compliance, and professional legal standards would be required.
