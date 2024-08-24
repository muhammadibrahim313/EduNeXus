import os
import streamlit as st
from groq import Groq

# Set the Groq API key

os.environ["GROQ_API_KEY"] == st.secrets["API_KEY"]

# Initialize Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Define the LLaMA model to be used
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

# Define functions for each tool
def personalized_learning_assistant(topic):
    examples = [
        "Explain quantum mechanics. Example: Quantum mechanics is the study of particles at the atomic level.",
        "Explain general relativity. Example: General relativity describes gravity as a curvature in space-time.",
        "Explain machine learning. Example: Machine learning involves algorithms that improve through experience."
    ]
    prompt = f"Here are some examples of explanations:\n\n{examples}\n\nNow, explain the topic: {topic}"
    return call_groq_api(prompt)

def ai_coding_mentor(code_snippet):
    examples = [
        "Review the following code snippet:\n\nCode: 'for i in range(10): print(i)'\nSuggestion: Use list comprehension for cleaner code.",
        "Review this code:\n\nCode: 'def add(a, b): return a + b'\nSuggestion: Add type hints for better readability."
    ]
    prompt = f"Here are some examples of code reviews:\n\n{examples}\n\nReview the following code snippet:\n{code_snippet}"
    return call_groq_api(prompt)

def smart_document_summarizer(document_text):
    examples = [
        "Summarize the following text:\n\nText: 'Quantum computing is a rapidly evolving field with potential to revolutionize technology.'\nSummary: 'Quantum computing could transform technology.'",
        "Summarize this passage:\n\nText: 'The global climate change crisis necessitates urgent action to reduce carbon emissions.'\nSummary: 'Immediate action is needed to tackle climate change.'"
    ]
    prompt = f"Here are some examples of summaries:\n\n{examples}\n\nSummarize this document:\n{document_text}"
    return call_groq_api(prompt)

def interactive_study_planner(exam_schedule):
    examples = [
        "Create a study plan based on this schedule:\n\nSchedule: '3 exams in a week'\nPlan: 'Study 2 hours per subject each day before the exam.'",
        "Generate a study plan for:\n\nSchedule: 'Exams in 2 weeks'\nPlan: 'Focus on subjects with more weight and review daily.'"
    ]
    prompt = f"Here are some examples of study plans:\n\n{examples}\n\nCreate a study plan for the following schedule:\n{exam_schedule}"
    return call_groq_api(prompt)

def real_time_qa_support(question):
    examples = [
        "Answer this question:\n\nQuestion: 'What is Newton's second law of motion?'\nAnswer: 'Newton's second law states that force equals mass times acceleration (F=ma).'",
        "Provide an explanation for:\n\nQuestion: 'What is photosynthesis?'\nAnswer: 'Photosynthesis is the process by which plants convert light energy into chemical energy.'"
    ]
    prompt = f"Here are some examples of Q&A responses:\n\n{examples}\n\nAnswer the following question:\n{question}"
    return call_groq_api(prompt)

def mental_health_check_in(feelings):
    examples = [
        "Provide advice for:\n\nFeeling: 'Stressed about exams'\nAdvice: 'Take breaks, get enough sleep, and manage your study time effectively.'",
        "Offer support for:\n\nFeeling: 'Feeling overwhelmed'\nAdvice: 'Consider relaxation techniques and seek support from friends or a counselor.'"
    ]
    prompt = f"Here are some examples of mental health advice:\n\n{examples}\n\nProvide advice for:\n{feelings}"
    return call_groq_api(prompt)

# Define Streamlit app
st.set_page_config(page_title="EduNexus", page_icon=":book:", layout="wide")

# Add custom CSS for neon and animated design
st.markdown("""
    <style>
    body {
        background: white;
        color: #e0e0e0;
        font-family: 'Arial', sans-serif;
        overflow-x: hidden;
    }
    .neon-text {
        font-size: 32px;
        color: #ff0081;
        text-shadow: ;
        margin-bottom: 20px;
    }
    .neon-border {
        border: 2px solid #ff0081;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 20px;
        box-shadow: 0 0 15px #ff0081;
    }
    .animated-button {
        animation: pulse 2s infinite;
        background-color: #ff0081;
        color: #000;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
        margin: 10px 0;
    }
    .animated-button:hover {
        background-color: #cc0077;
    }
    .input-container {
        margin-bottom: 20px;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    </style>
""", unsafe_allow_html=True)

# Title and introduction
st.title("EduNexus: The Ultimate AI-Powered Student Companion")
st.markdown("<div class='neon-text'>Welcome to EduNexus! Choose a tool below to get started.</div>", unsafe_allow_html=True)

# Define function to clear all inputs
def clear_chat():
    st.session_state['personalized_learning_assistant'] = ""
    st.session_state['ai_coding_mentor'] = ""
    st.session_state['smart_document_summarizer'] = ""
    st.session_state['interactive_study_planner'] = ""
    st.session_state['real_time_qa_support'] = ""
    st.session_state['mental_health_check_in'] = ""

# Add Clear Chat button using HTML
if st.button("Clear All", key="clear_button", help="Click to clear all inputs"):
    clear_chat()

# Personalized Learning Assistant
st.header("Personalized Learning Assistant")
with st.form(key="learning_form"):
    topic_input = st.text_input("Enter a topic you want to learn about", key="topic_input", placeholder="e.g., Quantum Mechanics")
    submit_button = st.form_submit_button("Generate Learning Material")
    if submit_button:
        if topic_input:
            st.write(personalized_learning_assistant(topic_input))
        else:
            st.write("Please enter a topic.")

# AI Coding Mentor
st.header("AI Coding Mentor")
with st.form(key="coding_form"):
    code_input = st.text_area("Paste your code snippet", key="code_input", placeholder="e.g., for i in range(10): print(i)")
    submit_button = st.form_submit_button("Get Coding Assistance")
    if submit_button:
        if code_input:
            st.write(ai_coding_mentor(code_input))
        else:
            st.write("Please paste your code snippet.")

# Smart Document Summarizer
st.header("Smart Document Summarizer")
with st.form(key="summary_form"):
    doc_input = st.text_area("Paste the text of the document", key="doc_input", placeholder="e.g., Quantum computing is...")
    submit_button = st.form_submit_button("Summarize Document")
    if submit_button:
        if doc_input:
            st.write(smart_document_summarizer(doc_input))
        else:
            st.write("Please paste the document text.")

# Interactive Study Planner
st.header("Interactive Study Planner")
with st.form(key="planner_form"):
    schedule_input = st.text_area("Enter your exam schedule", key="schedule_input", placeholder="e.g., 3 exams in 1 week")
    submit_button = st.form_submit_button("Generate Study Plan")
    if submit_button:
        if schedule_input:
            st.write(interactive_study_planner(schedule_input))
        else:
            st.write("Please enter your exam schedule.")

# Real-Time Q&A Support
st.header("Real-Time Q&A Support")
with st.form(key="qa_form"):
    question_input = st.text_input("Ask any academic question", key="question_input", placeholder="e.g., What is Newton's second law?")
    submit_button = st.form_submit_button("Get Answer")
    if submit_button:
        if question_input:
            st.write(real_time_qa_support(question_input))
        else:
            st.write("Please ask a question.")

# Mental Health Check-In
st.header("Mental Health Check-In")
with st.form(key="checkin_form"):
    feelings_input = st.text_area("How are you feeling?", key="feelings_input", placeholder="e.g., Stressed about exams")
    submit_button = st.form_submit_button("Check In")
    if submit_button:
        if feelings_input:
            st.write(mental_health_check_in(feelings_input))
        else:
            st.write("Please describe your feelings.")
