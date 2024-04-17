import os
from langchain_community.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"

def vectorization(doc_path):
    text_loader = TextLoader(doc_path, encoding='utf-8')
    index = VectorstoreIndexCreator().from_loaders([text_loader])
    return index

def query_with_doc(index, query)
    result = index.query_with_sources(query)
    return result["answer"]

# Usage
doc_path = "DOC_FILE_PATH"
query = "QUESTION"
index = vectorization(doc_path)
print(query_with_doc(index, query))
