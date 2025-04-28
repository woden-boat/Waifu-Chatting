from ollama import Client
from config import BaseConfig

class OllamaClient:
    def __init__(self):
        self.ollama_client = Client(host=BaseConfig.OLLAMA_HOST)
    
    def streamOllamaResponse(self, prompt, model=BaseConfig.MODEL_NAME):
        stream = self.ollama_client.chat(
            model=model,
            messages=[{'role': 'user', 'content': f"{BaseConfig.pre_prompt}\n{prompt}"}],
            stream=True
        )
        for chunk in stream:
            content = chunk['message']['content']
            yield content