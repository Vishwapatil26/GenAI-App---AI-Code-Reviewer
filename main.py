import streamlit as st
import google.generativeai as genai

# Configure Google Gemini API
genai.configure(api_key="Your Gemini API Key")

def analyze_code(code):
    """Send the user-submitted Python code to Gemini API for analysis."""
    prompt = f"""
    Analyze the given Python code for potential bugs, errors, inefficiencies, or areas of improvement. 
    - Identify syntax, logical, and performance-related issues. 
    - Provide a concise yet detailed explanation of the problems found. 
    - Suggest well-documented corrected version of the code. 
    - Ensure the response is precise, accurate, and formatted for readability.

    Code:
    ```python
    {code}
    ```
    """
    
    model = genai.GenerativeModel("gemini-pro")  # Use appropriate Gemini model
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
st.title("Python Code Reviewer")
st.write("Submit your Python code for bug detection and suggestions.")

# User input field for Python code
code_input = st.text_area("Enter your Python code here:", height=200)

if st.button("Analyze Code"):
    if code_input.strip():
        with st.spinner("Analyzing your code..."):
            review_result = analyze_code(code_input)
            st.subheader("Code Review & Suggestions")
            st.write(review_result)
    else:
        st.warning("Please enter some Python code before submitting.")
