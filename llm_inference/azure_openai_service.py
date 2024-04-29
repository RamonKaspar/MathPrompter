import os
from openai import AzureOpenAI

from .llm_interface import LLMInterface

class AzureOpenAIService(LLMInterface):
    def __init__(self, model_name):
        super().__init__(model_name)
        self.client = AzureOpenAI(
            api_version="2023-05-15",
            api_key=os.getenv("AZURE_OPENAI_KEY"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
        )

    def create_prompt(self, prompt):
        return [{"role": "user", "content": prompt}]

    def make_request(self, prompt):
        messages = self.create_prompt(prompt)
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            max_tokens=200,
            temperature=0.3
        )
        return response.choices[0].message.content