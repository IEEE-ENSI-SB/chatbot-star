# 🚀 **Flask Chatbot with Gemini API**

Welcome to the **Flask Chatbot** powered by **Gemini API**! 🤖✨ This simple web application allows you to chat with an intelligent bot that can understand and respond to your messages. You can also listen to the responses as speech! 🎤👂

## 🔧 **Setup Instructions**

### 1. **Clone the Repository**

Start by cloning the repository to your local machine:

```bash
git clone <repository_url>
cd <project_directory>
```

### 2. **Set up a Virtual Environment**

Next, create a virtual environment to manage your dependencies. For **Windows**:

```bash
python -m venv venv
venv\Scripts\activate
```

For **macOS/Linux**:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. **Install Dependencies**

Install the necessary libraries by running:

```bash
pip install -r requirements.txt
```

### 4. **Set Your Gemini API Key**

To interact with the Gemini API, you need to set your API key. For **Windows (PowerShell)**, use this command:

```bash
$env:GEMINI_API_KEY="your-api-key-here"
```

For **macOS/Linux**, use:

```bash
export GEMINI_API_KEY="your-api-key-here"
```

### 5. **Run the Application**

Start the Flask app and open it in your browser:

```bash
python app.py
```

The app will be live at `http://127.0.0.1:5000`.

