import streamlit as st
import uuid
from collections import deque

from utils.llm_utils import ask_llm

if 'session_id' not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())
if 'messages' not in st.session_state:
    st.session_state.messages = deque()
    
st.title("Chat with LLM")
st.write(st.session_state)

for idx, message in enumerate(st.session_state.messages):
    st.write(f"**{message['role']:** {message['content']}}")    
    
user_input = st.text_input("You:", key="input")
if st.button("Send"):
    if user_input:
        st.session_state.message.append()