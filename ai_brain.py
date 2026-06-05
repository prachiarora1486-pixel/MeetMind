# ai_brain.py
import os
from groq import Groq

# Initialize the Groq Brain using the key inside your hidden .env file
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_meeting_briefing(contact_name, past_history_list):
    """Asks the AI to generate a professional briefing based on history."""
    
    # Format the list of history into clear bullet points for the AI
    if past_history_list:
        formatted_history = "\n".join([f"- {note}" for note in past_history_list])
    else:
        formatted_history = "No previous history found. This is your very first meeting with them."
        
    # The system prompt instructions give the AI its unique personality and goal
    system_instruction = (
        "You are an elite executive assistant AI. Your goal is to prepare a brief, "
        "high-impact, bulleted meeting preparation guide for the user."
    )
    
    user_prompt = f"""
    Please prepare a briefing for my upcoming meeting with: {contact_name}
    
    Here is the historical context of my past interactions with this person:
    {formatted_history}
    
    Provide your output exactly in this structure:
    1. SUMMARY OF PAST INTERACTION (Keep it short)
    2. KEY REMINDERS (Promises made or things to look out for)
    3. SUGGESTED CONVERSATION OPENERS
    """
    
    # Call the Groq Cloud API
    response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",  # Update this line
    messages=[
        {"role": "system", "content": system_instruction},
        {"role": "user", "content": user_prompt}
    ],
    temperature=0.6
)
    
    return response.choices[0].message.content