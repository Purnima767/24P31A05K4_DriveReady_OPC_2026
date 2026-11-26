Day 3 – LangChain Prompt Chains, Conversation History, and Testing
Overview
This task builds on the Sweet Crumbs Home Bakery assistant using LangChain. It creates a chat prompt template, preserves conversation history, runs simple CSV-based response checks, and introduces LangChain's agent creation API.
Concepts covered
- Installing langchain and langchain-groq
- Connecting ChatGroq to a Groq-hosted model using a Colab Secret
- Creating a prompt with ChatPromptTemplate
- Adding previous messages with MessagesPlaceholder
- Converting model output to text with StrOutputParser
- Building a chain using prompt | llm | parser
- Preserving conversation history between questions
- Running simple response checks from a CSV file
- Creating an introductory LangChain agent with create_agent
Requirements
- Google Colab
- A Groq API key stored in Colab Secrets as GROQ_API_KEY
- A test.csv file uploaded to /content/test.csv if you want to run the CSV test function
Setup in Google Colab
1. Open your Day 3 notebook or create a new Colab notebook.
2. Run this installation command:
   !pip install -q langchain langchain-groq
3. Open Secrets using the key icon in the left sidebar.
4. Add a secret named GROQ_API_KEY and paste your Groq API key as its value.
5. Enable notebook access for this secret.
6. Upload task.py to Colab or paste its contents into a code cell, then run it.
Example CSV format
The CSV test function expects these exact column headings:
question,must_include
How much is a plum cake?,500
Do you deliver to Kakinada?,I'll check with the owner
Upload the file to the Colab session at /content/test.csv before running:
run_tests()
The test checks whether the assistant's answer contains the expected must_include text. A failed check means the expected text was not found; it does not necessarily mean the model call failed.
Agent example
The task introduces create_agent with an empty tools list. It is an introductory agent example and does not yet use external tools.

The original notebook's final agent cell used inconsistent variable names (agent_order versus agent, and result_order versus result). In task.py, these names are made consistent so the example can run.
Important notes
- The model used is openai/gpt-oss-120b; availability depends on Groq.
- The CSV test expects a file at /content/test.csv.
- Keep your API key private. Never hard-code it or commit it, Colab Secrets, or .env files to GitHub.
