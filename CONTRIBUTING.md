# 🤝 Contributing to AI Python Code Generator

First off, thank you for considering contributing to the AI Python Code Generator! It's people like you that make this tool better for everyone.

## 📋 Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md). Please read it before contributing.

## 🚀 How Can I Contribute?

### 🐛 Reporting Bugs

This section guides you through submitting a bug report. Following these guidelines helps maintainers understand your report, reproduce the behavior, and find related reports.

- Use the bug report template when creating an issue
- Include detailed steps to reproduce the bug
- Describe the behavior you observed and what you expected to see
- Include screenshots if possible
- Mention your environment (OS, browser, Python version, etc.)

### 💡 Suggesting Features

This section guides you through submitting an enhancement suggestion, including completely new features and minor improvements to existing functionality.

- Use the feature request template when creating an issue
- Provide a clear description of the suggested enhancement
- Include any relevant examples or mockups
- Explain why this enhancement would be useful to users

### 💻 Code Contributions

#### 🌱 Setting Up the Development Environment

1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/MOD_5.git`
3. Create a virtual environment: `python -m venv venv`
4. Activate the environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`
6. Create a `.streamlit/secrets.toml` file with your Together AI API key:
   ```toml
   TOGETHER_API_KEY = "your_key_here"
   ```

#### 🔄 Pull Request Process

1. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bugfix-name
   ```

2. Make your changes, adhering to the code style of the project

3. Run the linting checks:
   ```bash
   flake8 .
   black .
   ```

4. Commit your changes using a descriptive commit message:
   ```bash
   git commit -m "Add feature: your feature description"
   ```

5. Push to your branch:
   ```bash
   git push origin feature/your-feature-name
   ```

6. Submit a pull request to the `main` branch of the original repository

7. Wait for review and address any feedback

## 🎨 Style Guides

### 💻 Code Style

- Follow PEP 8 style guidelines for Python code
- Use meaningful variable and function names
- Include docstrings for functions and classes
- Keep functions focused and concise

### 📝 Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests after the first line

## 🙏 Thank You

Your contributions to open source, large or small, make projects like this possible. Thank you for taking the time to contribute. 