import streamlit as st
import together
import os
from streamlit_lottie import st_lottie
import requests
import json

# Set custom theme and page configuration
st.set_page_config(
    page_title="AI Code Generator", 
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        background-color: #f5f7ff;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .stTextArea textarea {
        border-radius: 10px;
        border: 1px solid #4361ee;
    }
    .stButton>button {
        border-radius: 20px;
        background-color: #4361ee;
        color: white;
        font-weight: bold;
        padding: 0.5rem 2rem;
        border: none;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #3a56d4;
        box-shadow: 0 4px 8px rgba(67, 97, 238, 0.3);
        transform: translateY(-2px);
    }
    h1 {
        color: #3a0ca3;
        font-weight: 800;
    }
    .footer {
        text-align: center;
        font-size: 0.8rem;
        color: #555;
        margin-top: 3rem;
    }
    .code-header {
        color: #3a0ca3;
        font-weight: 600;
        margin-top: 2rem;
    }
    .subtitle {
        color: #4361ee;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    .stSpinner {
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Function to load Lottie animations
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

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

# Layout with columns
col1, col2 = st.columns([2, 1])

with col1:
    st.title("Python Code Generator")
    st.markdown('<p class="subtitle">Powered by Together AI & Streamlit</p>', unsafe_allow_html=True)
    
    # User input
    st.markdown("##### What code would you like to generate today?")
    user_input = st.text_area("", height=150, 
                              placeholder="E.g., Create a function that sorts a list of dictionaries by a specific key")

with col2:
    # Load and display Lottie animation
    lottie_coding = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_fcfjwiyb.json")
    if lottie_coding:
        st_lottie(lottie_coding, height=250, key="coding")
    else:
        st.image("https://cdn-icons-png.flaticon.com/512/6213/6213731.png", width=200)

# Generate button - centered
col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
with col_btn2:
    generate_button = st.button("✨ Generate Code")

# Code generation
if generate_button:
    if user_input:
        try:
            with st.spinner("🧠 AI is crafting your code..."):
                # API call to Together AI using a serverless model
                response = together.Complete.create(
                    prompt=f"Write Python code for the following task: {user_input}\nProvide only the code with no explanations:\n```python\n",
                    model="mistralai/Mistral-7B-Instruct-v0.2",
                    max_tokens=1000,
                    temperature=0.2,
                    stop=["```"]
                )
                
                # Extract the generated code - handle different response formats
                if isinstance(response, dict):
                    if 'output' in response and 'text' in response['output']:
                        generated_code = response['output']['text'].strip()
                    elif 'choices' in response and len(response['choices']) > 0:
                        generated_code = response['choices'][0].get('text', '').strip()
                    elif 'generated_text' in response:
                        generated_code = response['generated_text'].strip()
                    else:
                        # Try a different access pattern based on Together AI docs
                        generated_code = response.get('text', str(response)).strip()
                else:
                    # If response is not a dict, convert to string
                    generated_code = str(response).strip()
                
                # Display the generated code
                st.markdown('<p class="code-header">📄 Generated Python Code:</p>', unsafe_allow_html=True)
                st.code(generated_code, language="python")
                
                # Copy button
                st.download_button(
                    label="📋 Copy to Clipboard",
                    data=generated_code,
                    file_name="generated_code.py",
                    mime="text/plain",
                )
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.info("Please check your API key and internet connection.")
            
            # Display more detailed error information for debugging
            with st.expander("View error details"):
                import traceback
                st.code(traceback.format_exc(), language="python")
    else:
        st.warning("⚠️ Please enter a description first.")

# Footer
st.markdown('<div class="footer">Created with ❤️ by your friendly neighborhood Data Analyst Patrick Scott | Python Code Generator powered by Together AI and Streamlit</div>', unsafe_allow_html=True) 