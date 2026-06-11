# import os
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq
# from langchain_community.tools.tavily_search import TavilySearchResults
# from langgraph.prebuilt import create_react_agent


# # Load variables from .env
# load_dotenv()

# # Check if the API key exists
# api_key = os.getenv("GROQ_API_KEY")
# tavily_key=os.getenv("TAVILY_API_KEY")
# if not api_key or not tavily_key:
#     print("Error: ensure both GROQ_API_KEY and tavily are in .env file!")
# else:
#     # Initialize the LLM
#     llm = ChatGroq(model="llama-3.3-70b-versatile",
#                    api_key=api_key,
#                    temperature=0.7)
#     search_tool = TavilySearchResults(max_results=2)
#     tools = [search_tool]

#     agent = create_react_agent(llm, tools)

#     query = "who won the ipl 2016 final in india"

#     print(f"Asking agent:{query}....\n")
#     # Simple test call
#     # response = llm.invoke("Hello! Can you hear me?")
#     # print("Agent Response:", response.content)
#     response = agent.invoke({"messages":[("user",query)]})
#     print("Agent Response:", response["messages"][-1].content)
    

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain.agents import create_agent

# Load variables
load_dotenv()

# Initialize components
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)
search_tool = TavilySearchResults(max_results=2)
tools = [search_tool]

# Create the agent
# Ensure your langgraph version supports this signature
agent = create_react_agent(llm, tools)

query = "what is the score of ipl 2016 final"

# Corrected invocation using "messages"
response = agent.invoke({"messages": [("user", query)]})

# Accessing the final output
print("Agent Response:", response["messages"][-1].content)