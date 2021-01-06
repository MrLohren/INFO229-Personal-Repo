import os
from flask import Flask
from slack import WebClient
from nestorbot import NestorBot
from slackeventsapi import SlackEventAdapter

app = Flask(__name__)

slack_event_adapter = SlackEventAdapter(
    os.environ.get("SIGNING_SECRET"), '/', app)

# Create a slack client
slack_web_client = WebClient(token=os.environ.get("SLACK_TOKEN"))

# Get a new NestorBot
nestor_bot = NestorBot("#private-playground")

# Get the onboarding message payload
greeting = nestor_bot.get_message_payload()

# Post the onboarding message in Slack
slack_web_client.chat_postMessage(**greeting)
BOT_API = "U01C83MH5GD"

@slack_event_adapter.on('message')
def message(payload):
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')

    #answer
    if BOT_API != user_id:
        if text.lower().startswith("nestor busca: "):
            w_query = text.lower()[13::]
            #slack_web_client.chat_postMessage(channel=channel_id, text=w_query)
            w_response = nestor_bot.buscar_en_wikipedia(w_query)
            slack_web_client.chat_postMessage(channel=channel_id, text=w_response)

if __name__ == "__main__":
    app.run()