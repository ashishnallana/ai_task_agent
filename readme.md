# ⚡ AI Task Agent

A powerful AI-driven task management system powered by Groq's LLaMA model and built with Gradio. Manage your tasks using natural language!

## 🎯 Features

- **Natural Language Processing**: Add, edit, delete, and manage tasks using conversational AI
- **Task Management**: Full CRUD operations on tasks with due dates and time tracking
- **Status Tracking**: Mark tasks as pending or completed
- **Web UI**: User-friendly Gradio interface for easy interaction
- **Persistent Storage**: Tasks stored in JSON database
- **Smart Agent**: Groq-powered CodeAgent that understands task-related requests

## 🛠 Tech Stack

- **LLM**: Groq (LLaMA 3.3 70B Versatile)
- **Agent Framework**: smolagents CodeAgent
- **Frontend**: Gradio
- **Backend**: Python
- **Storage**: JSON (tasks.json)

## 📋 Available Tools

The AI agent has access to the following tools:

- **`add_task`**: Add a new task with name, due date, and time
- **`list_tasks`**: View all current tasks with their IDs and status
- **`edit_task`**: Modify an existing task's details
- **`delete_task`**: Remove a task from the database
- **`update_task_status`**: Mark a task as completed or pending

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Groq API Key (get it from [https://console.groq.com](https://console.groq.com))

### Installation

1. **Clone or navigate to the project directory**

   ```bash
   cd ai_task_agent
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows
   # or
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

### Usage

**Start the web application:**

```bash
python app.py
```

The Gradio interface will launch at `http://localhost:7860`

### Example Requests

Try these natural language commands:

- _"Add a task to complete DSA at 6pm tomorrow"_
- _"Remind me to revise DBMS on the 31st of March"_
- _"Mark task 1 as completed"_
- _"Delete task 2"_
- _"Show me all my tasks"_
- _"Edit task 1 to change the time to 5pm"_

## 📁 Project Structure

```
ai_task_agent/
├── agent.py          # AI agent initialization with Groq model
├── app.py            # Gradio web interface
├── database.py       # JSON database utilities
├── tools.py          # Task management tools
├── requirements.txt  # Project dependencies
├── tasks.json        # Tasks database (auto-created)
└── readme.md         # This file
```

## 📖 How It Works

1. **User Input**: User enters a natural language request in the Gradio UI
2. **Agent Processing**: The Groq-powered agent analyzes the request
3. **Tool Invocation**: The agent selects and executes the appropriate tool
4. **Database Update**: Changes are persisted to `tasks.json`
5. **Response**: The agent returns a friendly confirmation message

## 🔌 API Configuration

The agent uses Groq's OpenAI-compatible API with these settings:

- **Model**: llama-3.3-70b-versatile
- **API Base**: https://api.groq.com/openai/v1
- **Framework**: smolagents CodeAgent

## 💾 Database Schema

Each task in `tasks.json` has the following structure:

```json
{
  "id": 1,
  "task_name": "Task description",
  "due_date": "31st March",
  "time": "6pm",
  "status": "pending"
}
```

## 🎨 UI Tabs

- **💬 Chat & Add Tasks**: Interact with the AI agent to manage tasks
- **📂 View Database**: View all tasks in a formatted list with refresh option

## ⚙️ Configuration

Key settings in `agent.py`:

- Model ID: `llama-3.3-70b-versatile`
- Tools: All five task management tools available
- Base tools: Disabled to focus on task-specific operations

## 🐛 Troubleshooting

**"GROQ_API_KEY is missing"**

- Ensure your `.env` file is in the project root
- Verify your Groq API key is correct

**Agent not responding**

- Check your internet connection
- Verify your Groq API quota hasn't been exceeded
- Ensure all dependencies are installed: `pip install -r requirements.txt`

**Tasks not saving**

- Verify write permissions in the project directory
- Check that `tasks.json` exists or can be created

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Feel free to fork, modify, and improve this project!

---

**Made with ⚡ and Groq AI**
