# chatbot
This repository contains the code for a simple chatbot built using Flask, SQLite, and HTML/CSS for the frontend. The chatbot can answer predefined questions and store conversations in a SQLite database.

Requirements
Python 
Flask
SQLite (comes pre-installed with Python)
HTML, CSS, JavaScript (for the frontend)

python app.py
The server will start running on http://127.0.0.1:5000/.

Access the Chatbot: Open a web browser and navigate to http://127.0.0.1:5000/ to interact with the chatbot. The chatbot will answer predefined questions, and each conversation will be stored in the database.

Project Structure
plaintext
Copy code
chatbot-flask/
│
├── app.py             # Flask application with chatbot logic
├── database.py        # SQLite database handling
├── templates/
│   └── index.html     # HTML template for chatbot frontend
└── static/
    └── style.css      # CSS styles for the chatbot interface
Key Features
Flask Server: A lightweight web server to handle user requests.
SQLite Database: Stores user messages and chatbot replies.
Predefined Responses: The chatbot responds to a set of predefined questions.
.
How to Use the Chatbot
Open the chatbot page in your browser.
Type your message in the input box and click the "Send" button.
The chatbot will respond based on predefined responses in app.py.
Conversations are saved to the SQLite database, accessible through the backend.
Example Questions
"Hi"
"How are you?"
"What devices do you sell?"
"Can I track my order?"
"How do I cancel my order?"
