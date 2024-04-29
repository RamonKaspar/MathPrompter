# LLM Inference Service

This directory contains the modules necessary for interfacing with various Large Language Models (LLMs) such as Azure's OpenAI and Hugging Face models. It provides a way to abstract and standardize LLM access, making it easy to integrate and switch between different LLM services.

Structure:

- `llm_interface.py`: Defines the standard interface for LLM services.
- `azure_llm_service.py`: Implementation of the interface for Azure's LLM.
- `huggingface_llm_service.py`: Implementation of the interface for Hugging Face's LLM.
- `google_gemini_service.py`: Implementation of the interface for Google's Gemini Pro
- `llm_factory.py`: A factory module used to instantiate LLM service objects dynamically based on the desired service.

## Usage of the current services

Default is the usage of the Azure OpenAI API with the `gpt-35-turbo` model. However, you can find implemented services for the Google Gemini Pro API and all the available Hugging Face models.

1. Setting Up Environment:
   Ensure you have a `.env` file in your environment with the necessary API keys and endpoints (depends on the LLM you want to use) described as:

- `AZURE_OPENAI_KEY`
- `AZURE_OPENAI_ENDPOINT`

2. Initializing a Service:
   Import and use the `get_llm_service` function from `llm_factory.py` to initialize the LLM service of your choice:

```python
from llm_inference.llm_factory import get_llm_service

# Initialize Azure LLM Service
azure_service = get_llm_service('azure')
```

## Adding a New LLM Model

To incorporate a new LLM into the system:

1. ### Add API Keys and Endpoints: Set up the necessary keys and endpoints in your `.env` file.

2. ### Implement the Interface:

   - Create a new Python file for the LLM service.
   - Inherit from `LLMInterface`.
   - Implement all abstract methods (`create_prompt`, `make_request`).
     Example:

   ```python
   from llm_interface import LLMInterface

    class NewLLMService(LLMInterface):
        def create_prompt(self, prompt):
            # Implement prompt preparation
            pass

        def make_request(self, prompt):
            # Implement making an HTTP request to the LLM API
            pass
   ```

3. ### Register in the Factory:

   Modify `llm_factory.py` to recognize your new LLM service.
   Example:

   ```python
    def get_llm_service(service_name, model_name=None):
    if service_name == 'new_llm':
        return NewLLMService(model_name)
   ```

4. ### Usage
   Now you can use the newly added service in the same way as existing services by calling `get_llm_service('new_llm')`.
