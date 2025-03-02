import streamlit as st

st.title("Notes")
tab1, tab2, tab3 = st.tabs(["English", "Herbology", "Math"])
with tab1:
    st.header("English Notes")
user_input = st.text_area("Notes")

with tab2:
    st.header("Herbology")
    

with tab3:
    st.header("Math")
    


#////////////////////////////////////

  