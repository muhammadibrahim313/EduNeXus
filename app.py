import streamlit as st
import os
from groq import Groq
import random

# Set up page configuration
st.set_page_config(page_title="EduNexus 🚀", page_icon="🚀", layout="wide")

# Initialize Groq client with API key
api_key = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=api_key)

# Define the LLaMA model
MODEL_NAME = "llama3-8b-8192"

# Function to call Groq API
def call_groq_api(prompt):
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=MODEL_NAME
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Define tool functions
def personalized_learning_assistant(topic):
    prompt = f"Create a personalized learning plan for the topic: {topic}"
    return call_groq_api(prompt)

def ai_coding_mentor(code_snippet):
    prompt = f"Review this code and provide improvements:\n{code_snippet}"
    return call_groq_api(prompt)

def smart_document_summarizer(document_text):
    prompt = f"Summarize this document:\n{document_text}"
    return call_groq_api(prompt)

def interactive_study_planner(exam_schedule):
    prompt = f"Create a study plan based on this exam schedule:\n{exam_schedule}"
    return call_groq_api(prompt)

def real_time_qa_support(question):
    prompt = f"Answer this question:\n{question}"
    return call_groq_api(prompt)

def mental_health_check_in(feelings):
    prompt = f"Provide supportive advice for someone feeling:\n{feelings}"
    return call_groq_api(prompt)

# Initialize session state
if 'responses' not in st.session_state:
    st.session_state['responses'] = {
        "personalized_learning_assistant": "",
        "ai_coding_mentor": "",
        "smart_document_summarizer": "",
        "interactive_study_planner": "",
        "real_time_qa_support": "",
        "mental_health_check_in": ""
    }

# Function to clear session state
def clear_response(key):
    st.session_state['responses'][key] = ""

# Custom CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

.main-title {
    font-size: 3.5rem;
    font-weight: 700;
    text-align: center;
    margin-bottom: 2rem;
    color: #ffffff;
}

.tool-card {
    background-color: rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    padding: 1.5rem;
    margin-bottom: 1rem;
    backdrop-filter: blur(10px);
}

.response-area {
    background-color: rgba(255, 255, 255, 0.1);
    border-radius: 10px;
    padding: 1rem;
    margin-top: 1rem;
}

.footer {
    text-align: center;
    padding: 1rem;
    background-color: rgba(255, 255, 255, 0.1);
    border-radius: 10px;
    margin-top: 2rem;
}

.footer a {
    color: #ffffff;
    text-decoration: none;
    margin: 0 1rem;
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)

# Main app
def main():
    # Title
    st.markdown("<h1 class='main-title'>🚀 Welcome to EduNexus</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.2rem;'>Your AI-powered learning companion</p>", unsafe_allow_html=True)

    # Sidebar navigation
    st.sidebar.markdown("<h2 style='text-align: center;'>🧠 EduNexus Tools</h2>", unsafe_allow_html=True)
    selected_task = st.sidebar.radio("Select a Tool", [
        "🧑‍🎓 Personalized Learning Assistant",
        "🤖 AI Coding Mentor",
        "📄 Smart Document Summarizer",
        "🗓 Interactive Study Planner",
        "❓ Real-Time Q&A Support",
        "💬 Mental Health Check-In"
    ])

    # Tool implementations
    tools = {
        "🧑‍🎓 Personalized Learning Assistant": {
            "key": "personalized_learning_assistant",
            "function": personalized_learning_assistant,
            "input_label": "What would you like to learn about? 🤔",
            "input_type": "text_input",
            "description": "Create a personalized learning plan just for you!"
        },
        "🤖 AI Coding Mentor": {
            "key": "ai_coding_mentor",
            "function": ai_coding_mentor,
            "input_label": "Paste your code here for review 👨‍💻",
            "input_type": "text_area",
            "description": "Get expert code review and suggestions!"
        },
        # Add similar configurations for other tools
    }

    tool = tools.get(selected_task)
    if tool:
        st.markdown(f"""
        <div class='tool-card'>
            <h3>{selected_task}</h3>
            <p>{tool['description']}</p>
        </div>
        """, unsafe_allow_html=True)

        # Input field
        if tool["input_type"] == "text_input":
            user_input = st.text_input(tool["input_label"])
        else:
            user_input = st.text_area(tool["input_label"])

        # Action buttons
        col1, col2 = st.columns([1, 3])
        with col1:
            if st.button("🧹 Clear"):
                clear_response(tool["key"])
                st.rerun()
        with col2:
            if st.button("🚀 Generate"):
                if user_input:
                    with st.spinner("Processing..."):
                        st.session_state['responses'][tool["key"]] = tool["function"](user_input)
                else:
                    st.session_state['responses'][tool["key"]] = "Please provide input to continue."

        # Display response
        st.markdown("<div class='response-area'>", unsafe_allow_html=True)
        st.markdown("### Response:")
        st.markdown(st.session_state['responses'][tool["key"]])
        st.markdown("</div>", unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <div class="footer">
        <a href="https://github.com/muhammadibrahim313" target="_blank">GitHub</a>
        <a href="https://www.linkedin.com/in/muhammad-ibrahim-qasmi-9876a1297/" target="_blank">LinkedIn</a>
        <a href="https://github.com/Ahmad-Fakhar" target="_blank">Partner's GitHub</a>
        <a href="https://www.linkedin.com/in/ahmad-fakhar-357742258/" target="_blank">Partner's LinkedIn</a>
    </div>
    """, unsafe_allow_html=True)

    # Inspirational quote
    quotes = [
        "The capacity to learn is a gift; the ability to learn is a skill; the willingness to learn is a choice. - Brian Herbert",
        "Education is the passport to the future, for tomorrow belongs to those who prepare for it today. - Malcolm X",
        "The beautiful thing about learning is that nobody can take it away from you. - B.B. King",
        "The more that you read, the more things you will know. The more that you learn, the more places you'll go. - Dr. Seuss",
        "Live as if you were to die tomorrow. Learn as if you were to live forever. - Mahatma Gandhi"
    ]
    st.sidebar.markdown(f"### 💡 Quote of the Day\n\n*{random.choice(quotes)}*")

if __name__ == "__main__":
    main()
