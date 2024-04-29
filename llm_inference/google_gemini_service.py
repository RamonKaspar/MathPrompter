import os
import google.generativeai as genai

from .llm_interface import LLMInterface

class GoogleGeminiService(LLMInterface):
    def __init__(self, model_name='gemini-pro'):
        super().__init__(model_name)
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    def create_prompt(self, prompt):
        return prompt

    def make_request(self, prompt):
        gemini = genai.GenerativeModel(self.model_name)
        chat = gemini.start_chat(history=[])
        response = chat.send_message(prompt)
        return response.text