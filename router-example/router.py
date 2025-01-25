from pydantic import BaseModel, Field, create_model
from openai import OpenAI
import instructor
from enum import Enum

class RouterQuery:
    def __init__(self, categories: Enum):
        self.client = instructor.from_openai(OpenAI())
        self.model = "gpt-4o-2024-08-06"

        self.response_model = create_model(
            'Choice',
            category=(categories, ...),
            reason=(str, Field(description="The reason for selecting this category"))
        )
       
        
    def route(self, query: str):
       
        choice = self.client.chat.completions.create(
            model=self.model,
            response_model=self.response_model,
            max_retries=1, 
            messages=[
                {"role": "system", "content": "You're a helpful personal assistant that can classify incoming messages."},
                {"role": "user", "content": query },
            ],
            )
            
        return choice 