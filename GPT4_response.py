import requests

def gpt4_api_call(prompt, api_key):
    url = "https://api.openai.com/v1/engines/davinci-codex/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 100
    }

    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()

    return response_json["choices"][0]["text"]

# Usage example
prompt = ""  # Add your prompt here
api_key = ""  # Add your API key here

response = gpt4_api_call(prompt, api_key)
print(response)