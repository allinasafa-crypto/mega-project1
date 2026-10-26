from openai import OpenAI

# pip install openai
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
        {"role": "user", "content": "what is coding"}
    ]
)

print(completion.choices[0].message.content)

