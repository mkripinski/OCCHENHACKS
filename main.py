import streamlit as st
import time
pg = st.navigation([st.Page("ai.py",title="Decree Drafting", default=True),
                    st.Page("cal.py",title="Calendar"),
                    st.Page("note.py",title="NoteTaking"),
                    ]
                    )

with st.sidebar:
    st.session_state.time = st.number_input("Timer",1)
    
    ph = st.empty()
    N = 5*60
    for secs in range(N,0,-1):
        mm, ss = secs//60, secs%60
        ph.metric("Timer", f"{mm:02d}:{ss:02d}")
        time.sleep(1)


pg.run()