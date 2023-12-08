# import openai
# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route('/chat', methods=['POST'])
# def chat():
#     user_input = request.json.get('input')
#     openai.api_key = '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'

#     response = openai.Completion.create(
#       engine="text-davinci-003",
#       prompt=user_input,
#       max_tokens=150
#     )

#     return jsonify(response.choices[0].text.strip())

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)

import openai

def get_openai_response(prompt, api_key, model="gpt-3.5-turbo"):
    """
    Generates a response from OpenAI's chat model.

    :param prompt: The prompt to send to the model.
    :param api_key: Your OpenAI API key.
    :param model: The chat model to use. Defaults to 'gpt-3.5-turbo'.
    :return: The model's response as a string.
    """
    openai.api_key = api_key

    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content']
    except Exception as e:
        return str(e)

def main():
    api_key = "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"  # Replace with your OpenAI API key
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        response = get_openai_response(user_input, api_key)
        print("AI:", response)

if __name__ == "__main__":
    main()


# from flask import Flask, render_template, request, jsonify
# import openai

# app = Flask(__name__)

# def get_openai_response(prompt, api_key, model="gpt-3.5-turbo"):
#     openai.api_key = api_key
#     try:
#         response = openai.ChatCompletion.create(
#             model=model,
#             messages=[{"role": "user", "content": prompt}]
#         )
#         return response.choices[0].message['content']
#     except Exception as e:
#         return str(e)

# @app.route("/")
# def index():
#     return render_template('test.html')

# @app.route("/get_response", methods=["POST"])
# def get_response():
#     user_input = request.json["message"]
#     api_key = "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"  # Replace with your OpenAI API key
#     return jsonify({"response": get_openai_response(user_input, api_key)})

# if __name__ == "__main__":
#     app.run(debug=True)

