import streamlit as st
import os
from groq import Groq
from streamlit.components.v1 import html
import random

# Set up page configuration
st.set_page_config(page_title="EduNexus 🚀", page_icon="🚀", layout="wide")

# Initialize Groq client
api_key = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=api_key)
MODEL_NAME = "llama3-8b-8192"

def call_groq_api(prompt):
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=MODEL_NAME,
            temperature=0.7,
            max_tokens=2048
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Tool functions with enhanced prompts
def personalized_learning_assistant(topic):
    prompt = f"""Create a detailed personalized learning plan for: {topic}
    Include:
    1. Learning objectives
    2. Step-by-step learning path
    3. Recommended resources
    4. Practice exercises
    5. Milestones and assessments
    Format the response with clear sections and bullet points."""
    return call_groq_api(prompt)

def ai_coding_mentor(code_snippet):
    prompt = f"""Analyze this code and provide:
    1. Code review with improvements
    2. Best practices suggestions
    3. Potential bugs or issues
    4. Performance optimization tips
    5. Security considerations
    Code to review:
    {code_snippet}"""
    return call_groq_api(prompt)

def smart_document_summarizer(document_text):
    prompt = f"""Provide a comprehensive summary of this document including:
    1. Main points and key takeaways
    2. Important details and facts
    3. Conclusions or recommendations
    4. Structure and organization analysis
    Document text:
    {document_text}"""
    return call_groq_api(prompt)

def interactive_study_planner(exam_schedule):
    prompt = f"""Create a detailed study plan based on this exam schedule:
    1. Daily study schedule
    2. Topic prioritization
    3. Review sessions
    4. Break times and rest periods
    5. Practice test schedule
    Exam schedule:
    {exam_schedule}"""
    return call_groq_api(prompt)

def real_time_qa_support(question):
    prompt = f"""Provide a detailed answer to this question:
    1. Core explanation
    2. Examples or illustrations
    3. Additional context
    4. Related concepts
    5. Sources for further reading
    Question:
    {question}"""
    return call_groq_api(prompt)

def mental_health_check_in(feelings):
    prompt = f"""Provide empathetic support and advice for someone feeling:
    1. Validation and understanding
    2. Coping strategies
    3. Self-care suggestions
    4. Professional resources if needed
    5. Positive affirmations
    Feelings expressed:
    {feelings}"""
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

