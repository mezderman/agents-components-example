import os
from dotenv import load_dotenv
from openai import OpenAI
from router import RouterQuery
from models import QueryCategory
from pydantic import BaseModel, Field


# Load environment variables
load_dotenv()


def main():
    # query = "What are the main points of the document?"
    # query = "What are the highlights of this article?"
    query = "What would you tell someone who hasn't read this yet?"
    # query = "What is the name of the event?"
    # query = "Who is the main person mentioned in the document?"

    router = RouterQuery()
    result = router.route(query)
    print(result)
   

if __name__ == "__main__":
    main() 