from flask import Flask, render_template, request

app = Flask(__name__)

# If-Else Chatbot Function
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How are you?"
    elif "how are you" in user_input:
        return "I'm doing great, thanks for asking!"
    elif "your name" in user_input:
        return "I am a simple AI chatbot."
    elif "bye" in user_input:
        return "Goodbye! Have a nice day!"
    else:
        return "Sorry, I didn't understand that."

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    if request.method == "POST":
        user_message = request.form["message"]
        response = chatbot_response(user_message)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)

