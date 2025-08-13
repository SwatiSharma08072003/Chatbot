import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Retrieve API key from environment
api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=api_key)

# Validate API key
if not api_key or not api_key.startswith("gsk_"):
    st.error("🚫 Invalid or missing API key. Please check your .env file.")
    st.stop()

# Page configuration
st.set_page_config(page_title="AI Career Chat", page_icon="🤖", layout="centered")

# Sidebar with info
with st.sidebar:
    st.header("🔍 About This App")
    st.markdown("""
    Ask questions about careers in Artificial Intelligence:
    - Required skills
    - Popular job roles
    - Salary expectations
    - Future trends
    """)
    st.markdown("**Model Used:** `llama-3.3-70b-versatile`")
    st.markdown("---")
    st.caption("Powered by Groq & Streamlit")

# Main title
st.title("💼 Explore Careers in AI Technology")
st.markdown("Curious about AI jobs? Ask anything and get expert insights!")

# Input field
user_input = st.text_input(
    "🧠 What would you like to know?",
    placeholder="e.g., What skills are needed for AI jobs?"
)

# Submit button
if st.button("🚀 Get Answer"):
    if not user_input.strip():
        st.warning("⚠️ Please enter a question to get started.")
    else:
        with st.spinner("Thinking..."):
            try:
                chat_completion = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": "You are a helpful AI career advisor."},
                        {"role": "user", "content": user_input}
                    ]
                )
                response = chat_completion.choices[0].message.content.strip()
                st.success("✅ Here's what I found:")
                st.markdown(
                    f"<div style='background-color:#f0f2f6; padding:1em; border-radius:8px;'>{response}</div>",
                    unsafe_allow_html=True
                )
            except Exception as e:
                st.error("⚠️ Something went wrong while fetching the response.")
                st.caption(f"Error details: `{e}`")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "💬 Try asking about AI tools, certifications, or remote job options!"
    "</div>",
    unsafe_allow_html=True
)