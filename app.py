import gradio as gr
from agent import get_agent
from database import load_tasks

# Initialize our Groq-powered agent
agent = get_agent()


def process_user_input(prompt):
    if not prompt:
        return "Please enter a request."
    try:
        # We give the agent a strong directive on how to behave
        system_prompt = f"""
        Process this user request: '{prompt}'. 
        
        RULES:
        1. If adding a task, use add_task.
        2. If editing, deleting, or updating the status of a task, you MUST use the `list_tasks` tool FIRST to find the correct integer ID.
        3. Once you have the ID, use the appropriate tool (edit_task, delete_task, or update_task_status).
        4. Reply to the user in a brief, friendly, and natural way telling them what you did.
        """
        response = agent.run(system_prompt)
        return response
    except Exception as e:
        return f"Agent Error: {str(e)}"


def format_tasks_for_ui():
    tasks = load_tasks()
    if not tasks:
        return "No tasks found in the database. Add some!"

    display_text = "📋 **Your Task List:**\n\n"
    for t in tasks:
        display_text += f"- **[{t['id']}] {t['task_name']}** \n  *(Due: {t['due_date']} @ {t['time']})* - Status: `{t['status']}`\n"
    return display_text


# Build the Gradio Interface
with gr.Blocks(theme=gr.themes.Monochrome()) as demo:
    gr.Markdown("# ⚡ Groq-Powered AI Task Agent")
    gr.Markdown(
        "Type a natural language request like: *'Remind me to complete DSA at 6pm and revise DBMS tomorrow'*")

    with gr.Tab("💬 Chat & Add Tasks"):
        with gr.Row():
            user_input = gr.Textbox(
                lines=2, placeholder="Enter your tasks here...", scale=4)
            submit_btn = gr.Button("Send to Agent", variant="primary", scale=1)

        output_text = gr.Textbox(
            label="Agent Response", interactive=False, lines=4)
        submit_btn.click(fn=process_user_input,
                         inputs=user_input, outputs=output_text)

    with gr.Tab("📂 View Database"):
        refresh_btn = gr.Button("🔄 Refresh Task List")
        tasks_display = gr.Markdown(format_tasks_for_ui())
        refresh_btn.click(fn=format_tasks_for_ui,
                          inputs=[], outputs=tasks_display)

if __name__ == "__main__":
    print("Starting Gradio App...")
    demo.launch()
