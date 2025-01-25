from pydantic import BaseModel, Field
from openai import OpenAI
import instructor
from models import QueryCategory




class Choice(BaseModel):
    category: QueryCategory
    reason: str = Field(description="The reason for selecting this category")



class RouterQuery:
    def __init__(self):

        self.client = instructor.from_openai(OpenAI())
        self.model = "gpt-4o-2024-08-06"
        
    def route(self, query: str) -> Choice:
       
        choice = self.client.chat.completions.create(
            model=self.model,
            response_model=Choice,
            max_retries=1, 
            messages=[
                {"role": "system", "content": "You're a helpful personal assistant that can classify incoming messages."},
                {"role": "user", "content": query },
            ],
            )
            
        return choice 