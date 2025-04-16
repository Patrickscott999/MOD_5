# Together AI Streamlit App

A Streamlit application that uses Together AI's API to generate Python code based on text descriptions.

## Setup

1. Clone this repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up your Together AI API key as an environment variable:
   ```
   export TOGETHER_API_KEY=your_api_key_here
   ```

## Running Locally

Run the app with:
```
streamlit run app.py
```

## Deployment

This app can be deployed on Streamlit Cloud:

1. Connect your GitHub account to Streamlit Cloud
2. Deploy the app by selecting this repository
3. Set the main file path to `app.py`
4. Add your Together AI API key in the Secrets Management tab:
   - Key: `TOGETHER_API_KEY`
   - Value: Your actual API key

## Usage

1. Enter a description of the Python code you want to generate
2. Click "Generate Code"
3. View the generated Python code 