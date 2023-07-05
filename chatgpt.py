import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

while(True):
   
    question = input('What is your question? \n ')
    print(question)

    if(question.lower() == 'quit'):
        break
    completion = openai.Completion.create(
        model= 'gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "you are an assistant. Answer the given question"},
            {"role": "user", "content": question}
        ]
    )
    print('\033[32m'+completion.choices[0].message.content + '\n')