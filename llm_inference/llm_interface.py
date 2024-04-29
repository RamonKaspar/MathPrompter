class LLMInterface:
    def __init__(self, model_name=None):
        self.model_name = model_name
        
    def create_prompt(self, prompt):
        raise NotImplementedError
    
    def make_request(self, prompt):
        raise NotImplementedError