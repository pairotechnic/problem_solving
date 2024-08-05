'''
    Purpose : Query a PDF
    Author : Rohit Pai
    Date : 5th August 2024
'''

# Standard Library Import
import os

# Third Party Import
from PyPDF2 import PdfReader

from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAI, OpenAIEmbeddings

# Local Application Import
from credentials import OPENAI_API_KEY, pdf_path, question



# Set the OpenAI API Key
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Initialize a PdfReader object for the specified PDF file path.
pdfreader = PdfReader(pdf_path)

# Read the pdf and extract text
raw_text = ''
for i, page in enumerate(pdfreader.pages):
    content = page.extract_text()
    if content : 
        raw_text += content

# The extracted text is split into chunks
text_splitter = CharacterTextSplitter(
    separator = "\n",
    chunk_size = 800,
    chunk_overlap = 200,
    length_function = len,
)
texts = text_splitter.split_text(raw_text)

# Download embeddings from OpenAI
embeddings = OpenAIEmbeddings()

# Create a FAISS vector store from the text chunks and their corresponding embeddings
# This allows for efficient similarity search
document_search = FAISS.from_texts(texts, embeddings)

# Load the question answering chain
chain = load_qa_chain(OpenAI(), chain_type="stuff")

# Find chunks of text similar to the query
query = question
docs = document_search.similarity_search(query)

# Invoke the question-answering chain with the relevant documents and the query to generate an answer
output = chain.invoke({"input_documents":docs, "question":query})

print("Question : ", output["question"])
print("Answer : ", output["output_text"])