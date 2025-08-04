# Expert Knowledge Worker - RAG System

## Overview

This Jupyter notebook implements a **Retrieval Augmented Generation (RAG)** system for Insurellm, an insurance technology company. The system creates an expert knowledge worker that can answer questions based on the company's internal knowledge base with high accuracy and low cost.

## 🎯 Purpose

The system is designed to:

- Provide accurate answers to employee questions about company information
- Reduce costs by using RAG instead of fine-tuning large language models
- Enable employees to quickly access company knowledge across multiple domains
- Visualize and understand the knowledge base structure

## 🏗️ Architecture

### Core Components

1. **Document Processing**

   - Loads documents from `knowledge-base/` directory
   - Supports multiple document types: company, contracts, employees, products
   - Splits documents into chunks for better retrieval

2. **Vector Database**

   - Uses Chroma as the vector store
   - OpenAI embeddings for semantic search
   - 1,536-dimensional vectors for each document chunk

3. **Search & Retrieval**

   - Semantic similarity search
   - Returns top-k most relevant documents
   - Supports multiple query types

4. **Visualization**

   - 2D and 3D t-SNE visualizations of the vector space
   - Color-coded by document type
   - Interactive plots using Plotly

5. **User Interface**
   - Gradio web interface for easy interaction
   - Real-time question answering
   - Export capabilities for flagged data

## 📁 Knowledge Base Structure

The system processes documents from four main categories:

- **Company**: General company information, about pages, careers
- **Contracts**: Client contracts and agreements
- **Employees**: HR records and employee information
- **Products**: Product descriptions and specifications

## 🚀 Features

### Document Processing

- Automatic document loading from nested directories
- UTF-8 encoding support with fallback options
- Configurable chunk size (1000 characters) with overlap (200 characters)
- Metadata preservation for document type classification

### Vector Search

- Semantic similarity search using OpenAI embeddings
- Configurable number of results (default: 3)
- Support for various query types

### Visualization

- **2D Visualization**: t-SNE dimensionality reduction for easy viewing
- **3D Visualization**: Enhanced spatial understanding of document relationships
- **Interactive Plots**: Hover information and zoom capabilities
- **Color Coding**: Different colors for each document type

### User Interface

- **Gradio Web Interface**: Easy-to-use web-based Q&A system
- **Real-time Responses**: Instant answers based on knowledge base
- **Export Functionality**: Save flagged questions and answers
- **Shareable Links**: Public access to the interface

## 🛠️ Setup Instructions

### Prerequisites

1. **Python Environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. **Install Dependencies**

   ```bash
   pip install langchain langchain-openai langchain-chroma gradio plotly scikit-learn numpy python-dotenv
   ```

3. **Environment Variables**
   Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

### Knowledge Base Setup

1. Create a `knowledge-base/` directory
2. Organize documents into subdirectories:
   ```
   knowledge-base/
   ├── company/
   ├── contracts/
   ├── employees/
   └── products/
   ```
3. Add markdown files (`.md`) to each subdirectory

## 📊 Usage

### Running the Notebook

1. **Start Jupyter**

   ```bash
   jupyter notebook embeddings.ipynb
   ```

2. **Execute Cells**

   - Run all cells in order
   - The system will automatically process documents and create the vector database

3. **Interactive Features**
   - Test search functionality with sample queries
   - Explore visualizations
   - Launch the Gradio interface

### Using the Web Interface

1. **Launch Interface**

   ```python
   interface.launch(share=True, debug=True)
   ```

2. **Ask Questions**
   - Type questions in the text box
   - Get instant answers based on the knowledge base
   - Export results if needed

### Search Examples

```python
# Search for insurance policies
search_knowledge_base("insurance policies")

# Search for employee benefits
search_knowledge_base("employee benefits")

# Search for health coverage
search_knowledge_base("health coverage")
```

## 🔧 Configuration

### Model Settings

```python
MODEL = "gpt-4o-mini"  # OpenAI model for chat
db_name = "vector_db"   # Vector database directory
```

### Document Processing

```python
chunk_size = 1000       # Characters per chunk
chunk_overlap = 200     # Overlap between chunks
```

### Search Parameters

```python
k = 3                  # Number of results to return
```

## 📈 Visualization Features

### 2D Visualization

- Shows document relationships in 2D space
- Color-coded by document type
- Interactive hover information

### 3D Visualization

- Enhanced spatial understanding
- Rotatable 3D plot
- Better separation of document clusters

## 🔍 Search Capabilities

The system supports various types of queries:

- **Product Information**: "What are the features of Carllm?"
- **Employee Data**: "Tell me about Alex Chen's performance"
- **Contract Details**: "What are the terms of the Apex Reinsurance contract?"
- **Company Information**: "What does Insurellm do?"
