from langchain.text_splitter import CharacterTextSplitter
import os
from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import DeepLake
os.environ['OPENAI_API_KEY'] = 'YOUR KEY HERE'
os.environ['ACTIVELOOP_TOKEN'] = 'YOUR KEY HERE'
embeddings = OpenAIEmbeddings(disallowed_special=())

root_dir = './the-algorithm'
docs = []
for dirpath, dirnames, filenames in os.walk(root_dir):
    for file in filenames:
        try:
            loader = TextLoader(os.path.join(dirpath, file), encoding='utf-8')
            docs.extend(loader.load_and_split())
        except Exception as e:
            pass

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(docs)
username = "mikelabs"  # replace with your username from app.activeloop.ai
# dataset would be publicly available
db = DeepLake(dataset_path=f"hub://{username}/twitter-algorithm",
              embedding_function=embeddings, public=True)
db.add_documents(texts)
print("done")

# Utilizing dolly-v2-12b to Process and Understand User Queries
