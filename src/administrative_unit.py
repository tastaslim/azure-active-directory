from config import version, host
from requests import get, delete, post, patch
from json import dumps, loads

# TODO: Create Custom Types for AdministrativeUnit Object


class AdministrativeUnitService:
    def __init__(self, access_token) -> None:
        self.access_token = access_token

    def list_administrative_units(self, params):
        try:
            url = f'{host}/{version}/directory/administrativeUnits'  
            headers = {
                "Authorization": f'Bearer {self.access_token}'
            }
            response = get(url=url, headers=headers, params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)

    def get_administrative_unit(self, administrative_unit_id: str, params):
        try:
            url = f'{host}/{version}/directory/administrativeUnits/{administrative_unit_id}'
            headers = {
                "Authorization": f'Bearer {self.access_token}'
            }
            response = get(url=url, headers=headers, params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)

    def delete_administrative_unit(self, administrative_unit_id: str, params) -> None:
        try:
            url = f'{host}/{version}/directory/administrativeUnits/{administrative_unit_id}'
            headers = {
                "Authorization": f'Bearer {self.access_token}'
            }
            response = delete(url=url, headers=headers, params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)

    def create_administrative_unit(self, payload, params):
        try:
            url = f'{host}/{version}/directory/administrativeUnits'
            headers = {
                "Authorization": f'Bearer {self.access_token}'
            }
            response = post(url=url, headers=headers,
                            data=dumps(payload), params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)

    def update_administrative_unit(self, administrative_unit_id: str, payload, params):
        try:
            url = f'{host}/{version}/directory/administrativeUnits/{administrative_unit_id}'
            headers = {
                "Authorization": f'Bearer {self.access_token}'
            }
            response = patch(url=url, headers=headers,
                            data=dumps(payload), params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)

    def list_administrative_units_delta(self, params):
        try:
            url = f'{host}/{version}/directory/administrativeUnits/delta'
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
        "@odata.id":"https://graph.microsoft.com/v1.0/users/{user-id}"
    }
    """

    def add_user_to_administrative_unit(self, administrative_unit_id: str, user_id: str, params):
        try:
            url = f'{host}/{version}/directory/administrativeUnits/{administrative_unit_id}/members/$ref'
            headers = {
                "Authorization": f'Bearer {self.access_token}',
                "Content-Type": "application/json"
            }
            payload = {
                "@odata.id": f"https://graph.microsoft.com/v1.0/users/{user_id}"
            }
            response = post(url=url, headers=headers, data=dumps(payload), params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)