# CSS styles
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
    
    .response-card {
        background-color: rgba(255, 255, 255, 0.15);
        border-radius: 15px;
        padding: 1.5rem;
        margin-top: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .emoji {
        font-size: 2rem;
        margin-right: 0.5rem;
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
    
    .stButton > button {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        color: white;
        border: none;
        border-radius: 30px;
        padding: 0.6rem 1.2rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    .quote-card {
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 1rem;
        margin-top: 1rem;
        font-style: italic;
    }
    </style>
    """

def display_learning_assistant():
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
                st.session_state['responses']["personalized_learning_assistant"] = "Please enter a topic to get started! 📚"
    
    if st.session_state['responses']["personalized_learning_assistant"]:
        st.markdown("<div class='response-card'>", unsafe_allow_html=True)
        st.markdown("### Your Personalized Learning Plan:")
        st.markdown(st.session_state['responses']["personalized_learning_assistant"])
        st.markdown("</div>", unsafe_allow_html=True)

def display_coding_mentor():
    st.markdown("""
    <div class='tool-card'>
        <h3><span class='emoji'>💻</span>AI Code Review</h3>
        <p>Get expert feedback on your code with suggestions for improvements and best practices!</p>
    </div>
    """, unsafe_allow_html=True)
    
    code_snippet = st.text_area("Paste your code here for review 👨‍💻", height=200)
    col1, col2 = st.columns([1, 3])
    
    with col1:
        if st.button("🧹 Clear"):
            st.session_state['responses']["ai_coding_mentor"] = ""
            st.rerun()
    with col2:
        if st.button("🚀 Review Code"):
            if code_snippet:
                with st.spinner("Reviewing your code..."):
                    st.session_state['responses']["ai_coding_mentor"] = ai_coding_mentor(code_snippet)
            else:
                st.session_state['responses']["ai_coding_mentor"] = "Please paste your code to get started! 📜"
    
    if st.session_state['responses']["ai_coding_mentor"]:
        st.markdown("<div class='response-card'>", unsafe_allow_html=True)
        st.markdown("### Code Review Feedback:")
        st.markdown(st.session_state['responses']["ai_coding_mentor"])
        st.markdown("</div>", unsafe_allow_html=True)

def display_document_summarizer():
    st.markdown("""
    <div class='tool-card'>
        <h3><span class='emoji'>📄</span>Smart Document Summarizer</h3>
        <p>Paste your document text here, and let our AI provide a concise summary!</p>
    </div>
    """, unsafe_allow_html=True)
    
    document_text = st.text_area("Paste your document text here 📖", height=200)
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
                st.session_state['responses']["smart_document_summarizer"] = "Please paste your document text to get started! 📝"
    
    if st.session_state['responses']["smart_document_summarizer"]:
        st.markdown("<div class='response-card'>", unsafe_allow_html=True)
        st.markdown("### Document Summary:")
        st.markdown(st.session_state['responses']["smart_document_summarizer"])
        st.markdown("</div>", unsafe_allow_html=True)

def display_study_planner():
    st.markdown("""
    <div class='tool-card'>
        <h3><span class='emoji'>📅</span>Interactive Study Planner</h3>
        <p>Input your exam schedule, and our AI will create a tailored study plan!</p>
    </div>
    """, unsafe_allow_html=True)
    
    exam_schedule = st.text_area("Enter your exam schedule here (Subject, Date) 📅", height=200)
    col1, col2 = st.columns([1, 3])
    
    with col1:
        if st.button("🧹 Clear"):
            st.session_state['responses']["interactive_study_planner"] = ""
            st.rerun()
    with col2:
        if st.button("🚀 Generate Study Plan"):
            if exam_schedule:
                with st.spinner("Creating your study plan..."):
                    st.session_state['responses']["interactive_study_planner"] = interactive_study_planner(exam_schedule)
            else:
                st.session_state['responses']["interactive_study_planner"] = "Please enter your exam schedule to get started! 📆"
    
    if st.session_state['responses']["interactive_study_planner"]:
        st.markdown("<div class='response-card'>", unsafe_allow_html=True)
        st.markdown("### Your Study Plan:")
        st.markdown(st.session_state['responses']["interactive_study_planner"])
        st.markdown("</div>", unsafe_allow_html=True)

def display_qa_support():
    st.markdown("""
    <div class='tool-card'>
        <h3><span class='emoji'>❓</span>Real-Time Q&A Support</h3>
        <p>Ask any question and get instant, informative answers!</p>
    </div>
    """, unsafe_allow_html=True)
    
    question = st.text_input("What question do you have? 🧐")
    col1, col2 = st.columns([1, 3])
    
    with col1:
        if st.button("🧹 Clear"):
            st.session_state['responses']["real_time_qa_support"] = ""
            st.rerun()
    with col2:
        if st.button("🚀 Get Answer"):
            if question:
                with st.spinner("Fetching your answer..."):
                    st.session_state['responses']["real_time_qa_support"] = real_time_qa_support(question)
            else:
                st.session_state['responses']["real_time_qa_support"] = "Please enter your question to get started! 🤔"
    
    if st.session_state['responses']["real_time_qa_support"]:
        st.markdown("<div class='response-card'>", unsafe_allow_html=True)
        st.markdown("### Your Answer:")
        st.markdown(st.session_state['responses']["real_time_qa_support"])
        st.markdown("</div>", unsafe_allow_html=True)

def display_mental_health_checkin():
    st.markdown("""
    <div class='tool-card'>
        <h3><span class='emoji'>🧠</span>Mental Health Check-In</h3>
        <p>Express your feelings, and receive supportive advice!</p>
    </div>
    """, unsafe_allow_html=True)
    
    feelings = st.text_area("How are you feeling today? 🥲", height=200)
    col1, col2 = st.columns([1, 3])
    
    with col1:
        if st.button("🧹 Clear"):
            st.session_state['responses']["mental_health_check_in"] = ""
            st.rerun()
    with col2:
        if st.button("🚀 Get Support"):
            if feelings:
                with st.spinner("Providing support..."):
                    st.session_state['responses']["mental_health_check_in"] = mental_health_check_in(feelings)
            else:
                st.session_state['responses']["mental_health_check_in"] = "Please share your feelings to get started! 💬"
    
    if st.session_state['responses']["mental_health_check_in"]:
        st.markdown("<div class='response-card'>", unsafe_allow_html=True)
        st.markdown("### Support Response:")
        st.markdown(st.session_state['responses']["mental_health_check_in"])
        st.markdown("</div>", unsafe_allow_html=True)

# Display CSS styles
html(load_css(), height=0)

# App title
st.markdown("<h1 class='main-title'>Welcome to EduNexus 🚀</h1>", unsafe_allow_html=True)

# Display each tool
display_learning_assistant()
display_coding_mentor()
display_document_summarizer()
display_study_planner()
display_qa_support()
display_mental_health_checkin()

# Footer
st.markdown("""
<div class='footer'>
    <p>Created with ❤️ by Your Name</p>
    <a href="#">Privacy Policy</a>
    <a href="#">Terms of Service</a>
</div>
""", unsafe_allow_html=True)
