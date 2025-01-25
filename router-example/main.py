from dotenv import load_dotenv
from router import RouterQuery
from pydantic import BaseModel, Field
from enum import Enum


# Load environment variables
load_dotenv()


def main():
    query = "What are the main points of the document?"
    # query = "What are the highlights of this article?"
    # query = "What is the name of the event?"
    # query = "Who is the main person mentioned in the document?"
    # query = "What is the name of the event?"
    # query = "I have question about billings?"

    class Categories(str, Enum):
        """Enumeration of categories for incoming query.
        Pick specific if the query seeks detailed or pinpointed information
        Pick summary if the query seeks a broad overview or general understanding
        Pick other if the query if doesnt fit into specific or summary
        """
        SPECIFIC = "specific"
        SUMMARY = "summary"
        OTHER = "other"
    
    

    router = RouterQuery(Categories)

    result = router.route(query)
    print(result)
   

if __name__ == "__main__":
    main() 