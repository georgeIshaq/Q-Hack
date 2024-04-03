import json

file_path = 'prompts.json'

with open(file_path, 'r') as file:
    data = json.load(file)

MATH_PROMPT = data['math_prompt']['prompt']
print(MATH_PROMPT)