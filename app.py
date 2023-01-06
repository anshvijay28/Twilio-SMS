import mimetypes
from flask import Flask, Response, request
from twilio.twiml.messaging_response import MessagingResponse
import sys
sys.path.append('/Users/anshvijay/Desktop/IPhone_Automation')
sys.path.append('/Users/anshvijay/Desktop/Email_Automation')
from construct_message import get_body
import twilio_balance
import getting_quote

# import donenv for keeping passwords/API keys out of source code

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/sms", methods=['GET', 'POST'])
def send_sms():

    body = request.values.get('Body', None)
    body = str(body).lower().strip()

    # Start our TwiML response
    resp = MessagingResponse()
    
    # Logic of which message to respond with 
    if (body == "quote"):
      msg = resp.message(getting_quote.get_quote())
    elif (body == "weather"):
      msg = resp.message(get_body())
    elif (body == "hi"):
      msg = resp.message("Hey there!")
    elif (body == "picture"):
      msg = resp.message("Here is a picture")
      # Currently working on generating an image 
      # msg = resp.media("https://images.app.goo.gl/gr2rEFzEq1Zm2P1W9")
    elif (body == "balance"):
      msg = resp.message(twilio_balance.get_balance())
    else:
      msg = resp.message("Please type a valid command.")

    return Response(str(resp), mimetype="application/xml")


if __name__ == "__main__":
  app.run(debug=True)

