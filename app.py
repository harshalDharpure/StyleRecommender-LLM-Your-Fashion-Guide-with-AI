from flask import Flask, request, jsonify,render_template, request, jsonify
import openai

app = Flask(__name__)

# Initialize your OpenAI GPT-3 API key
# Replace 'your_api_key_here' with your actual API key
openai.api_key = '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'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend_clothing():
    user_input = request.json.get('user_input')

    # Use the GPT-3 model to generate clothing recommendations based on user input
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"I need clothing recommendations for a {user_input} event.",
        max_tokens=50  # Adjust this based on desired response length
    )

    recommendation = response.choices[0].text.strip()

    if recommendation:
        return jsonify({"recommendation": recommendation})
    else:
        return jsonify({"recommendation": "No recommendation available for this occasion."})

if __name__ == '__main__':
    app.run(debug=True)
