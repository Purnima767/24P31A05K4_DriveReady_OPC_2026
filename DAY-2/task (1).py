"""
Day 2 – Groq API, Python Data Handling, and Chatbot Memory

Google Colab setup:
1. Run: !pip install -q openai
2. Add GROQ_API_KEY in Google Colab Secrets.
3. Enable notebook access to the secret.
4. Run this script.

Never hard-code or upload your API key to GitHub.
"""

import json
import functools

from google.colab import userdata
from openai import OpenAI, RateLimitError, APIConnectionError


# Connect to Groq using its OpenAI-compatible API.
client = OpenAI(
    api_key=userdata.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

MODEL = "openai/gpt-oss-120b"

# Bakery menu: item name -> price in rupees.
MENU = {
    "plum cake": 500,
    "chocolate cake": 650,
    "cupcake": 80,
}

# Example: safely look up a menu item.
print("Cupcake price:", MENU.get("cupcake", "Item not available"))
print("Donut lookup:", MENU.get("donut", "Donuts not available"))

# Example customer order stored as a dictionary.
order = {
    "name": "Ravi",
    "item": "plum cake",
    "qty": 2,
    "eggless": True,
}
total = order["qty"] * MENU[order["item"]]
print("Order total: ₹", total)

# Convert the order dictionary to JSON and back.
order_json = json.dumps(order)
order_again = json.loads(order_json)
print("Order as JSON:", order_json)
print("JSON converted back to dictionary:", order_again)


def get_price(item: str, qty: int = 1) -> int:
    """Return the total price for an item on the bakery menu."""
    return MENU[item.lower().strip()] * qty


# A decorator that logs a function call and its result.
def log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[log] {func.__name__}{args} -> {result!r}")
        return result

    return wrapper


@log_call
def logged_get_price(item: str, qty: int = 1) -> int:
    return get_price(item, qty)


print("Six cupcakes cost: ₹", logged_get_price("cupcake", 6))


# Example of handling an error with try/except.
try:
    print("Unknown item price:", get_price("donut"))
except KeyError:
    print("Sorry, that item is not available on our menu.")


# System prompt: facts and rules for the bakery assistant.
SYSTEM = f"""ROLE: You are the friendly assistant for Sweet Crumbs Home Bakery.
FACTS: Menu with prices in rupees: {json.dumps(MENU)}
Orders need 24 hours' notice. All cakes have eggless versions.
RULES: Never promise a delivery time. If it isn't in FACTS, say
"I'll check with the owner." Remember the customer's name and order.
FORMAT: Under 50 words, friendly, and reply in English or Telugu
to match the customer."""

# Keep the system instructions and recent conversation messages.
history = [{"role": "system", "content": SYSTEM}]
MAX_TURNS = 8


def chat(user_text: str) -> str:
    """Send a message to Groq while keeping recent conversation history."""
    history.append({"role": "user", "content": user_text})

    # Keep the system message plus the most recent conversation messages.
    recent_messages = [history[0]] + history[1:][-MAX_TURNS:]

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=recent_messages,
            temperature=0.3,
        )
        reply = response.choices[0].message.content or ""
    except RateLimitError:
        reply = "We're a little busy. Please try again in a minute."
    except APIConnectionError:
        reply = "I can't reach the server right now. Please try again shortly."

    history.append({"role": "assistant", "content": reply})
    return reply


# Interactive chatbot loop. Type bye, exit, or quit to stop.
if __name__ == "__main__":
    print("\nWelcome to Sweet Crumbs Home Bakery!")
    while True:
        user_text = input("You: ").strip()

        if user_text.lower() in ("bye", "exit", "quit"):
            print("Bot: Thank you for visiting Sweet Crumbs!")
            break

        if not user_text:
            continue

        print("Bot:", chat(user_text))
