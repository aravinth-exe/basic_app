import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import gradio as gr

app = FastAPI()

# @app.get('/')
# def index():
#     data_source = load_iris()
#     df = pd.DataFrame(data=data_source.data, columns=data_source.feature_names)
#     # Convert the top 5 rows to a list of dicts for JSON response
#     return df.head(5).to_dict(orient='records')

# Mock movie search function
def search_movies(city, movie):
    return f"🎬 '{movie}' is available in {city} at 6:30 PM and 9:00 PM."

# Mock ticket booking function
def book_tickets(city, movie, time, count):
    return f"✅ Booked {count} ticket(s) for '{movie}' in {city} at {time}."

# Main function for Gradio
def ticket_booking(city, movie, time, count):
    showtimes = search_movies(city, movie)
    confirmation = book_tickets(city, movie, time, count)
    return f"{showtimes}\n\n{confirmation}"

# Gradio interface
iface = gr.Interface(
    fn=ticket_booking,
    inputs=[
        gr.Textbox(label="City"),
        gr.Textbox(label="Movie"),
        gr.Radio(["6:30 PM", "9:00 PM"], label="Select Show Time"),
        gr.Slider(1, 10, step=1, label="Number of Tickets")
    ],
    outputs="text",
    title="🎟️ Ticket Booking Assistant",
    description="Simulate movie ticket booking like BookMyShow"
)

iface.launch()