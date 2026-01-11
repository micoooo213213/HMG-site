from flask import Flask, send_from_directory
from pyngrok import ngrok

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory(".", "index.html")  # Serves your HTML file

if __name__ == "__main__":
    # Start ngrok tunnel
    public_url = ngrok.connect(5000)
    print("🌐 Public URL:", public_url)
    
    # Run Flask app
    app.run(port=5000)
