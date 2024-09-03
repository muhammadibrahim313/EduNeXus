import streamlit as st
from groq import Groq
from streamlit.components.v1 import html
import random

# Set up page configuration
st.set_page_config(page_title="EduNexus 🚀", page_icon="🚀", layout="wide")

api_key = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=api_key)

# Define the LLaMA model to be used
MODEL_NAME = "llama3-8b-8192"  # Replace with your actual model name

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

# Initialize session state if not already set
if 'responses' not in st.session_state:
    st.session_state['responses'] = {
        "personalized_learning_assistant": "",
        "ai_coding_mentor": "",
        "smart_document_summarizer": "",
        "interactive_study_planner": "",
        "real_time_qa_support": "",
        "mental_health_check_in": ""
    }

# Function to clear session state values
def clear_session_state():
    for key in st.session_state.keys():
        if key.startswith('responses'):
            st.session_state[key] = ""
        if key in ['personalized_learning_assistant', 'ai_coding_mentor', 'smart_document_summarizer', 'interactive_study_planner', 'real_time_qa_support', 'mental_health_check_in']:
            st.session_state[key] = ""


import streamlit as st

# Apply custom CSS for input and text area fields
st.markdown("""
<style>
    .stTextInput, .stTextArea {
        color: black; /* Set the text color to black for better visibility */
        background-color: white; /* Ensure the background is white */
        font-size: 16px; /* Optional: Adjust font size for better readability */
    }
    .stTextInput::placeholder, .stTextArea::placeholder {
        color: #888888; /* Set the placeholder text color */
    }
</style>
""", unsafe_allow_html=True)

# Your Streamlit code continues below...


