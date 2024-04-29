import requests
from transformers import AutoTokenizer
import os

from .llm_interface import LLMInterface

class HuggingFaceService(LLMInterface):
    def __init__(self, model_name):
        super().__init__(model_name)
        self.api_url = "https://api-inference.huggingface.co/models/" + model_name
        self.headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_TOKEN')}"}
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

    def create_prompt(self, prompt):
        chat_creation = [{"role": "user", "content": prompt}]
        chat_tokenized = self.tokenizer.apply_chat_template(chat_creation, tokenize=False)
        return {
            "inputs": chat_tokenized,
            "parameters": {
                "temperature": 0.3,
                "max_new_tokens": 200
            }
        }

    def make_request(self, prompt):
        messages = self.create_prompt(prompt)
        response = requests.post(self.api_url, headers=self.headers, json=messages)
        if response.status_code == 200:
            response_data = response.json()
            return response_data[0]['generated_text']
        else:
            raise Exception(f"Request failed with status code {response.text}")
