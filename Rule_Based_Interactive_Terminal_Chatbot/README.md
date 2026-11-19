# Rule-Based Interactive Terminal Assistant / Chatbot

## Project Overview

This project implements a Rule-Based Interactive Terminal Assistant using Python 3. It works as a customer support chatbot that recognizes user queries through keywords and regular expressions and provides appropriate responses using a JSON FAQ dataset.

The chatbot supports greetings, multiple intent recognition, contextual FAQ responses, fallback handling, and clean exit commands.

## Objectives

- Develop an interactive terminal-based chatbot.
- Recognize user intents using regular expressions.
- Load questions and answers from a JSON dataset.
- Handle multiple intents in a single user query.
- Provide appropriate responses to customer questions.
- Handle invalid queries and errors gracefully.

## Features

1. Greeting recognition.
2. Keyword-based intent detection.
3. Regular expression matching.
4. Multi-intent recognition.
5. JSON-based FAQ retrieval.
6. Contextual customer support responses.
7. Fallback handling for unknown queries.
8. Exit commands: "bye", "exit", and "quit".
9. Exception and error handling.

## Technologies Used

- Python 3
- Regular Expressions ("re")
- JSON
- pathlib
- Exception Handling

## Project Structure

Rule-Based-Chatbot/

├── chatbot.py

├── sample_faq.json

└── README.md

## Dataset Information

The project uses a JSON dataset containing:

- Greeting messages.
- Business operation hours.
- Internship project submission information.
- Certificate issuance information.

## Installation and Execution

Step 1: Install Python 3.

Step 2: Clone or download the repository.

Step 3: Open the project folder in VS Code.

Step 4: Ensure "chatbot.py" and "sample_faq.json" are in the same directory.

Step 5: Run the following command:
```
python chatbot.py
```
## Working Process

1. Load the FAQ dataset from the JSON file.
2. Normalize user input into lowercase.
3. Identify greetings using regular expressions.
4. Detect one or more user intents.
5. Retrieve matching answers from the FAQ dataset.
6. Display appropriate responses.
7. Handle unknown queries through fallback responses.
8. Terminate the conversation using exit commands.

## Example Queries

- Hello
- What are your business hours?
- How can I submit my internship project?
- When will I receive my certificate?
- Tell me about project submission and certificate details.

## Error Handling

The chatbot handles:

- Missing JSON dataset.
- Invalid JSON format.
- Invalid dataset structure.
- Empty user input.
- Keyboard interruption.
- Unknown user queries.

## Future Enhancements

- Add more customer support FAQs.
- Integrate product information and product queries.
- Add conversation history.
- Develop a graphical user interface.
- Integrate database connectivity.