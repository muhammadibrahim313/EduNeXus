import streamlit as st
import os
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

# Define functions for each tool with few-shot examples (unchanged)
def personalized_learning_assistant(topic):
    # ... (unchanged)

def ai_coding_mentor(code_snippet):
    # ... (unchanged)

def smart_document_summarizer(document_text):
    # ... (unchanged)

def interactive_study_planner(exam_schedule):
    # ... (unchanged)

def real_time_qa_support(question):
    # ... (unchanged)

def mental_health_check_in(feelings):
    # ... (unchanged)

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
        background-color: rgba(255, 255, 255, 0.2);
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
        <h3><span class='emoji'>💻</span>Get Expert Code Review</h3>
        <p>Paste your code snippet below, and our AI mentor will provide insightful suggestions and improvements!</p>
    </div>
    """, unsafe_allow_html=True)
    code_snippet = st.text_area("Paste your code here for review 👨‍💻")
    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("🧹 Clear"):
            st.session_state['responses']["ai_coding_mentor"] = ""
            st.rerun()
    with col2:
        if st.button("🔍 Analyze Code"):
            if code_snippet:
                with st.spinner("Analyzing your code with AI precision..."):
                    st.session_state['responses']["ai_coding_mentor"] = ai_coding_mentor(code_snippet)
            else:
                st.session_state['responses']["ai_coding_mentor"] = "Please enter a code snippet for our AI to review and enhance! 🖥️"
    
    st.markdown("<div class='response-area'>", unsafe_allow_html=True)
    st.markdown("### AI Code Review Results:")
    st.code(st.session_state['responses']["ai_coding_mentor"])
    st.markdown("</div>", unsafe_allow_html=True)

elif selected_task == "📄 Smart Document Summarizer":
    st.markdown("""
    <div class='tool-card'>
        <h3><span class='emoji'>📚</span>Summarize Any Document</h3>
        <p>Paste your document text, and watch as our AI distills it into a concise, informative summary!</p>
    </div>
    """, unsafe_allow_html=True)
    document_text = st.text_area("Paste your document text here 📝")
    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("🧹 Clear"):
            st.session_state['responses']["smart_document_summarizer"] = ""
            st.rerun()
    with col2:
        if st.button("📊 Summarize"):
            if document_text:
                with st.spinner("Condensing your document into a brilliant summary..."):
                    st.session_state['responses']["smart_document_summarizer"] = smart_document_summarizer(document_text)
            else:
                st.session_state['responses']["smart_document_summarizer"] = "Please paste a document for our AI to summarize! 📄"
    
    st.markdown("<div class='response-area'>", unsafe_allow_html=True)
    st.markdown("### Your Document Summary:")
    st.markdown(st.session_state['responses']["smart_document_summarizer"])
    st.markdown("</div>", unsafe_allow_html=True)

elif selected_task == "🗓 Interactive Study Planner":
    st.markdown("""
    <div class='tool-card'>
        <h3><span class='emoji'>📅</span>Plan Your Study Schedule</h3>
        <p>Input your exam dates and subjects, and let our AI create a tailored study plan to maximize your success!</p>
    </div>
    """, unsafe_allow_html=True)
    exam_schedule = st.text_area("Enter your exam schedule (e.g., 'Math: May 15, Physics: May 20') 📆")
    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("🧹 Clear"):
            st.session_state['responses']["interactive_study_planner"] = ""
            st.rerun()
    with col2:
        if st.button("🎯 Create Study Plan"):
            if exam_schedule:
                with st.spinner("Crafting your personalized study strategy..."):
                    st.session_state['responses']["interactive_study_planner"] = interactive_study_planner(exam_schedule)
            else:
                st.session_state['responses']["interactive_study_planner"] = "Please enter your exam schedule to get a customized study plan! 📚"
    
    st.markdown("<div class='response-area'>", unsafe_allow_html=True)
    st.markdown("### Your Personalized Study Plan:")
    st.markdown(st.session_state['responses']["interactive_study_planner"])
    st.markdown("</div>", unsafe_allow_html=True)

elif selected_task == "❓ Real-Time Q&A Support":
        st.markdown("""
        <div class='tool-card'>
            <h3><span class='emoji'>🤔</span>Ask Anything, Anytime</h3>
            <p>Got a burning question? Our AI is ready to provide instant, accurate answers to fuel your curiosity!</p>
        </div>
        """, unsafe_allow_html=True)
        question = st.text_input("What's your question? 🧐")
        col1, col2 = st.columns([1, 3])
        with col1:
            if st.button("🧹 Clear"):
                st.session_state['responses']["real_time_qa_support"] = ""
                st.rerun()
        with col2:
            if st.button("💡 Get Answer"):
                if question:
                    with st.spinner("Searching the depths of knowledge for your answer..."):
                        st.session_state['responses']["real_time_qa_support"] = real_time_qa_support(question)
                else:
                    st.session_state['responses']["real_time_qa_support"] = "Please ask a question to unlock the wisdom of our AI! 🔓"
        
        st.markdown("<div class='response-area'>", unsafe_allow_html=True)
        st.markdown("### Your Answer:")
        st.markdown(st.session_state['responses']["real_time_qa_support"])
        st.markdown("</div>", unsafe_allow_html=True)

elif selected_task == "💬 Mental Health Check-In":
        st.markdown("""
        <div class='tool-card'>
            <h3><span class='emoji'>🌈</span>Your Emotional Wellness Companion</h3>
            <p>Share how you're feeling, and let our AI provide supportive advice and resources for your mental well-being.</p>
        </div>
        """, unsafe_allow_html=True)
        feelings = st.text_input("How are you feeling today? 💭")
        col1, col2 = st.columns([1, 3])
        with col1:
            if st.button("🧹 Clear"):
                st.session_state['responses']["mental_health_check_in"] = ""
                st.rerun()
        with col2:
            if st.button("🤗 Get Support"):
                if feelings:
                    with st.spinner("Analyzing your emotions with care and empathy..."):
                        st.session_state['responses']["mental_health_check_in"] = mental_health_check_in(feelings)
                else:
                    st.session_state['responses']["mental_health_check_in"] = "Please share how you're feeling so we can offer personalized support. 💖"
        
        st.markdown("<div class='response-area'>", unsafe_allow_html=True)
        st.markdown("### Your Personalized Support:")
        st.markdown(st.session_state['responses']["mental_health_check_in"])
        st.markdown("</div>", unsafe_allow_html=True)

    # Animated background
    st.markdown("""
    <div class="stApp">
        <div class="animated-bg"></div>
    </div>
    """, unsafe_allow_html=True)

    # Footer with contact information
    st.markdown("""
    <div class="footer">
        <a href="https://github.com/muhammadibrahim313" target="_blank"><i class="fab fa-github"></i> GitHub</a>
        <a href="https://www.linkedin.com/in/muhammad-ibrahim-qasmi-9876a1297/" target="_blank"><i class="fab fa-linkedin"></i> LinkedIn</a>
        <a href="https://github.com/Ahmad-Fakhar" target="_blank"><i class="fab fa-github"></i> Partner's GitHub</a>
        <a href="https://www.linkedin.com/in/ahmad-fakhar-357742258/" target="_blank"><i class="fab fa-linkedin"></i> Partner's LinkedIn</a>
    </div>
    """, unsafe_allow_html=True)

    # Add some playful elements
    st.balloons()

    # Display a random inspirational quote
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
