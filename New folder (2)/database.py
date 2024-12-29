import sqlite3

# This function will initialize the database if it doesn't exist
def init_db():
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS messages
                 (id INTEGER PRIMARY KEY, user_message TEXT, bot_reply TEXT)''')
    conn.commit()
    conn.close()

# Function to save the conversation in the database
def save_conversation(user_message, bot_reply):
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute('INSERT INTO messages (user_message, bot_reply) VALUES (?, ?)', 
              (user_message, bot_reply))
    conn.commit()
    conn.close()

# Function to fetch all conversations (for debugging or displaying previous chats)
def get_conversations():
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute('SELECT * FROM messages')
    conversations = c.fetchall()
    conn.close()
    return conversations
