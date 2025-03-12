import streamlit as st
import re
import string

def check_password_strength(password):
    # Initialize score and feedback
    score = 0
    feedback = []
    
    # Check length
    if len(password) >= 8:
        score += 1
        feedback.append("✅ Good length")
    else:
        feedback.append("❌ Password should be at least 8 characters")
    
    # Check for uppercase
    if any(c.isupper() for c in password):
        score += 1
        feedback.append("✅ Contains uppercase letters")
    else:
        feedback.append("❌ Should contain uppercase letters")
    
    # Check for lowercase
    if any(c.islower() for c in password):
        score += 1
        feedback.append("✅ Contains lowercase letters")
    else:
        feedback.append("❌ Should contain lowercase letters")
    
    # Check for numbers
    if any(c.isdigit() for c in password):
        score += 1
        feedback.append("✅ Contains numbers")
    else:
        feedback.append("❌ Should contain numbers")
    
    # Check for special characters
    if any(c in string.punctuation for c in password):
        score += 1
        feedback.append("✅ Contains special characters")
    else:
        feedback.append("❌ Should contain special characters")
    
    return score, feedback

# Set page config
st.set_page_config(page_title="Password Strength Checker By Furqan Ali Khan", page_icon="🔒")

# Add custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTextInput > div > div > input {
        font-size: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.title("🔒 Password Strength Checker")
st.markdown("Check how strong your password is!")

# Password input
password = st.text_input("Enter your password", type="password")

if password:
    # Check password strength
    score, feedback = check_password_strength(password)
    
    # Display strength meter
    st.markdown("### Password Strength")
    progress = score / 5  # Convert score to percentage
    st.progress(progress)
    
    # Display strength level
    if score < 2:
        st.error("Weak Password")
    elif score < 4:
        st.warning("Moderate Password")
    else:
        st.success("Strong Password")
    
    # Display feedback
    st.markdown("### Feedback")
    for item in feedback:
        st.markdown(item)
    
    # Display score
    st.markdown(f"### Score: {score}/5")

# Add tips
with st.expander("Tips for a Strong Password"):
    st.markdown("""
    - Use at least 8 characters
    - Include uppercase and lowercase letters
    - Include numbers
    - Include special characters (!@#$%^&*)
    - Avoid common words or phrases
    - Don't use personal information
    """)
