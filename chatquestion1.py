import openai
import os
openai.api_key = os.getenv('OPENAI_API_KEY')

text = "What is the capital of Hungary?"
model_engine = "gpt-3.5-turbo"

try:
	print(f"Question: {text}")
	response = openai.ChatCompletion.create(model=model_engine, messages=[{"role": "user", "content": f"{text}"}]) 
	response_text = response.choices[0].message.content
	print(f"Response: {response_text}")
except openai.error.ServiceUnavailableError as e:
	print("Error: {0}".format(e))

