# RAG-based Question Answering Bot

A Question Answering system built using Retrieval Augmented Generation (RAG) that can answer questions based on provided PDF documents.

## Project Overview

This project implements a Question Answering bot that uses RAG architecture to provide accurate answers from PDF documents. The system processes PDF files, creates embeddings, stores them in a vector database, and uses retrieval mechanisms to find relevant context before generating answers.

## Features

- PDF document processing and text extraction
- Text chunking and embedding generation
- Vector database storage for efficient retrieval
- Question answering using RAG architecture
- Interactive interface for querying the system

## Project Structure

```
├── data
│   └── raw           # Contains input PDF documents
├── screenshots       # Project documentation images
├── qa_bot_app.py    # Main application file
├── test.py          # Test suite
├── pyproject.toml   # Project dependencies and configuration
└── uv.lock          # Lock file for dependencies
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/chitrakumarsai/Rag_QAbot_IMB_casestudy.git
cd Rag_QAbot_IMB_casestudy
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Place your PDF documents in the `data/raw` directory
2. Run the application:
```bash
python qa_bot_app.py
```
3. Ask questions about the content in your PDF documents

## Implementation Details

The project implements the following key components:

1. **PDF Loading**: Processes PDF documents and extracts text content
2. **Text Chunking**: Splits text into manageable chunks for processing
3. **Embedding Generation**: Creates vector representations of text chunks
4. **Vector Database**: Stores embeddings for efficient similarity search
5. **Question Answering**: Uses RAG to generate accurate answers

## Screenshots

The project includes several screenshots demonstrating different components:

- Code Splitter Implementation
- Embedding Generation Process
- PDF Loading Mechanism
- QA Bot Interface
- Retriever Component
- Vector Database Integration

## Requirements

- Python 3.8+
- Dependencies listed in pyproject.toml

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Created by Chitra Kumar Sai