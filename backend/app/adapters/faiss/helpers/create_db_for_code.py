from typing import List
import asyncio
import json
import numpy as np
from transformers import AutoTokenizer, AutoModel
from langchain.text_splitter import RecursiveCharacterTextSplitter, Language
from langchain.vectorstores import FAISS
from langchain.docstore.in_memory import InMemoryDocstore
from langchain.schema import Document
import torch
import os
import faiss

class FAISS_File_Search:
    def __init__(self, faiss_manager: FAISS_File_Manager = FAISS_File_Manager()):
        self.FAISS_MANAGER = faiss_manager
        
    def similary_search(self, query: str, k=10):
        FAISS_Manager.similarity_search(query=query, k=k)

class FAISS_File_Manager:
    
    async def similarity_search(self, query: str, k: int):
        query_embedding = await self.__embedding_fn(query)
        try:
            results = await self.faiss_store.similarity_search_by_vector(query_embedding, k)
            return results
        except Exception as e:
            print(f"Error during similarity search: {e}")
            return []
    
    def save_index(self):
        try:
            self.faiss_store.save_local(self.index_path)
            print("FAISS index successfully saved!")
        except Exception as e:
            print(f"Failed to save FAISS index: {e}")
    
    def __init__(self, model_name="microsoft/codebert-base", index_path="backend/db/faiss_index"):
        os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
        os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
        self.index_path = index_path
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)
        self.faiss_index = faiss.IndexFlatL2(768)
        self.faiss_store = FAISS(
            embedding_function=self.__embedding_fn,
            index=self.faiss_index,
            docstore=InMemoryDocstore({}),
            index_to_docstore_id={}
        )
        self.__load_index()

    def __embedding_fn(self, text: str) -> np.ndarray:
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
        return outputs.last_hidden_state[:, 0, :].squeeze().numpy()

    def __load_index(self):
        try:
            self.faiss_store = FAISS.load_local(
                self.index_path, 
                self.__embedding_fn, 
                allow_dangerous_deserialization=True
            )
        except Exception as e:
            print(f"Failed to load FAISS index: {e}")

    def __add_documents_from_json(self, json_data, path=""):
        python_splitter = RecursiveCharacterTextSplitter.from_language(
            language=Language.PYTHON,
            chunk_size=2000,
            chunk_overlap=200
        )

        for key, value in json_data.items():
            current_path = f"{path}/{key}" if path else key
            if isinstance(value, dict):
                self.__add_documents_from_json(value, current_path)
            elif isinstance(value, str):
                if current_path.endswith('.py'):
                    print(f"Processing file: {current_path}")
                    print(f"File content: {value}\n")

                    documents = [Document(page_content=value)]
                    chunks = python_splitter.split_documents(documents)
                    print(f"Split into {len(chunks)} chunks.")
                    
                    for chunk in chunks:
                        new_embedding = self.__embedding_fn(chunk.page_content)
                        if not self.__is_duplicate(new_embedding):
                            self.faiss_store.add_texts(
                                texts=[chunk.page_content],
                                embeddings=[new_embedding],
                                metadatas=[{"path": current_path}]
                            )

    def __is_duplicate(self, new_embedding, threshold=0.9):
        if self.faiss_store.index.ntotal == 0:
            return False
        distances, _ = self.faiss_store.index.search(np.array([new_embedding]), 1)
        similarity_threshold = 1 - threshold
        return distances[0][0] < similarity_threshold

# TODO: delete this
# async def test_faiss():
#     os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
#     os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
    
#     faiss_manager = FAISSManager()
#     faiss_manager.load_index()

#     query = """
#     print("Hello, world!")
#     print("Hello, world!")
#     print("Hello, world!")
#     print("Hello, world!")
#     print("Hello, world!")
#     """
   
#     results = await faiss_manager.similarity_search(query)

#     if results:
#         top_results = results[:8]
#         combined_content = "\n\n".join(
#             [result.page_content for result in top_results]
#         )  
#         return combined_content
#     else:
#         return "No results found."

# def main():
#     json_files = {
#         "anubis": "data/data_jsons/Anunbis-develop.json",
#         "backend_master": "data/data_jsons/backend-master.json",
#         "donna_backend_master": "data/data_jsons/donna-backend-master.json",
#         "final_year": "data/data_jsons/final-year-project-backend-api-master.json",
#         "flask_postgres": "data/data_jsons/Flask-PostgreSQL-API-Seed-master.json",
#         "flask_api": "data/data_jsons/FlaskApiEcommerce-master.json",
#         "gramps_api": "data/data_jsons/gramps-web-api-master.json",
#         "hacker_api": "data/data_jsons/hackernews-api-main.json",
#         "http_api": "data/data_jsons/http-api.json",
#         "launcher_api": "data/data_jsons/luncher-api-master.json",
#         "ml_flask_api": "data/data_jsons/ml-flask-api-master.json",
#         "rest_api": "data/data_jsons/RESTfulAPI-master 2.json",
#     }

#     os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
#     os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

#     faiss_manager = FAISSManager()
#     lol = asyncio.run(test_faiss())
#     print(lol)

# if __name__ == "__main__":
#     print("Тесты - ")
#     main()

