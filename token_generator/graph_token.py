import json
import os
from requests import get

from token_generator.token_generator import TokenGenerator


class GraphTokenGenerator(TokenGenerator):
    def __init__(self, token_provider):
        super().__init__(token_provider)
        
    def access_token(self, tenant_id: str) -> str:
        try:
            print(f'Generating Token for {self.token_provider}')
            url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
            payload = f'client_id={os.getenv("MICROSOFT_CLIENT_ID")}&client_secret={os.getenv("MICROSOFT_CLIENT_SECRET")}&scope=https://graph.microsoft.com/.default&grant_type=client_credentials'
            response = get(url, data=payload)
            data = json.loads(response.text)
            return data["access_token"]
        except Exception as e:
            print(e)
            return f'Error while generating access token for {tenant_id}'
