import streamlit as st
if 'english_notes' not in st.session_state:
    st.session_state.english_notes = ""
if 'herbology_notes' not in st.session_state:
    st.session_state.herbology_notes = ""
if 'math_notes' not in st.session_state:
    st.session_state.math_notes = ""
if 'english_notes_display' not in st.session_state:
    st.session_state.english_notes_display = ""
if 'herbology_notes_display' not in st.session_state:
    st.session_state.herbology_notes_display = ""
if 'math_notes_display' not in st.session_state:
    st.session_state.math_notes_display = ""

st.title("              Notes")
tab1, tab2, tab3 = st.tabs(["English", "Herbology", "Math"])
with tab1:
    st.header("English Notes :books:")
    st.session_state.english_notes_display += st.session_state.english_notes
    st.write(st.session_state.english_notes_display)
    st.text_area("Notes",key='english_notes',label_visibility="collapsed",)
   
with tab2:
    st.header("Herbology Notes :seedling:")
    st.session_state.herbology_notes_display += st.session_state.herbology_notes
    st.write(st.session_state.herbology_notes_display)
    st.text_area("Notes",key='herbology_notes',label_visibility="collapsed")
with tab3:
    st.header("Math Notes :blue_book:")
    st.session_state.math_notes_display += st.session_state.math_notes
    st.write(st.session_state.math_notes_display)
    st.text_area("Notes",key='math_notes',label_visibility="collapsed")
    


  