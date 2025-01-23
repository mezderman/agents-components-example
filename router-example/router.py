from pydantic import BaseModel, Field
from openai import OpenAI
from prompts import ROUTER_PROMPT_TEMPLATE

class Choice(BaseModel):
    id: str = Field(description="The ID of the selected choice")
    choice: str = Field(description="The selected choice")
    reason: str = Field(description="The reason for selecting this choice")

class RouterQuery:
    def __init__(self,  choices: list[dict], model: str = "gpt-4o-2024-08-06"):
        self.client = OpenAI()
        self.model = model
        self.choices = choices
        self.choices_str = "\n".join(f"- {choice['text']} (id: {choice['id']})" for choice in choices)
        self.instructions = "\n".join(f"- {choice['instruction']}" for choice in choices)

        # Initialize OpenAI client
        self.client = OpenAI()

    def _format_choices(self) -> str:
        return "\n".join(f"- {choice['text']} (id: {choice['id']})" for choice in self.choices)
    
    def _validate_choice(self, choice: Choice) -> bool:
        valid_ids = {c['id'] for c in self.choices}
        return choice.id in valid_ids
        
    def route(self, query: str) -> Choice:
        prompt = ROUTER_PROMPT_TEMPLATE.format(
            query=query,
            choices_str=self.choices_str,
            instructions=self.instructions
        )
        completion = self.client.beta.chat.completions.parse(
            model=self.model,
            messages=[
                {"role": "system", "content": "Determine the best action based on the query provided."},
                {"role": "user", "content": prompt},
            ],
            response_format=Choice,
        )
        result = completion.choices[0].message.parsed
        
        if not self._validate_choice(result):
            raise ValueError(f"Model returned invalid choice id: {result.id}. Valid ids are: {[c['id'] for c in self.choices]}")
            
        return result 