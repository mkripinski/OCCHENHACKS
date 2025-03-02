import streamlit as st
import random
from google import generativeai
from streamlit_mic_recorder import speech_to_text

generativeai.configure(api_key="AIzaSyBFB5rg_NNHDzvbfV0dGlukpK5ViHNR4fI")
#System instructions
system_instructions = "Pretend you exist in Medieval Times. Respond to prompts with Medieval language"

model = generativeai.GenerativeModel("models/gemini-2.0-flash",
    system_instruction=system_instructions,)

def clear_history():
     st.session_state.chat = model.start_chat()
def generate_intro():
    """
    Returns a random medieval introduction message
    """
    intros = [
        "By the sacred command of Her Majesty, Kween Henlizabeth, Soverign of the Realm,",
        "In the name of Her Most Gracious Majesty, Kween Henlizabeth, Protector of the Kingdom,",
        "Let it be proclaimed across the lands, by order of Her Majesty, Kween Henlizabeth,",
        "By the divine right of Her Majesty, Kween Henlizabeth, Ruler of this great domain,",
        "It is hereby decreed, under the wisdom and authority of Her Majesty, Kween Henlizabeth,",
        "By the will of the Crown and the grace of the divine, Her Majesty, Kween Henlizabeth commands,"
    ]
    return random.choice(intros)

st.set_page_config(
    page_title="Kween's Pigeon",
)

#Session state variable declaration
if 'chat' not in st.session_state:
    st.session_state.chat = model.start_chat()
if 'prompt_selection' not in st.session_state:
    st.session_state.prompt_selection = 1
if "stt" not in st.session_state:
    st.session_state.stt = ""

#Page Title
st.title("Kween Henlizabeth's Behooving Benedict")

st.session_state.prompt_selection = st.sidebar.selectbox(
    label="How Doth Thou Wish To Assist Kween Henlizabeth",
    options=("Decree Creation",
      "General Use",
      ),
    on_change=clear_history
)

st.session_state.stt = speech_to_text(just_once=True, start_prompt="Start Ye Talkin",stop_prompt="End Ye Talkin")

with st.chat_message("assistant", avatar="https://cdn.openart.ai/uploads/image_tgCCAiI9_1740869342844_raw.jpg"):
        st.markdown("Greetings my Kween. How can I be of assistance?")


#User Enters Text
if user_prompt := st.chat_input("Enter Ye Decree Hence")or st.session_state.stt != "" and st.session_state.stt != None:
    if st.session_state.stt != "" and st.session_state.stt != None:
        user_prompt = st.session_state.stt


    # Add our input to the chat window
    with st.chat_message("user",avatar="./favicon-25.svg"):
        st.markdown(user_prompt)
    
    #send input to Gemini and retrieve response
    if st.session_state.prompt_selection == "Decree Creation":
         response = st.session_state.chat.send_message(f"You are the **Royal Scribe of the Kingdom**, a master of crafting grand royal decrees for the noble Kween Henlizabeth. "
                       f"All decrees follow a traditional structure, but the format should be maintained subtly without explicit section titles:\n\n"
                       f"- Begin with a **noble and authoritative introduction**, invoking the Kween's name with variation.\n"
                       f"- Clearly state the **law, order, or proclamation** in formal, grand language.\n"
                       f"- Conclude with a **strong closing declaration**, ensuring subjects understand its authority and enforcement.\n\n"
                       f"Here is an example of a past decree:\n\n"
                       f"---\n"
                       f"{generate_intro()}\n\n"  # Inserts a random intro here!
                       f"Let it be known that henceforth, all merchants conducting trade within the kingdom shall render "
                       f"a tithe of one in ten bushels of wheat to the royal granary, ensuring prosperity for all.\n\n"
                       f"This decree shall be enforced by the Crown’s magistrates and is effective immediately.\n"
                       f"---\n\n"
                       f"Now, write a similar decree based on the following request:\n"
                       f"{user_prompt}")
    else:
        response = st.session_state.chat.send_message(user_prompt)

    #add response to message box
    with st.chat_message("assistant", avatar="https://cdn.openart.ai/uploads/image_tgCCAiI9_1740869342844_raw.jpg"):
        st.markdown(response.text)
