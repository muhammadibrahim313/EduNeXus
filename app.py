import os
import streamlit as st
from groq import Groq

# Set the Groq API key
api_key = st.secrets["GROQ_API_KEY"]

# Initialize the Groq client using the API key
client = Groq(api_key=api_key)

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
        "Explain quantum mechanics with a real-world example.",
        "Describe general relativity and its significance.",
        "Provide a simple explanation of machine learning and its applications."
    ]
    prompt = f"Here are some example explanations:\n\n{examples}\n\nNow, explain the topic: {topic}. Provide a detailed, yet simple explanation with a practical example."
    return call_groq_api(prompt)

def ai_coding_mentor(code_snippet):
    examples = [
        "Review this code snippet for optimization opportunities:\n\nCode: 'for i in range(10): print(i)'\nSuggestion: Use list comprehension for more efficient code.",
        "Analyze this code snippet for best practices:\n\nCode: 'def add(a, b): return a + b'\nSuggestion: Include type hints to improve readability and maintainability."
    ]
    prompt = f"Here are some code review examples:\n\n{examples}\n\nReview the following code snippet and provide suggestions for improvement:\n{code_snippet}. Include any potential issues or improvements."
    return call_groq_api(prompt)

def smart_document_summarizer(document_text):
    examples = [
        "Summarize this text:\n\nText: 'Quantum computing represents a revolutionary approach to computing that leverages quantum mechanics.'\nSummary: 'Quantum computing uses quantum mechanics to advance computing technology.'",
        "Create a summary for this passage:\n\nText: 'The rise of electric vehicles is a major step towards reducing global carbon emissions and combating climate change.'\nSummary: 'Electric vehicles help reduce carbon emissions and fight climate change.'"
    ]
    prompt = f"Here are some document summarization examples:\n\n{examples}\n\nSummarize the following document text concisely:\n{document_text}. Focus on capturing the main points clearly."
    return call_groq_api(prompt)

def interactive_study_planner(exam_schedule):
    examples = [
        "Generate a study plan for a schedule with multiple exams in a week:\n\nSchedule: '3 exams in one week'\nPlan: 'Allocate 2 hours per subject each day, with review sessions on weekends.'",
        "Create a study plan for preparing for exams over a period of 2 weeks:\n\nSchedule: 'Exams in 2 weeks'\nPlan: 'Prioritize subjects based on difficulty and importance, with daily reviews and mock tests.'"
    ]
    prompt = f"Here are some study planning examples:\n\n{examples}\n\nCreate a tailored study plan based on the following schedule:\n{exam_schedule}. Include daily study goals and break times."
    return call_groq_api(prompt)

def real_time_qa_support(question):
    examples = [
        "Provide an answer to this question:\n\nQuestion: 'What is Newton's third law of motion?'\nAnswer: 'Newton's third law states that for every action, there is an equal and opposite reaction.'",
        "Explain this concept:\n\nQuestion: 'What is the principle of conservation of energy?'\nAnswer: 'The principle of conservation of energy states that energy cannot be created or destroyed, only transformed from one form to another.'"
    ]
    prompt = f"Here are some examples of answers to academic questions:\n\n{examples}\n\nAnswer the following question:\n{question}. Provide a clear and comprehensive explanation."
    return call_groq_api(prompt)

def mental_health_check_in(feelings):
    examples = [
        "Offer advice for managing exam stress:\n\nFeeling: 'Stressed about upcoming exams'\nAdvice: 'Develop a study schedule, take regular breaks, and practice relaxation techniques.'",
        "Provide support for feeling overwhelmed:\n\nFeeling: 'Feeling overwhelmed with coursework'\nAdvice: 'Break tasks into smaller, manageable parts and seek support from peers or a counselor.'"
    ]
    prompt = f"Here are some examples of mental health advice:\n\n{examples}\n\nProvide advice based on the following feeling:\n{feelings}. Offer practical suggestions for improving well-being."
    return call_groq_api(prompt)

# Define Streamlit app
st.set_page_config(page_title="EduNexus", page_icon=":book:", layout="wide")

# Add custom styling using Streamlit
st.markdown("""
    <style>
    .css-1o7k8tt { 
        background-color: #282c34; 
        color: #ffffff; 
    }
    .css-1o7k8tt h1 {
        color: #61dafb;
    }
    .stButton {
        background-color: #61dafb;
        color: #000000;
        border-radius: 12px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton:hover {
        background-color: #4fa3d1;
    }
    .stTextInput, .stTextArea {
        border: 1px solid #61dafb;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# Define function to clear all inputs
def clear_chat():
    st.session_state['personalized_learning_assistant'] = ""
    st.session_state['ai_coding_mentor'] = ""
    st.session_state['smart_document_summarizer'] = ""
    st.session_state['interactive_study_planner'] = ""
    st.session_state['real_time_qa_support'] = ""
    st.session_state['mental_health_check_in'] = ""

# Add Clear Chat button
if st.button("Clear All", key="clear_button"):
    clear_chat()

# Navigation sidebar
st.sidebar.title("EduNexus Tools")
selected_tool = st.sidebar.radio(
    "Select a tool",
    ("Personalized Learning Assistant", "AI Coding Mentor", "Smart Document Summarizer",
     "Interactive Study Planner", "Real-Time Q&A Support", "Mental Health Check-In")
)

# Display tool based on selection
if selected_tool == "Personalized Learning Assistant":
    st.header("Personalized Learning Assistant")
    with st.form(key="learning_form"):
        topic_input = st.text_input("Enter a topic you want to learn about", placeholder="e.g., Quantum Mechanics")
        submit_button = st.form_submit_button("Get Explanation")
        if submit_button:
            explanation = personalized_learning_assistant(topic_input)
            st.write(explanation)

elif selected_tool == "AI Coding Mentor":
    st.header("AI Coding Mentor")
    with st.form(key="coding_form"):
        code_input = st.text_area("Enter your code snippet", placeholder="e.g., def add(a, b): return a + b")
        submit_button = st.form_submit_button("Review Code")
        if submit_button:
            review = ai_coding_mentor(code_input)
            st.write(review)

elif selected_tool == "Smart Document Summarizer":
    st.header("Smart Document Summarizer")
    with st.form(key="summarizer_form"):
        document_input = st.text_area("Enter the text you want to summarize", placeholder="Paste document text here...")
        submit_button = st.form_submit_button("Summarize Document")
        if submit_button:
            summary = smart_document_summarizer(document_input)
            st.write(summary)

elif selected_tool == "Interactive Study Planner":
    st.header("Interactive Study Planner")
    with st.form(key="planner_form"):
        schedule_input = st.text_area("Enter your exam schedule", placeholder="e.g., 3 exams in 1 week")
        submit_button = st.form_submit_button("Generate Study Plan")
        if submit_button:
            study_plan = interactive_study_planner(schedule_input)
            st.write(study_plan)

elif selected_tool == "Real-Time Q&A Support":
    st.header("Real-Time Q&A Support")
    with st.form(key="qa_form"):
        question_input = st.text_input("Ask any academic question", placeholder="e.g., What is Newton's second law?")
        submit_button = st.form_submit_button("Get Answer")
        if submit_button:
            answer = real_time_qa_support(question_input)
            st.write(answer)

elif selected_tool == "Mental Health Check-In":
    st.header("Mental Health Check-In")
    with st.form(key="checkin_form"):
        feelings_input = st.text_area("How are you feeling?", placeholder="e.g., Stressed about exams")
        submit_button = st.form_submit_button("Check In")
        if submit_button:
            advice = mental_health_check_in(feelings_input)
            st.write(advice)
