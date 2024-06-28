import uuid

from chromadb import QueryResult
from chromadb.db.base import UniqueConstraintError

from vector_cache.vector_stores.base import VectorStoreInterface
import chromadb
from typing import Union, Callable, Tuple
from vector_cache.utils.key_util import get_query_index
class ChromaDB(VectorStoreInterface):

    default_collection = 'default_collection'

    def __init__(self, collection: str = default_collection, persistent = False, identifier: Union[str, Callable, None] = None) -> None:
        if persistent:
            self.chroma_client = chromadb.PersistentClient()
        else:
            self.chroma_client = chromadb.Client()
        self.identifier = identifier
        try:
            self.collection = self.chroma_client.create_collection(name=collection)
        except UniqueConstraintError:
            print(f"Collection {collection} already exists")
            self.collection = self.chroma_client.get_collection(name=collection)

    def add(self, embedding: list, **kwargs) -> str:
        vector_id = get_query_index(self.identifier)
        # chroma db client expects the embeddings themselves to be a list.
        # So, we convert it to such but only if it's not already a list
        if isinstance(embedding, list):
            self.collection.add(ids=[vector_id], embeddings=[embedding])
        else:
            embedding_list = embedding.tolist()
            self.collection.add(ids=[vector_id], embeddings=[embedding_list])
        return vector_id

    def get(self, id: str) -> Tuple[str, float]:
        pass

    def search(self, embedding: list, top_k: int, include_distances:bool = True, **kwargs) -> Tuple[list, list]:
        # chroma db client expects the embeddings themselves to be a list.
        # So, we convert it to such but only if it's not already a list

        if isinstance(embedding, list):
            embedding_list = embedding
        else:
            embedding_list = embedding.tolist()

        if include_distances:
            query_result: QueryResult = self.collection.query(query_embeddings=[embedding_list], n_results=top_k, include=["distances"])
            return query_result['ids'][0], query_result['distances'][0]
        else:
            query_result: QueryResult = self.collection.query(query_embeddings=[embedding_list], n_results=top_k, include=["distances"])
            return query_result['ids'][0]


    def __enter__(self) -> "ChromaDB":
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.close()