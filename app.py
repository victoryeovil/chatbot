from urllib import response
import requests
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/txt', methods=['GET','POST'])
def bot():
    #creating logic of bot
    msg = request.form.get('Body')
    resp =MessagingResponse()
    respond = False

    if "quote" in msg.lower():
        results = requests.get('https://api.quotable.io/random')

        if results.status_code == 200:
            results_object = results.json()
            quote = f"{results_object['content'] + 'By:' + results_object['author']}"


        else:
            quote = "I couldn't fetch a quote, make sure to include the word quote in your message"


        resp.message(quote)

        return str(resp)
        respond = True

    if "cat" in msg.lower():

        return str(resp)
        respond = True

    if not respond:
        resp.message("I couldn't fetch a quote, make sure to include the word quote in your message")
        return str(resp)

if __name__ == '__main__':
    app.run() 