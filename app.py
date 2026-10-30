import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

load_dotenv()

st.title("Skull AI")

model = ChatGroq(model="openai/gpt-oss-120b", temperature=1)

if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="you are a flirty AI agent and reply in a flirty manner to all responses.")
    ]

with st.chat_message("assistant"):
    st.write("Welcome to Skull AI how may I assist you?")

for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

prompt = st.chat_input("You : ")

if prompt:
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.write(prompt)

    response = model.invoke(st.session_state.messages)
    st.session_state.messages.append(AIMessage(content=response.content))
    with st.chat_message("assistant"):
        st.write(response.content)