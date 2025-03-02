import streamlit as st
<<<<<<< HEAD
import random
from google import generativeai

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
=======
import time
if 'timer' not in st.session_state:
    st.session_state.timer = 0
    st.session_state.time = 0
>>>>>>> parent of f9af5e7 (Revert "Merge branch 'main' of https://github.com/mkripinski/OCCHENHACKS")

st.set_page_config(
    page_title="Kween's Pigeon",
)
pg = st.navigation([st.Page("ai.py",title="Decree Drafting", default=True),
                    st.Page("cal.py",title="Calendar"),
                    st.Page("note.py",title="NoteTaking"),
                    ]
                    )

<<<<<<< HEAD
#Session state variable declaration
if 'chat' not in st.session_state:
    st.session_state.chat = model.start_chat()
if 'prompt_selection' not in st.session_state:
    st.session_state.prompt_selection = 1
#Page Title
st.title("Kween Henlizabeth's Behooving Benedict")

st.session_state.prompt_selection = st.sidebar.selectbox(
    label="How Doth Thou Wish To Assist Kween Henlizabeth",
    options=("Decree Creation",
      "General Use",
      ),
    on_change=clear_history
)

with st.chat_message("assistant", avatar="https://cdn.openart.ai/uploads/image_tgCCAiI9_1740869342844_raw.jpg"):
        st.markdown("Greetings my Kween. How can I be of assistance?")


#User Enters Text
if user_prompt := st.chat_input("Enter Ye Decree Hence"):
   
    # Add our input to the chat window
    with st.chat_message("user",avatar="./favicon-25.svg"):
        st.markdown(user_prompt)
=======
with st.sidebar:
    def timer_start():
        for st.session_state.time in range(timer,0,-1):
            mm, ss = st.session_state.time//60, st.session_state.time%60
            ph.metric("Timer", f"{mm:02d}:{ss:02d}")
            time.sleep(1)
    
    timer = st.number_input("Timer",1,300)
    st.button("Start",on_click=timer_start)
    timer *=60
    ph = st.empty()
>>>>>>> parent of f9af5e7 (Revert "Merge branch 'main' of https://github.com/mkripinski/OCCHENHACKS")
    

<<<<<<< HEAD
    #add response to message box
    with st.chat_message("assistant", avatar="https://cdn.openart.ai/uploads/image_tgCCAiI9_1740869342844_raw.jpg"):
        st.markdown(response.text)
=======

pg.run()
>>>>>>> parent of f9af5e7 (Revert "Merge branch 'main' of https://github.com/mkripinski/OCCHENHACKS")
