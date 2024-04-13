import os
from langchain_community.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"

def query_with_doc(doc_path, query):
    text_loader = TextLoader(doc_path, encoding='utf-8')
    index = VectorstoreIndexCreator().from_loaders([text_loader])
    result = index.query_with_sources(query)
    return result["answer"]

# Example
doc_path = "DOC_FILE_PATH"
query = "QUESTION"
query_with_doc(doc_path, query)
