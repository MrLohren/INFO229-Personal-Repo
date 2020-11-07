import os
from flask import Flask
from slack import WebClient
from nestorbot import NestorBot
from slackeventsapi import SlackEventAdapter

app = Flask(__name__)

slack_event_adapter = SlackEventAdapter(
    os.environ.get("SIGNING_SECRET"), '/slack/events', app)

# Create a slack client
slack_web_client = WebClient(token=os.environ.get("SLACK_TOKEN"))

# Get a new NestorBot
nestor_bot = NestorBot("#private-playground")

# Get the onboarding message payload
message = nestor_bot.get_message_payload()

# Post the onboarding message in Slack
slack_web_client.chat_postMessage(**message)

if __name__ == "__main__":
    app.run(debug=True)