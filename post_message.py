from botbuilder.schema import *
from botframework.connector import ConnectorClient
from botframework.connector.auth import MicrosoftAppCredentials
from dotenv import load_dotenv
from os import getenv

load_dotenv()

credentials = MicrosoftAppCredentials(getenv("APP_ID"), getenv("APP_PASSWORD"))
connector = ConnectorClient(credentials, base_url=getenv("SERVICE_URL"))

conversation = connector.conversations.create_conversation(ConversationParameters(
    is_group=True,
    channel_data={ "channel": { "id": getenv("TEST_CHANNEL_ID") } },
    activity=Activity(
        type=ActivityTypes.message,
        text="Hello, world from Python")))

reply = connector.conversations.send_to_conversation(conversation.id, Activity(
    type=ActivityTypes.message,
    text="This is a reply"))
