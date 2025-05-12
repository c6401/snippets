import ollama

response = ollama.chat(
    model='llama3.2-vision:11b',
    messages=[{
        'role': 'user',
        'content': '...',
    }],
    format={
        "type": "object",
        "properties": {...}
    },
    # keep_alive=True,
)

response.message.content
