import random
import gradio as gr

def generate_item(prompt):
    return f"The {random.choice(['Sword', 'Amulet', 'Ring', 'Dagger'])} of {random.choice(['Flames', 'Shadows', 'Eternity', 'Storms'])}"

iface = gr.Interface(
    fn=generate_item,
    inputs=gr.Textbox(label="Enter your prompt"),
    outputs=gr.Textbox(label="Generated Fantasy Item"),
    title="🧝‍♀️ Fantasy Item Generator",
    description="Generate magical fantasy items using AI!",
)

iface.launch()
