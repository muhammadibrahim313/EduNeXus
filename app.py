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
