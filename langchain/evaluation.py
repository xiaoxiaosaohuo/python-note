from langchain.indexes import VectorstoreIndexCreator
from langchain.document_loaders import CSVLoader
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
import os
from langchain.evaluation.qa import QAGenerateChain

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())


from langchain.vectorstores import DocArrayInMemorySearch


file = 'OutdoorClothingCatalog_1000.csv'
loader = CSVLoader(file_path=file)
data = loader.load()


index = VectorstoreIndexCreator(
    vectorstore_cls=DocArrayInMemorySearch
).from_loaders([loader])

llm = ChatOpenAI(temperature=0.0)
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=index.vectorstore.as_retriever(),
    verbose=True,
    chain_type_kwargs={
        "document_separator": "<<<<>>>>>"
    }
)
example_gen_chain = QAGenerateChain.from_llm(ChatOpenAI())
new_examples = example_gen_chain.apply_and_parse(
    [{"doc": t} for t in data[:5]]
)
examples = [
    {
        "query": "Do the Cozy Comfort Pullover Set\
        have side pockets?",
        "answer": "Yes"
    },
    {
        "query": "What collection is the Ultra-Lofty \
        850 Stretch Down Hooded Jacket from?",
        "answer": "The DownTek collection"
    }
]
examples += new_examples
qa.run(examples[0]["query"])
