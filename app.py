from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)

client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

@app.route("/generate", methods=["POST"])
def generate_story():
    data = request.json

    prompt = f"""
    Write a short {data['genre']} story.
    Characters: {data['characters']}
    Theme: {data['theme']}
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    story = response.choices[0].message.content
    return jsonify({"story": story})

if __name__ == "__main__":
    app.run(debug=True)
