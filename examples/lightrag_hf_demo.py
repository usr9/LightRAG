import os
import sys

from lightrag import LightRAG, QueryParam
from lightrag.llm import hf_model_complete, hf_embedding
from transformers import AutoModel,AutoTokenizer

WORKING_DIR = "./dickens"

if not os.path.exists(WORKING_DIR):
    os.mkdir(WORKING_DIR)

rag = LightRAG(
    working_dir=WORKING_DIR,
    llm_model_func=hf_model_complete,  
    llm_model_name='meta-llama/Llama-3.1-8B-Instruct',
    embedding_func=hf_embedding,  
    tokenizer=AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2"),
    embed_model=AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
)


with open("./book.txt") as f:
    rag.insert(f.read())

# Perform naive search
print(rag.query("What are the top themes in this story?", param=QueryParam(mode="naive")))

# Perform local search
print(rag.query("What are the top themes in this story?", param=QueryParam(mode="local")))

# Perform global search
print(rag.query("What are the top themes in this story?", param=QueryParam(mode="global")))

# Perform hybrid search
print(rag.query("What are the top themes in this story?", param=QueryParam(mode="hybrid")))