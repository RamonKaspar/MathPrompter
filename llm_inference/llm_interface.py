class LLMInterface:
    def __init__(self, model_name, temperature, max_tokens):
        """
        Initialize the LLMInterface.

        Parameters:
            model_name (str): Name of the language model to use.
            temperature (float): Sampling temperature for generating responses.
            max_tokens (int): Maximum number of tokens to generate in each response.
        """
        self.model_name = model_name
        self.temperature = temperature
        self.max_tokens = max_tokens
        
    def create_prompt(self, system_prompt, few_shot_examples, question):
        """
        Create a prompt for the language model.

        Parameters:
            system_prompt (str): The system prompt to start the conversation.
            few_shot_examples (list): List of few-shot examples for in-context learning.
            question (str): The user's question to generate a response for.

        Returns:
            list: List of messages formatted for input to the language model.
            NOTE: YOU HAVE TO ADAPT THIS METHOD BASED ON THE LANGUAGE MODEL YOU USE
        """
        raise NotImplementedError
    
    def make_request(self, messages):
        """
        Make a request to the language model service.

        Parameters:
            messages (list): List of messages formatted for input to the language model.

        Returns:
            str: Generated response from the language model.
        """
        raise NotImplementedError