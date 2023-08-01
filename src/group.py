from config import version, host
from requests import get, delete, post, patch
from json import dumps, loads

# TODO: Create Custom Types for Group Object


class GroupService:
    def __init__(self, access_token) -> None:
        self.access_token = access_token

    def list_groups(self, params):
        try:
            url = f'{host}/{version}/groups'
            headers = {
                "Authorization": f'Bearer {self.access_token}'
            }
            response = get(url=url, headers=headers, params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)

    def get_group(self, group_id: str, params):
        try:
            url = f'{host}/{version}/groups/{group_id}'
            headers = {
                "Authorization": f'Bearer {self.access_token}'
            }
            response = get(url=url, headers=headers, params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)

    def delete_group(self, group_id: str, params) -> None:
        try:
            url = f'{host}/{version}/groups/{group_id}'
            headers = {
                "Authorization": f'Bearer {self.access_token}'
            }
            response = delete(url=url, headers=headers, params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)

    def create_group(self, payload, params):
        try:
            url = f'{host}/{version}/groups'
            headers = {
                "Authorization": f'Bearer {self.access_token}',
                "Content-Type": "application/json"
            }
            response = post(url=url, headers=headers,
                            data=dumps(payload), params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)

    def update_group(self, group_id: str, payload, params):
        try:
            url = f'{host}/{version}/groups/{group_id}'
            headers = {
                "Authorization": f'Bearer {self.access_token}',
                "Content-Type": "application/json"
            }
            response = patch(url=url, headers=headers,
                             data=dumps(payload), params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)

    def list_groups_delta(self, params):
        try:
            url = f'{host}/{version}/groups/delta'
            headers = {
                "Authorization": f'Bearer {self.access_token}'
            }
            response = get(url=url, headers=headers, params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)
    
    def list_deleted_groups(self, params):
        try:
            url = f'{host}/{version}/directory/deletedItems/microsoft.graph.group'
            headers = {
                "Authorization": f'Bearer {self.access_token}'
            }
            response = get(url=url, headers=headers, params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)
    
    def list_member_groups(self, group_id:str, params):
        try:
            url = f'{host}/{version}/groups/{group_id}/members'
            headers = {
                "Authorization": f'Bearer {self.access_token}'
            }
            response = get(url=url, headers=headers, params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)
    
    """ 
    {
        "@odata.id": "https://graph.microsoft.com/v1.0/directoryObjects/{id}"
    }
    """
    def add_group_member(self, group_id: str, user_id, params):
        try:
            url = f'{host}/{version}/groups/{group_id}/members/$ref'
            headers = {
                "Authorization": f'Bearer {self.access_token}',
                "Content-Type": "application/json"
            }
            payload = {
                "@odata.id": f"https://graph.microsoft.com/v1.0/directoryObjects/{user_id}"
            }
            response = post(url=url, headers=headers, data=dumps(payload),params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)
            
    def list_owner_groups(self, group_id:str, params):
        try:
            url = f'{host}/{version}/groups/{group_id}/owners'
            headers = {
                "Authorization": f'Bearer {self.access_token}'
            }
            response = get(url=url, headers=headers, params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)
            
        """_summary_
        If successful, this method returns a 204 No Content response code. It does not return anything in the 
        response body. This method returns a 400 Bad Request response code when the object is already a member 
        of the group. This method returns a 404 Not Found response code when the object being added doesn't exist.
        """
    def add_owner(self, group_id: str, user_id: str, params):
        try:
            url = f'{host}/{version}/groups/{group_id}/owners/$ref'
            headers = {
                "Authorization": f'Bearer {self.access_token}',
                "Content-Type": "application/json"
            }
            payload = {
                "@odata.id": f"https://graph.microsoft.com/v1.0/users/{user_id}"
            }
            response = post(url=url, headers=headers, data=dumps(payload),params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)
