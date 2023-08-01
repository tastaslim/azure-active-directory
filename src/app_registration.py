from config import version, host
from requests import get, delete, post, patch
from json import dumps, loads

# TODO: Create Custom Types for Application Object


class AppRegistrationService:
    def __init__(self, access_token) -> None:
        self.access_token = access_token

    def list_applications(self, params):
        try:
            url = f'{host}/{version}/applications'
            headers = {
                "Authorization": f'Bearer {self.access_token}'
            }
            response = get(url=url, headers=headers, params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)

    def get_application(self, application_id: str, params):
        try:
            url = f'{host}/{version}/applications/{application_id}'
            headers = {
                "Authorization": f'Bearer {self.access_token}'
            }
            response = get(url=url, headers=headers, params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)

    def delete_application(self, application_id: str, params) -> None:
        try:
            url = f'{host}/{version}/applications/{application_id}'
            headers = {
                "Authorization": f'Bearer {self.access_token}'
            }
            response = delete(url=url, headers=headers, params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)

    def create_application(self, payload, params):
        try:
            url = f'{host}/{version}/applications'
            headers = {
                "Authorization": f'Bearer {self.access_token}'
            }
            response = post(url=url, headers=headers,
                            data=dumps(payload), params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)

    def update_application(self, application_id: str, payload, params):
        try:
            url = f'{host}/{version}/applications/{application_id}'
            headers = {
                "Authorization": f'Bearer {self.access_token}'
            }
            response = patch(url=url, headers=headers,
                             data=dumps(payload), params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)

    def list_applications_delta(self, params):
        try:
            url = f'{host}/{version}/applications/delta'
            headers = {
                "Authorization": f'Bearer {self.access_token}'
            }
            response = get(url=url, headers=headers, params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)
    
    def add_application_owner(self, application_id: str, directory_object_id: str, params):
        try:
            url = f'{host}/{version}/applications/{application_id}/owners/$ref'
            headers = {
                "Authorization": f'Bearer {self.access_token}',
                "Content-Type": "application/json"
            }
            payload = {
                "@odata.id": f"{host}/{version}/directoryObjects/{directory_object_id}"
            }
            response = post(url=url, headers=headers, data=dumps(payload),params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)
