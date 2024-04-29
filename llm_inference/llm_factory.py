from dotenv import load_dotenv
from huggingface_hub import InferenceClient

from .huggingface_llm_service import HuggingFaceService
from .azure_openai_service import AzureOpenAIService
from .google_gemini_service import GoogleGeminiService

load_dotenv()   # Load the environment variables located in the .env file

def get_llm_service(service_name, model_name=None):
    if service_name == 'azure':
        return AzureOpenAIService(model_name)
    elif service_name == 'huggingface':
        # Check if model is deployed
        client = InferenceClient()
        list = client.list_deployed_models("text-generation-inference")['text-generation']
        for l in list:
            print(l)
        if not model_name in list:
            raise Exception(f"Model {model_name} is not deployed")
        return HuggingFaceService(model_name)
    elif service_name == 'google':
        return GoogleGeminiService()
    else:
        raise Exception("Unsupported LLM service type")