from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/')
def get_quote():
    with open('quotes.txt', 'r') as f:
        quotes = f.readlines()
    quote = random.choice(quotes)
    return jsonify(quote=quote)

if __name__ == '__main__':
    app.run(debug=True)