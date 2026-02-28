import json
import os
import uuid

SESSION_DIR = 'sessions'

def create_session():
    """Creates a new session ID and an empty history file."""
    session_id = str(uuid.uuid4())
    filepath = os.path.join(SESSION_DIR, f"{session_id}.json")
    with open(filepath, 'w') as f:
        json.dump([], f)
    return session_id

def add_message(session_id, role, content):
    """Adds a message (user or assistant) to the session history."""
    filepath = os.path.join(SESSION_DIR, f"{session_id}.json")
    if not os.path.exists(filepath):
        raise ValueError(f"Session {session_id} not found")
        
    with open(filepath, 'r') as f:
        history = json.load(f)
        
    history.append({"role": role, "content": content})
    
    with open(filepath, 'w') as f:
        json.dump(history, f)

def get_history(session_id):
    """Retrieves the chat history for a given session."""
    filepath = os.path.join(SESSION_DIR, f"{session_id}.json")
    if not os.path.exists(filepath):
        return[]
    with open(filepath, 'r') as f:
        return json.load(f)

def clear_session(session_id):
    """Wipes the chat history for a session."""
    filepath = os.path.join(SESSION_DIR, f"{session_id}.json")
    if os.path.exists(filepath):
        # Overwrite with empty array
        with open(filepath, 'w') as f:
            json.dump([], f)