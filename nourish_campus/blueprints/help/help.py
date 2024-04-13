from flask import Flask, Blueprint, render_template, request
import openai
help_bp = Blueprint("help", __name__, template_folder="templates")

openai.api_key  = "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"

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]
@help_bp.route("/help")
def home():    
    return render_template("home.html")
@help_bp.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')  
    response = get_completion(userText)  
    #return str(bot.get_response(userText)) 
    return response
if __name__ == "__main__":
    help_bp.run(debug=True, host="127.0.0.1", port=5000)