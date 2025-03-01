import streamlit as st
from google import generativeai

generativeai.configure(api_key="AIzaSyBFB5rg_NNHDzvbfV0dGlukpK5ViHNR4fI")
#System instructions
system_instructions = "Pretend you exist in Medieval Times. Respond to prompts with Medieval language"

model = generativeai.GenerativeModel("models/gemini-2.0-flash",
    system_instruction=system_instructions,)


#Prompt definitions
prompts = [
    "Enter First Prompt Here",
    "Enter Second Prompt Here"

]

def clear_history():
     st.session_state.chat = model.start_chat()

st.set_page_config(
    page_title="King's Pigeon",
)

#Session state variable declaration
if 'chat' not in st.session_state:
    st.session_state.chat = model.start_chat()
if 'prompt_selection' not in st.session_state:
    st.session_state.prompt_selection = 1
#Page Title
st.title("King's Secret Helper")

st.sidebar.radio("Chat Selection:",
                 ["Declarations",
                  "ndnsclsmlc"],
                  on_change=clear_history
                  )

with st.chat_message("assistant"):
        st.markdown("Greetings my King. How can I be of assistance?")

#prompt selection cases
match st.session_state.prompt_selection:

        case 1:

            st.session_state.chat.send_message(prompts[1])
        case 2:
            st.session_state.chat.send_message(prompts[2])
        case _:
            st.warning("Ye Must Choose Ye Chat Type")

#User Enters Text
if user_prompt := st.chat_input("Enter Ye Decree Hence"):
   
    # Add our input to the chat window
    with st.chat_message("user"):
        st.markdown(user_prompt)
    
    #send input to Gemini and retrieve response
    response = st.session_state.chat.send_message(user_prompt)

    #add response to message box
    with st.chat_message("assistant"):
        st.markdown(response.text)