import streamlit as st
import together
import os

# Set page configuration
st.set_page_config(page_title="Together AI Code Generator", layout="wide")

# Set API key from environment variable or secrets
try:
    # Try to get from Streamlit secrets (for Streamlit Cloud)
    together.api_key = st.secrets["TOGETHER_API_KEY"]
except:
    # Try to get from environment variable (for local development)
    together.api_key = os.environ.get("TOGETHER_API_KEY")
    
    # Check if API key is available
    if not together.api_key:
        st.error("API key not found. Please add your Together AI API key to the .streamlit/secrets.toml file or as an environment variable.")
        st.stop()

# Main app
st.title("Python Code Generator with Together AI")
st.write("Enter a description of the Python code you want to generate:")

# User input
user_input = st.text_area("Description", height=150)

# Generate button
if st.button("Generate Code"):
    if user_input:
        try:
            with st.spinner("Generating code..."):
                # API call to Together AI using a serverless model
                response = together.Complete.create(
                    prompt=f"Write Python code for the following task: {user_input}\nProvide only the code with no explanations:\n```python\n",
                    model="mistralai/Mistral-7B-Instruct-v0.2",
                    max_tokens=1000,
                    temperature=0.2,
                    stop=["```"]
                )
                
                # Extract the generated code
                generated_code = response['output']['text'].strip()
                
                # Display the generated code
                st.subheader("Generated Python Code:")
                st.code(generated_code, language="python")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.info("Please check your API key and internet connection.")
    else:
        st.error("Please enter a description first.")

# Footer
st.markdown("---")
st.markdown("Powered by Together AI and Streamlit") 