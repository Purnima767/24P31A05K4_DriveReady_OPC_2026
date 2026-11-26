# Day 1 – Introduction to LLMs with Groq and LangChain

## Overview
This task creates a simple AI assistant for **Sweet Crumbs Home Bakery** using a Groq-hosted language model and LangChain. It also includes the Prompt Guard model example from the Day 1 notebook.

## Concepts covered
- Installing and importing `langchain-groq` and `groq`
- Connecting to a Groq-hosted model with `ChatGroq`
- Reading an API key securely from Google Colab Secrets
- Writing a system prompt that defines the assistant's role, facts, rules, and response format
- Sending user questions to the model using an `ask()` function
- Calling the Groq Prompt Guard model with an example prompt

## Requirements
- Google Colab
- A Groq API key
- Python packages: `langchain-groq` and `groq`

## Setup in Google Colab

1. Open your Day 1 notebook in Google Colab.
2. Run this installation command in a Colab code cell:

   ```python
   !pip install -q langchain-groq groq
   ```

3. Open **Secrets** using the key icon in the left sidebar.
4. Add a secret named `GROQ_API_KEY` and paste your Groq API key as its value.
5. Enable notebook access for this secret.
6. Upload `task.py` to Colab or paste its contents into a code cell, then run it.

## Example

The assistant is given these bakery facts:
- Orders are made to order.
- Orders need 24 hours' notice.
- Cakes have eggless versions.

Example question:

```python
ask("Can I get my order tomorrow?")
```

The assistant should answer politely and must not promise a delivery time.

## Files

- `task.py` – Day 1 Python code.

## Important notes
- Never hard-code your API key in the source code.
- Never upload your API key, Colab Secrets, or `.env` file to GitHub.
- The model names used in this notebook must be available to your Groq account. If a model is unavailable, check the current model names in Groq.
- The Prompt Guard section demonstrates a model call; it is not a complete production safety system.
