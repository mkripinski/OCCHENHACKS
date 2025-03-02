import streamlit as st
import time
if 'timer' not in st.session_state:
    st.session_state.timer = 0
    st.session_state.time = 0

st.set_page_config(
    page_title="Kween's Pigeon",
)
pg = st.navigation([st.Page("ai.py",title="Decree Drafting", default=True),
                    st.Page("cal.py",title="Calendar"),
                    st.Page("note.py",title="NoteTaking"),
                    ]
                    )

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
    


pg.run()