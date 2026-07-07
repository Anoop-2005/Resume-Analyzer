---
title: Resume Analyzer
emoji: 📄
colorFrom: blue
colorTo: indigo
sdk: streamlit
sdk_version: 1.25.0
app_file: finalapp.py
pinned: false
license: GNU
---

# Resume Analyzer

Resume Analyzer is an AI-powered resume analyzer built with **Streamlit**, **LangChain**, **Hugging Face**, and **FAISS**.  
It helps users compare a resume with a job description and generates a structured evaluation including match score, strengths, missing skills, and improvement suggestions.

## Features

- Upload a resume in PDF format.
- Paste any job description.
- Extract text from the resume automatically.
- Split resume text into chunks for retrieval.
- Use Hugging Face embeddings and vector search with FAISS.
- Generate an AI-based analysis of the resume against the job description.
- Display:
  - Match score.
  - Strong points.
  - Missing skills.
  - Improvement suggestions.
  - Final verdict.

## Tech Stack

- **Frontend:** Streamlit
- **PDF Parsing:** pypdf
- **LLM Framework:** LangChain
- **Embeddings:** sentence-transformers
- **Vector Database:** FAISS
- **Model Hosting:** Hugging Face Endpoint
- **Environment Management:** python-dotenv

## Project Structure

```bash
resumefit-ai/
├── finalapp.py
├── requirements.txt
└── README.md
```

## How It Works

1. The user uploads a resume PDF.
2. The app extracts text from the PDF.
3. The resume text is split into smaller chunks.
4. Chunks are converted into embeddings.
5. FAISS stores the embeddings for retrieval.
6. The job description is sent to the model along with relevant resume chunks.
7. The AI returns a structured resume analysis.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Anoop-2005/Resume-Analyzer.git
cd resume-Analyzer-ai
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Hugging Face token

Create a `.streamlit/secrets.toml` file:

```toml
HF_TOKEN = "your_hugging_face_token"
```

## Run Locally

```bash
streamlit run app.py
```

## Deployment on Hugging Face Spaces

This project is ready to be deployed on **Hugging Face Spaces** using Streamlit.  
Make sure your repository contains:

- `finalapp.py`
- `requirements.txt`
- `README.md` with the YAML config block above

Then push the project to Hugging Face Spaces or connect your GitHub repository.

## Usage

1. Open the app.
2. Upload a resume PDF.
3. Paste the job description.
4. Click **Analyze Resume**.
5. View the AI-generated evaluation.

## Example Output

- Match Score: 82/100
- Strong Points: Python, React, APIs
- Missing Skills: Docker, Kubernetes, AWS
- Improvement Suggestions: Add more project impact and deployment experience
- Final Verdict: Good fit with minor improvements

## Limitations

- Works best with text-based PDF resumes.
- Scanned image PDFs may not extract properly.
- Model output can vary depending on the prompt and Hugging Face model used.

## Future Improvements

- Add a cleaner scoring system.
- Export analysis as PDF.
- Add chat history.
- Support DOCX upload.
- Improve prompt formatting for more consistent output.
- Show the match score in a visual chart.

## License

This project is licensed under the GNU License.

## Author

Built by **Anoop** for learning purposes.

This Readme is written by Perplexity 
