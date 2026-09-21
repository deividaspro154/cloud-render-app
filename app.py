from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Cloud Computing Project</h1>
    <p>This application is deployed using Render.com.</p>
    <p>Platform as a Service (PaaS) example.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)