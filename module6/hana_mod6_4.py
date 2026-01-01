from langchain_ollama import ChatOllama
from langchain.tools import tool
from langchain.agents import create_agent
from langchain.messages import HumanMessage


# --------------------
# Simple calculator tool
# --------------------
@tool
def calculator(expression: str) -> str:
    """Solve basic math like: 2+3, 5*6, 10/2"""
    try:
        return str(eval(expression))
    except:
        return "Invalid math expression"


# --------------------
# Load LLM
# --------------------
llm = ChatOllama(
    model="llama3.1",
    temperature=0
)

# --------------------
# Create agent
# --------------------
agent = create_agent(
    model=llm,
    tools=[calculator],
    system_prompt="You are a math assistant. Use the calculator tool for calculations."
)

# --------------------
# Chat loop
# --------------------
while True:
    question = input("\nAsk a math question (or type exit): ")
    if question.lower() == "exit":
        break

    result = agent.invoke({
        "messages": [HumanMessage(content=question)]
    })

    print("Answer:", result["messages"][-1].content)

    #The code creates a LangChain agent using a local Ollama LLM that answers math questions by calling a calculator tool when calculations are needed.
