import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("Chef Chat (2 Star Michelin Experience)")

def generate_content(prompt):
    response = client.chat.completions.create(
        model = 'gpt-4o-mini',
        messages = [
            
            {
                "role": "system",
                "content": "Youe are a 2 michelin star chef who wants to help home cooks improve their cooking skills .You may only answe4 homecooking related questions."
            },{
                "role": "user",
                "content": prompt
            }
        ],
        n=1,
        max_tokens=150
    )

    return response.choices[0].message.content


if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role":"assistant",
            "content":"How may i help you?"
        }
    ]

def display_messages():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def ai_function(prompt):
    
    response = generate_content(prompt)

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({
        "role":"user",
        "content":prompt
    })
    st.session_state.messages.append({
        "role":"assistant",
        "content":response
    })
    display_messages()

prompt = st.chat_input("Ask me anything!")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)

    ai_function(prompt)

if st.button("Clear All Messages"):
    st.session_state.messages = []  
    display_messages()