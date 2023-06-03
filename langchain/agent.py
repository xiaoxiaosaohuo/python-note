from langchain.python import PythonREPL
from langchain.tools.python.tool import PythonREPLTool
from langchain.agents import AgentType
from langchain.agents import load_tools, initialize_agent
from langchain.agents.agent_toolkits import create_python_agent
import warnings
import os
import langchain
langchain.debug = True


from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())  # read local .env file

warnings.filterwarnings("ignore")

from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI(temperature=0)
tools = load_tools(["llm-math","wikipedia"], llm=llm)

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True,
    verbose=True)

question = "Tom M. Mitchell is an American computer scientist \
and the Founders University Professor at Carnegie Mellon University (CMU)\
what book did he write?"
# result = agent(question)

# print(result)


# Python Agent


agent = create_python_agent(
    llm,
    tool=PythonREPLTool(),
    verbose=True
)
customer_list = [["Harrison", "Chase"],
                 ["Lang", "Chain"],
                 ["Dolly", "Too"],
                 ["Elle", "Elem"],
                 ["Geoff", "Fusion"],
                 ["Trance", "Former"],
                 ["Jen", "Ayai"]
                 ]
agent.run(f"""Sort these customers by \
last name and then first name \
and print the output: {customer_list}""")
