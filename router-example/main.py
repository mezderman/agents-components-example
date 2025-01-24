import os
from dotenv import load_dotenv
from openai import OpenAI
from router import RouterQuery

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI()

def main():
    # Test the parser
    choices = [
        {
            "id": "specific", 
            "text": "Pick 'specific' if the query seeks detailed or pinpointed information"
        },
        {
            "id": "summary", 
            "text": "Pick 'summary' if the query seeks a broad overview or general understanding"
        }
    ]

    router = RouterQuery(choices=choices)

    # query = "What are the main points of the document?"
    # query = "What are the highlights of this article?"
    query = "What would you tell someone who hasn’t read this yet?"
    # query = "What is the name of the event?"
    # query = "Who is the main person mentioned in the document?"
    
    result = router.route(query)
    print(result)
   

if __name__ == "__main__":
    main() 