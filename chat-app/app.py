import streamlit as st

st.set_page_config(page_title="Chat App", page_icon=":speech_balloon:", layout="wide")

st.title("Welcome to the Chat App!")
st.write("chatbot with intent ...")

user_input=st.text_input("Type your message here...")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if st.button("Send"):
    pass
