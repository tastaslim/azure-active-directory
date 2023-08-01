from config import version, host
from requests import get, delete, post, patch
from json import dumps, loads

# TODO: Create Custom Types for Device Object


class DeviceService:
    def __init__(self, access_token) -> None:
        self.access_token = access_token

    def list_devices(self, params):
        try:
            url = f'{host}/{version}/devices'
            headers = {
                "Authorization": f'Bearer {self.access_token}'
            }
            response = get(url=url, headers=headers, params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)

    def get_device(self, device_id: str, params):
        try:
            url = f'{host}/{version}/devices/{device_id}'
            headers = {
                "Authorization": f'Bearer {self.access_token}'
            }
            response = get(url=url, headers=headers, params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)

    def delete_device(self, device_id: str, params) -> None:
        try:
            url = f'{host}/{version}/devices/{device_id}'
            headers = {
                "Authorization": f'Bearer {self.access_token}'
            }
            response = delete(url=url, headers=headers, params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)
    
    """ 
    {
        "accountEnabled":false,
        "alternativeSecurityIds":
        [
            {
            "type":2,
            "key":"base64Y3YxN2E1MWFlYw=="
            }
        ],
        "deviceId":"4c299165-6e8f-4b45-a5ba-c5d250a707ff",
        "displayName":"Test device",
        "operatingSystem":"linux",
        "operatingSystemVersion":"1"
    }
    """
    def create_device(self, payload, params):
        try:
            url = f'{host}/{version}/devices'
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

    def update_device(self, device_id: str, payload, params):
        try:
            url = f'{host}/{version}/devices/{device_id}'
            headers = {
                "Authorization": f'Bearer {self.access_token}'
            }
            response = patch(url=url, headers=headers,
                             data=payload, params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)

    def list_devices_delta(self, params):
        try:
            url = f'{host}/{version}/devices/delta'
            headers = {
                "Authorization": f'Bearer {self.access_token}'
            }
            response = get(url=url, headers=headers, params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)
    
    def register_devices_owner(self, device_id: str, user_id: str, params):
        try:
            url = f'{host}/{version}/devices/{device_id}/registeredOwners/$ref'
            headers = {
                "Authorization": f'Bearer {self.access_token}',
                "Content-Type": "application/json"
            }
            payload = {
                "@odata.id": f"https://graph.microsoft.com/v1.0/directoryObjects/{user_id}"
            }
            response = post(url=url, headers=headers, data=dumps(payload), params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)
