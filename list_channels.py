from botbuilder.schema import *
from botframework.connector.auth import MicrosoftAppCredentials
from botframework.connector.teams.teams_connector_client import TeamsConnectorClient
from dotenv import load_dotenv
from os import getenv

load_dotenv()

credentials = MicrosoftAppCredentials(getenv("APP_ID"), getenv("APP_PASSWORD"))
connector = TeamsConnectorClient(credentials, base_url=getenv("SERVICE_URL"))

channels = connector.teams.get_teams_channels(team_id=getenv("TEAM_ID"))

for channel in channels.conversations:
    print(f"{channel.name} ({channel.id})")
