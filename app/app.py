from flask import Flask, jsonify

app = Flask(__name__)  # Jenkins trigger test

@app.route("/")
def home():
    return jsonify({
        "message": "CI/CD Pipeline Working 🚀"
    })

if __name__ == "__main__":
    app.run(debug=True)