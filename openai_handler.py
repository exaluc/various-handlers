import requests

class OpenAIHandler:
    def __init__(self, api_key):
        self.api_key = api_key
        self.endpoint = "https://api.openai.com/v1/engines/davinci/completions"  # Utilisez l'URL de l'API pertinente ici

        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "User-Agent": "OpenAI-Python"
        }

    def complete(self, prompt, max_tokens=150):
        """Demandez une complétion à OpenAI basée sur un prompt."""
        data = {
            "prompt": prompt,
            "max_tokens": max_tokens
        }

        response = requests.post(self.endpoint, headers=self.headers, json=data)
        response_json = response.json()

        if response.status_code != 200:
            raise Exception(f"OpenAI API error: {response_json['error']}")

        return response_json['choices'][0]['text'].strip()

# Utilisation :

api_key = "VOTRE_API_KEY_OPENAI"

handler = OpenAIHandler(api_key)

response = handler.complete("Translate the following English text to French: 'Hello World'")
print(response)
