import os
from flask import Flask, render_template

template_dir = os.path.join(os.path.dirname(__file__), '..', 'templates')
static_dir = os.path.join(os.path.dirname(__file__), '..', 'static')
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
app.config['DEBUG'] = True

# Menu data
menu = [
    {"name": "Idli", "ingredients": ["Rice", "Urad Dal", "Water", "Salt"]},
    {"name": "Dosa", "ingredients": ["Rice", "Urad Dal", "Potatoes", "Onions", "Curry Leaves", "Mustard Seeds"]},
    {"name": "Sambar", "ingredients": ["Toor Dal", "Tamarind", "Vegetables (e.g., Drumstick)", "Spices"]},
    {"name": "Vada", "ingredients": ["Urad Dal", "Onions", "Green Chilies", "Curry Leaves"]},
    {"name": "Pongal", "ingredients": ["Rice", "Moong Dal", "Ghee", "Pepper", "Cumin"]},
    {"name": "Uttapam", "ingredients": ["Rice", "Urad Dal", "Tomatoes", "Onions", "Green Chilies"]},
    {"name": "Rasam", "ingredients": ["Tamarind", "Tomatoes", "Garlic", "Spices"]}
]

@app.route('/')
def home():
    return render_template('index.html', menu=menu)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
