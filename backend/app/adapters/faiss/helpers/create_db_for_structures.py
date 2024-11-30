from backend.db.get_jsonstr import GetDataBase
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from typing import List
from langchain.docstore.in_memory import InMemoryDocstore
from langchain.vectorstores import FAISS


class FAISS_Structure_Search:
    def __init__(self):
        self.manager = FAISS_Structure_Manager()
        
    async def similary_search(self, query: str, k=10):
        return self.manager.similarity_search(query=query, k=k)

class FAISS_Structure_Manager:

    def similarity_search(self, query: str, k: int = 5) -> List[str]:
        query_embedding = self.__embedding_fn(query)
        results = self.faiss_store.similarity_search_by_vector(query_embedding, k)
        return [result.page_content for result in results]
        
    def save_index(self):
        try:
            self.faiss_store.save_local(self.index_path)
            print("FAISS index successfully saved!")
        except Exception as e:
            print(f"Failed to save FAISS index: {e}")
    
    def __init__(self, model_name: str = 'sentence-transformers/all-MiniLM-L6-v2', index_path: str = "backend/db/faiss_index_for_text"):
        self.index_path = index_path
        self.model = SentenceTransformer(model_name)
        self.faiss_index = faiss.IndexFlatL2(384)  
        self.faiss_store = FAISS(
            embedding_function=self.__embedding_fn,
            index=self.faiss_index,
            docstore=InMemoryDocstore({}),
            index_to_docstore_id={}
        )
        self.__load_index()

    def __embedding_fn(self, text: str) -> np.ndarray:
        return self.model.encode([text], convert_to_numpy=True).squeeze()

    def __load_index(self):
        try:
            self.faiss_store = FAISS.load_local(self.index_path, self.__embedding_fn, allow_dangerous_deserialization=True)
        except Exception as e:
            print(f"Failed to load FAISS index: {e}")

    def __add_texts(self, texts: List[str]):
        embeddings = [self.__embedding_fn(text) for text in texts]
        metadatas = [{"id": i} for i, _ in enumerate(texts)]
        self.faiss_store.add_texts(texts=texts, embeddings=embeddings, metadatas=metadatas)
        print(f"Added {len(texts)} texts to the FAISS store.")

# TODO: delete this
# def main():
  
#     faiss_manager = FAISSManager_structure()
#     faiss_manager.load_index()
#     query = "'FlaskApiEcommerce-master': {'.gitignore': '', '.idea': {'.gitignore': '', 'F"
#     results = faiss_manager.search(query, k=1)
#     output = "\n".join(results)
#     print(output)

    

# if __name__ == "__main__":
#     main()
