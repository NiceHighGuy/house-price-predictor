from ollama import chat

print("Sending request...")

response = chat(
    model="llama3",
    messages=[{"role": "user", "content": "What affects house prices?"}]
)

# Correct way to get the AI reply
print("AI says:\n")
print(response.message.content)
