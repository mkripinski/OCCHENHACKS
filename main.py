import streamlit as st
from google import generativeai

generativeai.configure(api_key="AIzaSyBFB5rg_NNHDzvbfV0dGlukpK5ViHNR4fI")
#System instructions
system_instructions = "Pretend you exist in Medieval Times. Respond to prompts with Medieval language"

model = generativeai.GenerativeModel("models/gemini-2.0-flash",
    system_instruction=system_instructions,)

<<<<<<< Updated upstream

#Prompt definitions
prompts = [
    f"You are the **Royal Scribe of the Kingdom**, a master of crafting grand royal decrees. "
    f"All decrees follow a traditional structure, but the format should be maintained subtly without explicit section titles:\n\n"
    f"- Begin with a **noble and authoritative introduction**, invoking the King’s name.\n"
    f"- Clearly state the **law, order, or announcement** in formal, grand language.\n"
    f"- Conclude with a **strong closing declaration**, ensuring subjects understand its authority.\n\n"
    f"Here is an example of a past decree:\n\n"
    f"---\n"
    f"By Royal Decree of His Majesty, King Aldric the Wise, Ruler of the Realm,\n\n"
    f"Let it be known that henceforth, all merchants conducting trade within the kingdom shall render "
    f"a tithe of one in ten bushels of wheat to the royal granary, ensuring prosperity for all.\n\n"
    f"This decree shall be enforced by the Crown’s magistrates and is effective immediately.\n"
    f"---\n\n"
    f"Now, write a similar decree based on the following request:\n"
    f"{user_prompt}",
    "Enter Second Prompt Here"
]

=======
>>>>>>> Stashed changes
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

st.session_state.prompt_selection = st.sidebar.selectbox(
    label="How Doth Thou Wish To Assist Kween Henlizabeth",
    options=("Decree Creation",
      "Future option 2",
      ),
    on_change=clear_history
)

with st.chat_message("assistant"):
        st.markdown("Greetings my King. How can I be of assistance?")


#User Enters Text
if user_prompt := st.chat_input("Enter Ye Decree Hence"):
   
    # Add our input to the chat window
    with st.chat_message("user"):
        st.markdown(user_prompt)
    
    #send input to Gemini and retrieve response
    if st.session_state.prompt_selection == "Decree Creation":
         response = st.session_state.chat.send_message(f"You are the Royal Scribe of the Kingdom. Speak in grand, medieval style. "
                                                        f"Format your response as a formal decree, following this structure:\n\n"
                                                        f"📜 **Grand Introduction** 📜\n"
                                                         f"📖 **Proclamation of the Law or Message** 📖\n"
                                                          f"🏰 **Closing Words from the Crown** 🏰\n\n"
                                                            f"Here is the King's request: {user_prompt}")
    else:
        response = st.session_state.chat.send_message(user_prompt)

    #add response to message box
    with st.chat_message("assistant"):
        st.markdown(response.text)
