from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.llms.openai import OpenAI
# from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores.chroma import Chroma
from langchain.chains.summarize import load_summarize_chain
# from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_community.embeddings.openai import OpenAIEmbeddings
# from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.document_loaders.pdf import PyPDFLoader
from dotenv import load_dotenv
import os
from tempfile import NamedTemporaryFile
from Application.TextExtraction import extract_text

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
llm = OpenAI(temperature=0.9)

def get_chunks(text):
    splitter = RecursiveCharacterTextSplitter()
    chunks = splitter.split(text)
    return chunks

def get_docs(file_upload):
    # import pdb 
    # pdb.set_trace()
    temp_file = NamedTemporaryFile(delete=False)
    temp_file.write(file_upload.read())
    temp_file.close()

    uploaded_file = temp_file.name
    raw_text_content = extract_text(uploaded_file)

    if raw_text_content is None:
        # print("Error: Extracted text is None.")
        raise ValueError("Failed to extract text from the uploaded file.")
    else:
        print(f"Extracted text length: {len(raw_text_content)}")

    if len(raw_text_content) <= 12000:
        return raw_text_content, 'text'
    else:
        loader = PyPDFLoader(uploaded_file)
        documents = loader.load()
        docs = get_chunks(documents)
        return docs, 'chunks'

def get_summaryprompt(uploaded_file):
    docs, return_type = get_docs(uploaded_file)
    if return_type == 'text':
        summary = docs
    else:
        # embedding = SentenceTransformerEmbeddings(model_name='all-MiniLM-L6-v2')
        embedding = OpenAIEmbeddings()
        db = Chroma.from_documents(docs, embedding)
        query = 'find introduction, requirements, functional requirements, non-functional requirements or any important section in the document that will help in writing test cases'
        docs = db.similarity_search(query)
        chain = load_summarize_chain(llm, chain_type='stuff')
        summary = chain.run(docs)
    return summary

# def generate_test_cases(prompt):
#     prompt = PromptTemplate(input_variables=['text'], template='You are a software engineer, business analyst, ai developer, data analyst at a tech company and an expert at writing test cases. You are tasked with writing atleast 10 test cases for the following requirements or summary: \n\n{text}')
#     res = prompt.format(text=prompt)
#     result = llm(res,max_tokens=3900)
#     return result

def generate_test_cases(prompt):
    a = "hello this is sim"
    return a

