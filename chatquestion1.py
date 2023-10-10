import openai
import os
openai.api_key = os.getenv('OPENAI_API_KEY')

text1 = "Hello. What is the capital of Hungary?"
text2 = "Hello. What is the maximum of integer numbers 2 and 5"
model_engine = "gpt-3.5-turbo"

try:
	print(f"Question: {text2}")
	response = openai.ChatCompletion.create(model=model_engine, messages=[{"role": "user", "content": f"{text2}"}]) 
	response_text = response.choices[0].message.content
	print(f"Response: {response_text}")
except openai.error.ServiceUnavailableError as e:
	print("Error: {0}".format(e))

