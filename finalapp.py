import streamlit as st
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFaceEndpoint, ChatHuggingFace
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_classic.chains import RetrievalQA


st.set_page_config(page_title="Resume Analyzer with AI", page_icon="📄", layout="wide")


st.title("Resume Analyzer with AI")
st.write("Upload a resume and compare it with a job description.")
st.text("Analyze the Resume of any candidate to know if it fit or not")

@st.cache_resource
def load_models():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    llm_endpoint = HuggingFaceEndpoint(
        repo_id="Qwen/Qwen2.5-7B-Instruct",
        task="text-generation",
        temperature=0.3,
        max_new_tokens=1024,
        huggingfacehub_api_token=st.secrets.get("HF_TOKEN", "")
    )
    
    # 2. Wrap it inside ChatHuggingFace to format payloads correctly for conversational models
    llm = ChatHuggingFace(llm=llm_endpoint)

    return embeddings, llm

def extract_pdf_text(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def build_vectorstore(text, embeddings):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_text(text)
    if not chunks:
        return None
    return FAISS.from_texts(chunks, embedding=embeddings)

resume_file = st.file_uploader("Upload Resume PDF", type=["pdf"])
job_description = st.text_area("Paste Job Description here", height=250)

if resume_file and job_description:
    embeddings, llm = load_models()
    

    if st.button("Analyze Resume"):
        with st.spinner("Analyzing..."):
            resume_text = extract_pdf_text(resume_file)
            if not resume_text.strip():
                st.error("No text could be extracted from this PDF. It might be a scanned image.")
                st.stop()

            vectorstore = build_vectorstore(resume_text, embeddings)
            if vectorstore is None:
                st.error("❌ Failed to process text chunks.")
                st.stop()

            retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

            qa = RetrievalQA.from_chain_type(
                llm=llm,
                chain_type="stuff",
                retriever=retriever
            )

            prompt = f"""
            Compare this resume with the job description.

            Job Description:
            {job_description}

            Give output in this format:
            1. Match Score out of 100
            2. Strong Points
            3. Missing Skills
            4. Improvement Suggestions
            5. Final Verdict
            """

            try:
                result = qa.invoke({"query": prompt})
                st.subheader("Analysis Result")
                st.write(result["result"])
            except Exception as e:
                st.error(f"An error occurred during generation: {e}")

else:
    st.info("Please upload a resume PDF and paste a job description to begin.")