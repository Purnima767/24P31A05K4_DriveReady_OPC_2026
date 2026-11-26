# Day 2 – Groq API, Python Data Handling, and Chatbot Memory

## Overview
This task develops the **Sweet Crumbs Home Bakery** assistant using Groq's OpenAI-compatible API and Python. It also demonstrates Python data handling and how a chatbot can keep recent conversation history.

## Concepts covered
- Connecting to Groq using the `openai` Python package
- Sending system and user messages to a chat-completion model
- Creating a system prompt with bakery facts, prices, and response rules
- Storing menu items and customer orders in Python dictionaries
- Looking up values safely with `dict.get()`
- Converting dictionaries to JSON and back using `json.dumps()` and `json.loads()`
- Writing functions with parameters, type hints, and default values
- Handling errors with `try` / `except`
- Using a decorator to log function calls
- Maintaining chat history and limiting recent conversation context
- Handling API rate-limit and connection errors

## Requirements
- Google Colab
- A Groq API key saved in Colab Secrets as `GROQ_API_KEY`
- Python package: `openai`

## Setup in Google Colab
1. Open your Day 2 notebook in Google Colab.
2. Run this installation command in a code cell:

   ```python
   !pip install -q openai
   ```

3. Open **Secrets** using the key icon in the left sidebar.
4. Add a secret named `GROQ_API_KEY` and paste your Groq API key as its value.
5. Enable notebook access for this secret.
6. Upload `task.py` to Colab or paste its contents into a code cell, then run it.
7. Chat with the bakery assistant. Type `bye`, `exit`, or `quit` to stop.

## Bakery menu used in the task

| Item | Price |
|---|---:|
| Plum cake | ₹500 |
| Chocolate cake | ₹650 |
| Cupcake | ₹80 |

All cakes have eggless versions. Orders need 24 hours' notice.

## Example
A customer can ask:
- `What is the price of a cupcake?`
- `Do you have eggless cakes?`
- `Can I order a plum cake?`

The assistant should use the menu facts, remember recent messages during the chat, and avoid promising a delivery time.

## Files
- `task.py` – Day 2 Python code.

## Important notes
- The notebook uses Groq's OpenAI-compatible base URL: `https://api.groq.com/openai/v1`.
- The model used is `openai/gpt-oss-120b`; check Groq if the model is unavailable to your account.
- Never hard-code your API key or upload your API key, Colab Secrets, or `.env` file to GitHub.
- Some notebook cells demonstrate errors intentionally as part of learning exception handling.
