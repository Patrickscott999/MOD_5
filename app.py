import streamlit as st
import together
import os

# Set page configuration
st.set_page_config(page_title="Together AI Code Generator", layout="wide")

# Set API key from environment variable
together.api_key = os.environ.get("TOGETHER_API_KEY")

# Main app
st.title("Python Code Generator with Together AI")
st.write("Enter a description of the Python code you want to generate:")

# User input
user_input = st.text_area("Description", height=150)

# Generate button
if st.button("Generate Code"):
    if user_input:
        with st.spinner("Generating code..."):
            # API call to Together AI
            response = together.Complete.create(
                prompt=f"Write Python code for the following task: {user_input}\nProvide only the code with no explanations:\n```python\n",
                model="togethercomputer/llama-2-70b",
                max_tokens=1000,
                temperature=0.2,
                stop=["```"]
            )
            
            # Extract the generated code
            generated_code = response['output']['text'].strip()
            
            # Display the generated code
            st.subheader("Generated Python Code:")
            st.code(generated_code, language="python")
    else:
        st.error("Please enter a description first.")

# Footer
st.markdown("---")
st.markdown("Powered by Together AI and Streamlit") 