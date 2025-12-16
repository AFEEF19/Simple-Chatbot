import streamlit as st

st.set_page_config(page_title="Simple Chatbot", page_icon="🤖")

st.title("🤖 Simple Friendly Chatbot")

st.write("Hello! I am a simple chatbot. Ask me something 😊")

# Chatbot logic
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! Nice to meet you 👋"
    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking 😊"
    elif "your name" in user_input:
        return "I'm a simple chatbot created for a µLearn task 🤖"
    elif "help" in user_input:
        return "I can chat with you and answer basic questions!"
    elif "bye" in user_input:
        return "Goodbye! Have a great day 👋"
    else:
        return "Sorry, I didn't understand that. Can you rephrase?"

# User input
user_input = st.text_input("You:")

if user_input:
    response = chatbot_response(user_input)
    st.text_area("Bot:", value=response, height=100)
