# Router Agent Example

This example demonstrates the implementation of an Agent Router that can intelligently route queries to the appropriate handler based on the query's content.

## Overview

The Router Agent uses OpenAI's GPT models to analyze incoming queries and determine the most appropriate routing destination based on predefined choices. This is particularly useful in systems where different types of queries need different handling approaches.

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Example Structure

- `main.py`: Example usage of the router
- `router.py`: Implementation of the RouterQuery class
- `prompts.py`: Contains the prompt template for the router

## Usage

The example in `main.py` shows how to use the router with two routing choices: "specific" and "summary". You can modify these choices or add new ones based on your needs.

Run the example:

```bash
python main.py
```

This will execute the router and print the result to the console.

Example output:

```json
{
"id": "summary",
"reason": "The query specifically asks for the name of an event, which is a request for detailed and precise information rather than a broad or general overview"
}
```

This output indicates that the query was routed to the "specific" choice, and the explanation provides a rationale for this decision.

## Customization

You can customize the routing choices by modifying the `choices` list in `main.py`. Each choice should have:
- `id`: Unique identifier for the choice
- `text`: Guidance for when to select this choice

## License

MIT