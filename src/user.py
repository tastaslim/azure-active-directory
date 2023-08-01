from config import version, host, beta_version
from requests import get, delete, post, patch
from json import loads, dumps

# TODO: Create Custom Types for User Object

"""_summary_
    As far as I know, "adding custom user attributes and using graph API management" is the category of Azure AD B2C tenants and does not apply to standard Azure AD tenants.
    You can add custom attributes to a user by updating the user:
    Returns:
        _type_: _description_
"""
class UserService:
    def __init__(self, access_token) -> None:
        self.access_token = access_token
    def list_users(self, params):
        try:
            url = f'{host}/{version}/users'
            headers = {
                "Authorization": f'Bearer {self.access_token}'
            }
            response = get(url=url, headers=headers, params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)
    
    def get_user(self, user_id: str, params):
        try:
            url = f'{host}/{version}/users/{user_id}'
            headers = {
                "Authorization": f'Bearer {self.access_token}'
            }
            response = get(url=url, headers=headers, params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)
    
    def delete_user(self, user_id: str, params) -> None:
        try:
            url = f'{host}/{version}/users/{user_id}'
            headers = {
                "Authorization": f'Bearer {self.access_token}'
            }
            response = delete(url=url, headers=headers, params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)

    def create_user(self, payload, params):
        try:
            url = f'{host}/{version}/users'
            headers = {
                "Authorization": f'Bearer {self.access_token}',
                "Content-Type" : "application/json"
            }
            response = post(url=url, headers=headers, data=dumps(payload), params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)

    def update_user(self, user_id: str, payload, params):
        try:
            url = f'{host}/{version}/users/{user_id}'
            headers = {
                "Authorization": f'Bearer {self.access_token}',
                "Content-Type": "application/json"
            }
            response = patch(url=url, headers=headers,
                             data=payload, params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)
      
        """_summary_
        Alternative: return only the changed properties
        Adding an optional request header - prefer:return=minimal - results in the following behavior:
        If the property has changed, the new value is included in the response. This includes properties being set to null value.
        If the property has not changed, the property is not included in the response at all. (Different from the default behavior.)
        
        Changes to the licenseAssignmentStates property are currently not tracked.
        
        Problem with delta is that it only gives the userid of deleted users and no other info. We can use list deleted user endpoint
        to list all recently deleted user.
        """
    def list_users_delta(self, params):
        try:
            url = f'{host}/{version}/users/delta'
            headers = {
                "Authorization": f'Bearer {self.access_token}'
            }
            response = get(url=url, headers=headers, params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)
            
    def list_user_licenses(self, user_id:str, params):
        try:
            url = f'{host}/{version}/users/{user_id}/licenseDetails'
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
        "addLicenses": [
            {
            "disabledPlans": [ "11b0131d-43c8-4bbb-b2c8-e80f9a50834a" ],
            "skuId": "45715bb8-13f9-4bf6-927f-ef96c102d394"
            }
        ]
    }
    """
    
    # This API only works if {"usageLocation": "YOUR_COUNTRY_CODE"} is assigned to the user
    
    def assign_user_license(self, user_id: str, payload, params):
        try:
            url = f'{host}/{version}/users/{user_id}/assignLicense'
            headers = {
                "Authorization": f'Bearer {self.access_token}',
                "Content-Type": "application/json"
            }
            response = post(url=url, headers=headers, data=dumps(payload), params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)

    def list_deleted_users(self, params):
        try:
            url = f'{host}/{version}/directory/deletedItems/microsoft.graph.user'
            headers = {
                "Authorization": f'Bearer {self.access_token}'
            }
            response = get(url=url, headers=headers, params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)
            
    # User direct and indirect membership in groups, directory roles, and administrative units
    def list_user_transitive_membership(self, user_id:str, params):
        try:
            url = f'{host}/{version}/users/{user_id}/transitiveMemberOf'
            headers = {
                "Authorization": f'Bearer {self.access_token}',
                "ConsistencyLevel" : "eventual"
            }
            response = get(url=url, headers=headers, params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)
    
    # User Direct membership in groups, directory roles, and administrative units. We can use this API too for user roles
    # instead of list_user_roles method. In case of this API we need to pass roleTemplateId values in roleDefinitionId while creating/restoring roles
    def list_user_membership(self, user_id: str, params):
        try:
            url = f'{host}/{version}/users/{user_id}/memberOf'
            headers = {
                "Authorization": f'Bearer {self.access_token}',
                "ConsistencyLevel": "eventual"
            }
            response = get(url=url, headers=headers, params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)
    
    """
    It will return list of roles assigned to user but won't give all info of roles rather the Id. To get all info
    Pick the id from response and call get_role method in role_assignment.py
    """      
    def list_user_roles(self, user_id:str, params):
        try:
            url = f"{host}/{beta_version}/rolemanagement/directory/transitiveRoleAssignments?$count=true&$filter=principalId eq '{user_id}'"
            headers = {
                "Authorization": f'Bearer {self.access_token}',
                "ConsistencyLevel": "eventual"
            }
            response = get(url=url, headers=headers, params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)
    
    def assign_user_roles(self, user_id: str, role_id:str, params):
        try:
            url = f"{host}/{version}/roleManagement/directory/roleAssignments"
            headers = {
                "Authorization": f'Bearer {self.access_token}',
                "Content-Type": "application/json"
            }
            payload = {
                "@odata.type": "#microsoft.graph.unifiedRoleAssignment",
                "roleDefinitionId": f"{role_id}",
                "principalId": f"{user_id}",
                "directoryScopeId": "/"
            }
            response = post(url=url, headers=headers, data=dumps(payload), params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)
            
    def list_user_authentication_methods(self, user_id: str, params):
        try:
            url = f"{host}/{version}/users/{user_id}/authentication/methods"
            headers = {
                "Authorization": f'Bearer {self.access_token}'
            }
            response = get(url=url, headers=headers, params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)
    
        """_summary_
        {
            "phoneNumber": "+1 2065555555",
            "phoneType": "mobile"
        }
        """     
    def add_phone_authentication(self, user_id: str, payload, params):
        try:
            url = f"{host}/{version}/users/{user_id}/authentication/phoneMethods"
            headers = {
                "Authorization": f'Bearer {self.access_token}',
                "Content-Type": "application/json"
            }
            response = post(url=url, headers=headers, data=dumps(payload), params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)
            
    def enable_sms_sign_in(self, user_id: str, mobile_phone_id: str, params):
        try:
            url = f"{host}/{version}/users/{user_id}/authentication/phoneMethods/{mobile_phone_id}/enableSmsSignIn"
            headers = {
                "Authorization": f'Bearer {self.access_token}',
                "Content-Type": "application/json"
            }
            response = post(url=url, headers=headers, params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)
    """_summary_
    {
        "emailAddress": "taslim@contoso.com"
    }
    """
    def add_email_authentication(self, user_id: str, payload, params):
        try:
            url = f"{host}/{version}/users/{user_id}/authentication/emailMethods"
            headers = {
                "Authorization": f'Bearer {self.access_token}',
                "Content-Type": "application/json"
            }
            response = post(url=url, headers=headers, data=dumps(payload), params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)
            
    """_summary_   
    {
        "startDateTime": "2022-06-05T00:00:00.000Z",
        "lifetimeInMinutes": 60,
        "isUsableOnce": false
    }
    """
    def add_temporary_access_pass_authentication(self, user_id: str, payload, params):
        try:
            url = f"{host}/{version}/users/{user_id}/authentication/temporaryAccessPassMethods"
            headers = {
                "Authorization": f'Bearer {self.access_token}',
                "Content-Type": "application/json"
            }
            response = post(url=url, headers=headers, data=dumps(payload), params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)
             
    def list_user_ownerships(self, user_id: str, params):
        try:
            url = f"{host}/{version}/users/{user_id}/ownedObjects"
            headers = {
                "Authorization": f'Bearer {self.access_token}'
            }
            response = get(url=url, headers=headers, params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)
            
    def list_user_assigned_to_applications(self, user_id: str, params):
        try:
            url = f"{host}/{version}/users/{user_id}/appRoleAssignments"
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
        "principalId": "cde330e5-2150-4c11-9c5b-14bfdc948c79", # userId
        "resourceId": "8e881353-1735-45af-af21-ee1344582a4d", #applicationId
        "appRoleId": "00000000-0000-0000-0000-000000000000"
    }
    """

    def assign_user_to_application(self, user_id: str, resource_id: str,  params):
        try:
            url = f"{host}/{version}/users/{user_id}/appRoleAssignments"
            headers = {
                "Authorization": f'Bearer {self.access_token}',
                "Content-Type": "application/json"
            }
            
            payload = {
                "principalId": user_id,
                "resourceId": resource_id,  # applicationId
                # "appRoleId": "00000000-0000-0000-0000-000000000000"
            }
            response = post(url=url, headers=headers, data= dumps(payload), params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)
    
    def list_user_owned_devices(self, user_id: str, params):
        try:
            url = f"{host}/{version}/users/{user_id}/ownedDevices"
            headers = {
                "Authorization": f'Bearer {self.access_token}'
            }
            response = get(url=url, headers=headers, params=params)
            data = loads(response.text)
            return data
        except Exception as e:
            print(e)
