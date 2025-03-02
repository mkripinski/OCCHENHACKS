import streamlit as st

st.title("📅 Calendar")


calendar_url = "https://calendar.google.com/calendar/embed?src=fdf244d3bad05b417aae9441b4a141be7ba3edaba0d2f2a295eef2768cc6656d%40group.calendar.google.com&ctz=America%2FNew_York"

st.components.v1.iframe(calendar_url, width=800, height=600)
