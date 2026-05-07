import streamlit as st
import google.generativeai as genai

# Setup
genai.configure(api_key="AIzaSyAGk8IToRQAWBHMoTqxdnjwl9LtYB0CcXw")
model = genai.GenerativeModel('gemini-2.5-flash')

st.title("🤖 Niyas's Personal AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Show history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Get input
if prompt := st.chat_input("Ask me something..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    response = model.generate_content(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
    