'''
Nick DeMaestri
12/12/2024
CS-391

Palindrome Detector

Based off code provided from https://github.com/gnolankettering/lecture17/blob/main/app1.py
'''

from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from langchain_openai import ChatOpenAI
from langchain.tools import Tool
import config

# 1. Create the model
model = ChatOpenAI(openai_api_key=config.OPENAI_API_KEY) ## USE OWN OPENAI API KEY HERE ----------------------------------

# 2. Create the tools
def check_if_palindrome(str): ## Simple palindrome checker by comparing a string to its reversal
    return str == str[::-1]

tools = [
    Tool.from_function(
        func=check_if_palindrome,
        name="Check if the word is a palindrome",
        description="Check if the word in the string is a palindrome or not",
    )
]

# 3. Get the prompt to use
prompt = hub.pull("hwchase17/react",api_key=config.LANGSMITH_API_KEY) ## USE OWN LANGSMITH API KEY HERE ----------------------------------

# 4. Construct the ReAct agent
agent = create_react_agent(model, tools, prompt)

# 5. Create an agent executor by passing in the agent and tools
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 6. Invoke the agent executor
agent_executor.invoke({"input": 'Is the word "racecar" a palindrome?'})