from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
import warnings
import os
from langchain.memory import ConversationBufferWindowMemory
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())  # read local .env file

warnings.filterwarnings('ignore')

llm =ChatOpenAI(temperature=0.0)


# ConversationBufferMemory
# memory = ConversationBufferMemory()
# conversation = ConversationChain(
#     llm=llm,
#     memory=memory,
#     verbose=True
# )
# conversation.predict(input='hi,my name is siven')

# conversation.predict(input="What is 1+1?")
# conversation.predict(input="What is my name?")

# print(memory.buffer)


# memory.save_context({"input": "Hi"},
#                     {"output": "What's up"})
# memory.load_memory_variables({})

# ConversationBufferWindowMemory just keep a memory window
memory = ConversationBufferWindowMemory(k=1)
memory.save_context({"input": "Hi"},
                    {"output": "What's up"})  # this one is dropped
memory.save_context({"input": "Not much, just hanging"},
                    {"output": "Cool"}) 
memory.load_memory_variables({})

# ConversationTokenBufferMemory

# ConversationSummaryMemory， summary the history

schedule = "There is a meeting at 8am with your product team. \
You will need your powerpoint presentation prepared. \
9am-12pm have time to work on your LangChain \
project which will go quickly because Langchain is such a powerful tool. \
At Noon, lunch at the italian resturant with a customer who is driving \
from over an hour away to meet you to understand the latest in AI. \
Be sure to bring your laptop to show the latest LLM demo."

memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=100)
memory.save_context({"input": "Hello"}, {"output": "What's up"})
memory.save_context({"input": "Not much, just hanging"},
                    {"output": "Cool"})
memory.save_context({"input": "What is on the schedule today?"},
                    {"output": f"{schedule}"})
