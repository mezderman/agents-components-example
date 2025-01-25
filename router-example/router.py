from pydantic import BaseModel, Field
from openai import OpenAI
from prompts import ROUTER_PROMPT_TEMPLATE
import instructor
from enum import Enum

class QueryCategory(str, Enum):
        """Enumeration of categories for incoming query.
        Pick specific if the query seeks detailed or pinpointed information
        Pick summary if the query seeks a broad overview or general understanding
        """

        SPECIFIC = "specific"
        SUMMARY = "summary"

class Choice(BaseModel):
    category: QueryCategory
    reason: str = Field(description="The reason for selecting this category")



class RouterQuery:
    def __init__(self):

        self.client = instructor.from_openai(OpenAI())
        self.model = "gpt-4o-2024-08-06"

    def _format_choices(self) -> str:
        return "\n".join(f"- {choice['text']} (id: {choice['id']})" for choice in self.choices)
    
    def _validate_choice(self, choice: Choice) -> bool:
        valid_ids = {c['id'] for c in self.choices}
        return choice.id in valid_ids
        
    def route(self, query: str) -> Choice:
        # prompt = ROUTER_PROMPT_TEMPLATE.format(
        #     query=query,
        #     choices_str=self.choices_str
        # )
       
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