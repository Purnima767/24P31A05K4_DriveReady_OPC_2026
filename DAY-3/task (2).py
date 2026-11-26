"""
Day 3 – LangChain Prompt Chains, Conversation History, CSV Tests, and Agent

Google Colab setup:
1. Run: !pip install -q langchain langchain-groq
2. Add GROQ_API_KEY to Colab Secrets and enable notebook access.
3. Run this script in Google Colab.
4. Upload test.csv to /content if you want to run the CSV checks.

Do not hard-code or upload your API key to GitHub.
"""

import os
import csv

from google.colab import userdata
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain.agents import create_agent


# Load the Groq API key securely from Colab Secrets.
os.environ["GROQ_API_KEY"] = userdata.get("GROQ_API_KEY")

# Initialize the Groq-hosted language model.
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.3,
)

# Instructions for the Sweet Crumbs Home Bakery assistant.
SYSTEM = """ROLE: You are the friendly assistant for Sweet Crumbs Home Bakery.
FACTS: Plum cake Rs 500. Chocolate cake Rs 650. Cupcake Rs 80 each.
       Orders need 24 hours' notice. All cakes have eggless versions.
RULES: Never promise a delivery time or place. If it isn't in FACTS,
       say "I'll check with the owner." Work out totals carefully.
FORMAT: Under 50 words, friendly, English or Telugu matching the customer."""


# Create a prompt template with a place for previous conversation messages.
prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM),
    MessagesPlaceholder("history"),
    ("human", "{question}"),
])

# Chain: prompt -> language model -> string output.
chain = prompt | llm | StrOutputParser()

# Store previous messages so the assistant can remember the conversation.
history = []


def ask(question: str) -> str:
    """Ask the bakery assistant and preserve the conversation history."""
    answer = chain.invoke({
        "history": history,
        "question": question,
    })
    history.extend([
        ("human", question),
        ("ai", answer),
    ])
    return answer


# Example conversation: the assistant should remember the customer's name.
if __name__ == "__main__":
    print(ask("Hi, I'm Ravi. Do you make eggless cakes?"))
    print(ask("What's my name?"))


def run_tests(path: str = "/content/test.csv") -> None:
    """Check whether each answer includes the expected text from a CSV file."""
    with open(path, newline="", encoding="utf-8") as csv_file:
        rows = list(csv.DictReader(csv_file))

    passed = 0
    for row in rows:
        answer = chain.invoke({
            "history": [],
            "question": row["question"],
        })
        ok = row["must_include"].lower() in answer.lower()
        passed += int(ok)
        print(
            "PASS" if ok else "FAIL",
            "|",
            row["question"],
            "->",
            answer[:70],
        )

    percentage = passed / len(rows) if rows else 0
    print(f"\n{passed}/{len(rows)} passed ({percentage:.0%})")


# Example LangChain agent.
# The original notebook had mismatched variable names in this cell.
# These names are made consistent here so the example can run.
agent_order = create_agent(
    model=llm,
    tools=[],
    system_prompt=SYSTEM,
)

result_order = agent_order.invoke({
    "messages": [
        {"role": "user", "content": "Do you make eggless cakes?"}
    ]
})
print(result_order["messages"][-1].content)

# To run the CSV checks after uploading /content/test.csv, uncomment:
# run_tests()
