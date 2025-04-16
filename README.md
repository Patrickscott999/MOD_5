# 💻 AI Python Code Generator

![GitHub last commit](https://img.shields.io/github/last-commit/Patrickscott999/MOD_5)
![GitHub repo size](https://img.shields.io/github/repo-size/Patrickscott999/MOD_5)
![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-FF4B4B)
![Together AI](https://img.shields.io/badge/Together_AI-Powered-blueviolet)

## 🚀 Overview

A modern Streamlit application that leverages Together AI's powerful LLMs to generate Python code based on text descriptions. Simply enter what you want your code to do, and the AI will craft a solution for you!

## ✨ Features

- 🧠 **AI-Powered Code Generation** - Utilizes Mistral-7B-Instruct for high-quality Python code
- 🎨 **Modern UI/UX** - Sleek interface with animations and responsive design
- 📋 **One-Click Copy** - Instantly copy generated code to your clipboard
- 🔍 **Detailed Error Handling** - Clear error messages and debugging information
- 🌐 **Cloud Deployment Ready** - Easily deploy on Streamlit Cloud

## 🛠️ Installation

```bash
# Clone this repository
git clone https://github.com/Patrickscott999/MOD_5.git

# Navigate to the project directory
cd MOD_5

# Install dependencies
pip install -r requirements.txt

# Set your Together AI API key
# For Linux/Mac
export TOGETHER_API_KEY=your_api_key_here

# For Windows
set TOGETHER_API_KEY=your_api_key_here
```

## 🚀 Usage

```bash
streamlit run app.py
```

Then navigate to `http://localhost:8501` in your browser.

## 🔧 Configuration

To use your own Together AI API key:

1. Create an account at [Together AI](https://together.ai)
2. Generate an API key
3. For local development:
   - Create `.streamlit/secrets.toml` with:
     ```toml
     TOGETHER_API_KEY = "your_key_here"
     ```
4. For Streamlit Cloud:
   - Add the key in the Secrets management section

## 📝 Example Prompts

- "Create a function to convert CSV to JSON"
- "Write code to scrape weather data from a website"
- "Build a decorator that measures function execution time"
- "Implement a binary search algorithm"

## 🌟 Roadmap

- [ ] Support for multiple programming languages
- [ ] Code optimization suggestions
- [ ] User accounts to save generated code
- [ ] Themed code templates
- [ ] Integration with GitHub Gists

## 📜 License

MIT License - see LICENSE file for details.

## 🙏 Credits

Created with ❤️ by your friendly neighborhood Data Analyst Patrick Scott

Powered by [Together AI](https://together.ai) and [Streamlit](https://streamlit.io) 