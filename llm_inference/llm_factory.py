from dotenv import load_dotenv

from .azure_openai_service import AzureOpenAIService
from .openai_service import OpenAIService

load_dotenv()   # Load the environment variables located in the .env file

def get_llm_service(service_name, model_name, temperature, max_tokens):
    """
    Get an instance of a Language Model Service.

    Parameters:
        service_name (str): Name of the LLM service provider.
        model_name (str): Name of the language model to use.
        temperature (float): Sampling temperature for generating responses.
        max_tokens (int): Maximum number of tokens to generate in each response.
        
    Returns:
        LLMInterface: Instance of a concrete implementation of LLMInterface.
    
    Raises:
        Exception: If the specified LLM service type is unsupported.
    """
    if service_name == 'azure':
        return AzureOpenAIService(model_name, temperature, max_tokens)
    elif service_name == 'openai':
        return OpenAIService(model_name, temperature, max_tokens)
    else:
        raise Exception("Unsupported LLM service type")