from config import version, host
from requests import get, delete, post, patch
from json import loads

# TODO: Create Custom Types for User Object


class RoleAssignmentService:
    def __init__(self, access_token) -> None:
        self.access_token = access_token

    def list_roles(self, params):
        try:
            url = f'{host}/{version}/roleManagement/directory/roleDefinitions'
            headers = {
                "Authorization": f'Bearer {self.access_token}'
            }
            response = get(url=url, headers=headers, params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)

    def get_role(self, role_id: str, params):
        try:
            url = f'{host}/{version}/roleManagement/directory/roleDefinitions/{role_id}'
            headers = {
                "Authorization": f'Bearer {self.access_token}'
            }
            response = get(url=url, headers=headers, params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)