# Function to load custom CSS
def load_css():
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    body {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: #ffffff;
    }
    
    .stApp {
        background-color: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    }
    
    .main-title {
        font-size: 3.5rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 2rem;
        color: #ffffff;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .stButton > button {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        color: white;
        border: none;
        border-radius: 30px;
        padding: 0.6rem 1.2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 8px rgba(0,0,0,0.15);
    }
    
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background-color: #818f8f;
        border: 2px solid rgba(255, 255, 255, 0.5);
        border-radius: 10px;
        color: #ffffff;
        font-size: 1rem;
    }
    
    .stRadio > div {
        background-color: rgba(255, 255, 255, 0.2);
        border-radius: 10px;
        padding: 1rem;
    }
    
    .stRadio > div > label {
        color: #ffffff !important;
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
        transition: all 0.3s ease;
    }
    
    .footer a:hover {
        color: #4ECDC4;
    }
    
    /* Animated background */
    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    
    body::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        z-index: -1;
    }
    
    /* 3D Card Effect */
    .tool-card {
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        transition: all 0.3s ease;
        transform: perspective(1000px) rotateX(0deg) rotateY(0deg);
        box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
    }
    
    .tool-card:hover {
        transform: perspective(1000px) rotateX(10deg) rotateY(10deg);
        box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
    }
    
    /* Emoji styles */
    .emoji {
        font-size: 2rem;
        margin-right: 0.5rem;
    }
    </style>
    """

# Inject custom CSS
st.markdown(load_css(), unsafe_allow_html=True)

# Main content area with 3D-inspired title
st.markdown("<h1 class='main-title'>🚀 Welcome to EduNexus</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2rem; margin-bottom: 2rem;'>Your AI-powered learning companion for the 21st century</p>", unsafe_allow_html=True)

# Sidebar with navigation options
st.sidebar.markdown("<h2 style='text-align: center;'>🧠 EduNexus Tools</h2>", unsafe_allow_html=True)
selected_task = st.sidebar.radio("Select a Tool", [
    "🧑‍🎓 Personalized Learning Assistant",
    "🤖 AI Coding Mentor",
    "📄 Smart Document Summarizer",
    "🗓 Interactive Study Planner",
    "❓ Real-Time Q&A Support",
    "💬 Mental Health Check-In"
])

# Display the selected task based on user selection
st.markdown(f"<h2 class='tool-title'>{selected_task}</h2>", unsafe_allow_html=True)

if selected_task == "🧑‍🎓 Personalized Learning Assistant":
    st.markdown("""
    <div class='tool-card'>
        <h3><span class='emoji'>🎓</span>Create Your Learning Journey</h3>
        <p>Enter a topic you're interested in, and let our AI craft a personalized learning plan just for you!</p>
    </div>
    """, unsafe_allow_html=True)
    topic = st.text_input("What would you like to learn about? 🤔")
    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("🧹 Clear"):
            st.session_state['responses']["personalized_learning_assistant"] = ""
            st.rerun()
    with col2:
        if st.button("🚀 Generate Learning Plan"):
            if topic:
                with st.spinner("Crafting your personalized learning journey..."):
                    st.session_state['responses']["personalized_learning_assistant"] = personalized_learning_assistant(topic)
            else:
                st.session_state['responses']["personalized_learning_assistant"] = "Please enter a topic to get started on your learning adventure! 📚"
    
    st.markdown("<div class='response-area'>", unsafe_allow_html=True)
    st.markdown("### Your Personalized Learning Plan:")
    st.markdown(st.session_state['responses']["personalized_learning_assistant"])
    st.markdown("</div>", unsafe_allow_html=True)

elif selected_task == "🤖 AI Coding Mentor":
    st.markdown("""
    <div class='tool-card'>
        <h3><span class='emoji'>🤖</span>Code Smarter, Not Harder</h3>
        <p>Need help with your code? Describe your problem or share your code, and let our AI mentor assist you!</p>
    </div>
    """, unsafe_allow_html=True)
    code_problem = st.text_area("Describe your coding problem or paste your code here: 👨‍💻")
    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("🧹 Clear"):
            st.session_state['responses']["ai_coding_mentor"] = ""
            st.rerun()
    with col2:
        if st.button("🚀 Get Coding Assistance"):
            if code_problem:
                with st.spinner("Analyzing your code..."):
                    st.session_state['responses']["ai_coding_mentor"] = ai_coding_mentor(code_problem)
            else:
                st.session_state['responses']["ai_coding_mentor"] = "Please describe your coding issue or paste your code above. 🤓"
    
    st.markdown("<div class='response-area'>", unsafe_allow_html=True)
    st.markdown("### AI Coding Mentor's Response:")
    st.markdown(st.session_state['responses']["ai_coding_mentor"])
    st.markdown("</div>", unsafe_allow_html=True)

elif selected_task == "📄 Smart Document Summarizer":
    st.markdown("""
    <div class='tool-card'>
        <h3><span class='emoji'>📄</span>Summarize Documents with Ease</h3>
        <p>Upload or paste a document, and our AI will provide a concise summary for you!</p>
    </div>
    """, unsafe_allow_html=True)
    document_text = st.text_area("Paste the document text you want summarized: 📄")
    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("🧹 Clear"):
            st.session_state['responses']["smart_document_summarizer"] = ""
            st.rerun()
    with col2:
        if st.button("🚀 Summarize Document"):
            if document_text:
                with st.spinner("Summarizing your document..."):
                    st.session_state['responses']["smart_document_summarizer"] = smart_document_summarizer(document_text)
            else:
                st.session_state['responses']["smart_document_summarizer"] = "Please paste some text to get a summary! 📝"
    
    st.markdown("<div class='response-area'>", unsafe_allow_html=True)
    st.markdown("### Summary of Your Document:")
    st.markdown(st.session_state['responses']["smart_document_summarizer"])
    st.markdown("</div>", unsafe_allow_html=True)

elif selected_task == "🗓 Interactive Study Planner":
    st.markdown("""
    <div class='tool-card'>
        <h3><span class='emoji'>🗓</span>Create Your Study Schedule</h3>
        <p>Plan your study sessions and let our AI optimize your learning experience!</p>
    </div>
    """, unsafe_allow_html=True)
    study_goals = st.text_area("What are your study goals for this week? 🎯")
    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("🧹 Clear"):
            st.session_state['responses']["interactive_study_planner"] = ""
            st.rerun()
    with col2:
        if st.button("🚀 Generate Study Plan"):
            if study_goals:
                with st.spinner("Creating your study plan..."):
                    st.session_state['responses']["interactive_study_planner"] = interactive_study_planner(study_goals)
            else:
                st.session_state['responses']["interactive_study_planner"] = "Please enter your study goals to get a customized study plan! 📚"
    
    st.markdown("<div class='response-area'>", unsafe_allow_html=True)
    st.markdown("### Your Interactive Study Plan:")
    st.markdown(st.session_state['responses']["interactive_study_planner"])
    st.markdown("</div>", unsafe_allow_html=True)

elif selected_task == "❓ Real-Time Q&A Support":
    st.markdown("""
    <div class='tool-card'>
        <h3><span class='emoji'>❓</span>Get Answers in Real Time</h3>
        <p>Ask a question and receive an instant response from our AI-powered support!</p>
    </div>
    """, unsafe_allow_html=True)
    question = st.text_input("What's your question? 🧐")
    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("🧹 Clear"):
            st.session_state['responses']["real_time_qa_support"] = ""
            st.rerun()
    with col2:
        if st.button("🚀 Get Answer"):
            if question:
                with st.spinner("Finding the best answer..."):
                    st.session_state['responses']["real_time_qa_support"] = real_time_qa_support(question)
            else:
                st.session_state['responses']["real_time_qa_support"] = "Please ask a question to get an answer! 🤔"
    
    st.markdown("<div class='response-area'>", unsafe_allow_html=True)
    st.markdown("### Real-Time Q&A Response:")
    st.markdown(st.session_state['responses']["real_time_qa_support"])
    st.markdown("</div>", unsafe_allow_html=True)

elif selected_task == "💬 Mental Health Check-In":
    st.markdown("""
    <div class='tool-card'>
        <h3><span class='emoji'>💬</span>Check In On Your Well-Being</h3>
        <p>Take a moment to reflect on your mental health and receive supportive feedback from our AI.</p>
    </div>
    """, unsafe_allow_html=True)
    mood_description = st.text_area("How are you feeling today? 🌦️")
    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("🧹 Clear"):
            st.session_state['responses']["mental_health_check_in"] = ""
            st.rerun()
    with col2:
        if st.button("🚀 Get Support"):
            if mood_description:
                with st.spinner("Providing feedback on your well-being..."):
                    st.session_state['responses']["mental_health_check_in"] = mental_health_check_in(mood_description)
            else:
                st.session_state['responses']["mental_health_check_in"] = "Please share how you're feeling to receive support! 💖"
    
    st.markdown("<div class='response-area'>", unsafe_allow_html=True)
    st.markdown("### Mental Health Support:")
    st.markdown(st.session_state['responses']["mental_health_check_in"])
    st.markdown("</div>", unsafe_allow_html=True)



# Footer
st.markdown("""
<div class='footer'>
    <p>EduNexus © 2024 | Designed with 💖 by [Your Name]</p>
    <p><a href='#'>Terms</a> | <a href='#'>Privacy</a> | <a href='#'>Contact</a></p>
</div>
""", unsafe_allow_html=True)
