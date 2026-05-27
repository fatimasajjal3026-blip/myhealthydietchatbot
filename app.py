import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key
groq_api_key = os.getenv("GROQ_API_KEY")

# Streamlit page settings
st.set_page_config(
    page_title="Healthy Diet Chatbot",
    page_icon="🥗"
)

st.title("🥗 Healthy Diet Chatbot")
st.write("Ask me anything about healthy food, diet plans, calories, and nutrition.")

# Initialize Groq LLM
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="llama-3.1-8b-instant"
)

# Prompt template
prompt = ChatPromptTemplate.from_template(
    """
    You are a professional healthy diet assistant.

    Answer the following question clearly and shortly.

    User Question:
    {question}
    """
)

# User input
user_question = st.text_input("Enter your question:")

# Button
if st.button("Ask Diet Bot"):

    if user_question.strip() == "":
        st.warning("Please enter a question.")
    else:
        try:
            # Create chain
            chain = prompt | llm

            # Get response
            response = chain.invoke({"question": user_question})

            # Display response
            st.subheader("🥦 Diet Bot Answer:")
            st.write(response.content)

        except Exception as e:
            st.error(f"Error: {e}")