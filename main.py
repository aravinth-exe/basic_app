import pandas as pd
import numpy as np
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import gradio as gr

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

app = FastAPI()

@app.get('/')
def index():
    # data_source = load_iris()
    # df = pd.DataFrame(data=data_source.data, columns=data_source.feature_names)
    # # Convert the top 5 rows to a list of dicts for JSON response
    # return df.head(5).to_dict(orient='records')
    # # iris_model.py

    # 1. Load the Iris dataset
    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    y = pd.Series(iris.target, name="species")

    # Optional: map species labels
    species_map = dict(zip(range(3), iris.target_names))
    y_named = y.map(species_map)

    # 2. Basic EDA
    print("Dataset Head:\n", X.head())
    print("\nTarget classes:\n", y_named.value_counts())

    # 3. Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 4. Train Model
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    # 5. Predict
    y_pred = model.predict(X_test)

    # 6. Evaluate
    print("\nAccuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=iris.target_names))
    print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

    # 7. Plot Pairplot (only for 2D understanding)
    sns.pairplot(pd.concat([X, y_named.rename("species")], axis=1), hue="species")
    plt.suptitle("Iris Pair Plot", y=1.02)
    plt.show()


# Mock movie search function
# def search_movies(city, movie):
#     return f"🎬 '{movie}' is available in {city} at 6:30 PM and 9:00 PM."

# # Mock ticket booking function
# def book_tickets(city, movie, time, count):
#     return f"✅ Booked {count} ticket(s) for '{movie}' in {city} at {time}."

# # Main function for Gradio
# def ticket_booking(city, movie, time, count):
#     showtimes = search_movies(city, movie)
#     confirmation = book_tickets(city, movie, time, count)
#     return f"{showtimes}\n\n{confirmation}"

# # Gradio interface
# iface = gr.Interface(
#     fn=ticket_booking,
#     inputs=[
#         gr.Textbox(label="City"),
#         gr.Textbox(label="Movie"),
#         gr.Radio(["6:30 PM", "9:00 PM"], label="Select Show Time"),
#         gr.Slider(1, 10, step=1, label="Number of Tickets")
#     ],
#     outputs="text",
#     title="🎟️ Ticket Booking Assistant",
#     description="Simulate movie ticket booking like BookMyShow"
# )

# iface.launch()