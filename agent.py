import os
from dotenv import load_dotenv
from smolagents import CodeAgent, OpenAIServerModel

# Import ALL our tools
from tools import add_task, list_tasks, delete_task, update_task_status, edit_task

load_dotenv()


def get_agent():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError(
            "GROQ_API_KEY is missing. Please check your .env file.")

    groq_model = OpenAIServerModel(
        model_id="llama-3.3-70b-versatile",
        api_base="https://api.groq.com/openai/v1",
        api_key=api_key
    )

    # Give the agent access to the full suite of tools
    agent = CodeAgent(
        tools=[add_task, list_tasks, delete_task,
               update_task_status, edit_task],
        model=groq_model,
        add_base_tools=False
    )

    return agent
