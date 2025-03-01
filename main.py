import streamlit as st
from google import genai
client = genai.Client(api_key="AIzaSyBFB5rg_NNHDzvbfV0dGlukpK5ViHNR4fI")
chat = client.chats.create(model="gemini-2.0-flash")



st.title("King's Secret Helper")

if 'messages' not in st.session_state:
    st.session_state.messages = [{"role": "assistant", 
                 "content": "Greetings my King. How can I be of assistance?"},]
# We loop through each message in the session state and render it as
# a chat message.
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message["content"],)


if user_prompt := st.chat_input("Enter Ye Decree Hence"):
    # Add our input to the session state
    st.session_state.messages.append(
        {"role": "user", "content": user_prompt}
    )
    
    # Add our input to the chat window
    with st.chat_message("user"):
        st.markdown(user_prompt)
    
    response = chat.send_message(user_prompt)

    st.session_state.messages.append(
        {'role': "assistant",
         "content": response.text}
    )

    with st.chat_message("assistant"):
        st.markdown(response.text)