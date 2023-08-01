
"""
1. Function names use snake_case instead of camelCase.
2. Any Lodash function that shares its name with a reserved Python keyword will have an _ appended after it (e.g. filter in Lodash would be filter_ in pydash).
3. Lodash's toArray() is pydash's to_list().
4. Lodash's functions() is pydash's callables(). This particular name difference was chosen in order to allow for 
the functions.py module file to exist at root of the project. Previously, functions.py existed in pydash/api/ but 
in v2.0.0, it was decided to move everything in api/ to pydash/. Therefore, to avoid import ambiguities, the 
functions() function was renamed.
5. Lodash's is_native() is pydash's is_builtin(). This aligns better with Python's builtins terminology.

from pydash import map_, pick
"""

from threading import Thread
from token_generator import GraphTokenGenerator
from src import UserService, GroupService, AdministrativeUnitService, DeviceService
from json import loads
access_token = GraphTokenGenerator("Graph_API").access_token("649b37da-e479-45dc-a099-fda797d7fcee")
usr = UserService(access_token=access_token)
grp = GroupService(access_token=access_token)
adm = AdministrativeUnitService(access_token=access_token)
dvc = DeviceService(access_token="eyJ0eXAiOiJKV1QiLCJub25jZSI6ImdFb3dIMGI1OU1hd3pyNzFRbWsteXZyc3FydE9vV3M3T1pFS1VTNUQ4aFUiLCJhbGciOiJSUzI1NiIsIng1dCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyIsImtpZCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyJ9.eyJhdWQiOiJodHRwczovL2dyYXBoLm1pY3Jvc29mdC5jb20iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC82NDliMzdkYS1lNDc5LTQ1ZGMtYTA5OS1mZGE3OTdkN2ZjZWUvIiwiaWF0IjoxNjkwNzc4OTgzLCJuYmYiOjE2OTA3Nzg5ODMsImV4cCI6MTY5MDc4NDAyMiwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFUUUF5LzhVQUFBQWxMRjdjSzNGaSt4bnI0ckJSdll6V1pmcTBScVhXS25sNjE4dGM0ckoveGtBSENXQjlHNkZGT0R5YjcvYWE2ZnUiLCJhbXIiOlsicHdkIl0sImFwcF9kaXNwbGF5bmFtZSI6IlRlc3RpbmctVGVhbXMiLCJhcHBpZCI6IjQxNTRhMGI3LTU3NTMtNDA0Mi04NjkxLTY2YjllZTk2YzlmZCIsImFwcGlkYWNyIjoiMSIsImZhbWlseV9uYW1lIjoiSmFjb2IiLCJnaXZlbl9uYW1lIjoiUm9ubywiLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiIxMzYuMTg1LjIxMC4xOTQiLCJuYW1lIjoiUm9ubywgSmFjb2IiLCJvaWQiOiJmOGEzNGY3NS1kYjU0LTQ1MTItYTYwZi0zZDYzMWYyMGI2NWIiLCJwbGF0ZiI6IjUiLCJwdWlkIjoiMTAwMzdGRkU5MjgyQUFGOSIsInJoIjoiMC5BVmdBMmplYlpIbmszRVdnbWYybmw5Zjg3Z01BQUFBQUFBQUF3QUFBQUFBQUFBQllBRnMuIiwic2NwIjoiRGlyZWN0b3J5LkFjY2Vzc0FzVXNlci5BbGwgVXNlci5SZWFkIHByb2ZpbGUgb3BlbmlkIGVtYWlsIiwic2lnbmluX3N0YXRlIjpbImttc2kiXSwic3ViIjoiYnpsZk5zUW5GNmZOa2QyUTdMZW11SkkyUHJZVDdyeFpxMGNwMHNPbE1wMCIsInRlbmFudF9yZWdpb25fc2NvcGUiOiJOQSIsInRpZCI6IjY0OWIzN2RhLWU0NzktNDVkYy1hMDk5LWZkYTc5N2Q3ZmNlZSIsInVuaXF1ZV9uYW1lIjoiaW5TeW5jLW9mZmljZTM2NS1pbnRlcm5hbEBkcnV2YWludGVybmFsLm9ubWljcm9zb2Z0LmNvbSIsInVwbiI6ImluU3luYy1vZmZpY2UzNjUtaW50ZXJuYWxAZHJ1dmFpbnRlcm5hbC5vbm1pY3Jvc29mdC5jb20iLCJ1dGkiOiJiS1FkNGdyaV9rV3piUmsyQ2NzT0FBIiwidmVyIjoiMS4wIiwid2lkcyI6WyI2MmU5MDM5NC02OWY1LTQyMzctOTE5MC0wMTIxNzcxNDVlMTAiLCJiNzlmYmY0ZC0zZWY5LTQ2ODktODE0My03NmIxOTRlODU1MDkiXSwieG1zX3N0Ijp7InN1YiI6IkFQand3bXVQVUxGdDdSaExLWFJFSnMzZklCMTU2cU05c3BheS1UZU91eTAifSwieG1zX3RjZHQiOjE0MzczOTE1MDN9.dm_czmA02HpB3uRGs-kUSSW7QpYk9GzV_BAymkVtz6Q26oBHeVMiMNMofPkcOxCCLG5s0Irgzo98Bx5xnNPB_2ZRIg4ogEboYkzj2NAfePLoKQNWlYz-U6UBzu6bQTnPFP0MVVI-MK_trxJNfpP3J9kTVsKe_1_-z8FPwKOpjYwOkfuK-Ec8y5UJ0z1ffOI39ne3WZZ23o7xYATJAo3l0DoFk_ZI21gIHrn36Xlh9IuIGWLeJlUTpggZg1BWEeJH9fYRM-DJvWH65LbYuvmAVCERP-mzBMCK8Osirj09Inmu7LLx2_W1nhDu3BVZU2_j5ll_tk79L8LaHXPN6ZAcRw")
user_id = '716dbf1f-a356-4b89-9b87-b8f9bd8c321a'


"""
# Restore User Assigned Roles Methods

with open("./data/roles.json") as f:
    roles = loads(f.read())
    for role in roles:
        print(usr.assign_user_roles(user_id, role["roleDefinitionId"], {}))
"""


"""
# Restore Authentication Methods

with open("./data/authentication.json") as f:
    auth_methods = loads(f.read())
    for method in auth_methods:
        if method["@odata.type"] == "#microsoft.graph.phoneAuthenticationMethod":
            phone_payload = {
                "phoneNumber": method["phoneNumber"],
                "phoneType": "mobile",
                "smsSignInState": method["smsSignInState"]
            }
            print(usr.add_phone_authentication(user_id, phone_payload, {}))
        elif method["@odata.type"] == "#microsoft.graph.emailAuthenticationMethod":
            email_payload = {
                "emailAddress": method["emailAddress"]
            }
            print(usr.add_email_authentication(user_id, email_payload, {}))
"""

"""
# Restore Group Ownership
with open("./data/ownership.json") as f:
    ownership = loads(f.read())
    for group in ownership:
        if group["@odata.type"] == "#microsoft.graph.group":
            res = grp.add_owner(group["id"], user_id, {})
            print(res)
"""

"""
# Restore Group Membership
memberships = {}
with open("./data/membership.json") as f:
    memberships = loads(f.read())

def restore_membership(membership):
    if membership["@odata.type"] == "#microsoft.graph.group":
        res = grp.add_group_member(membership["id"], user_id, {})
        print(res)
    elif membership["@odata.type"] == "#microsoft.graph.directoryRole":
        print(usr.assign_user_roles(user_id, membership["roleTemplateId"], {}))
    elif membership["@odata.type"] == "#microsoft.graph.administrativeUnit":
        print(adm.add_user_to_administrative_unit(membership["id"],user_id,{}))


threads = [Thread(target=restore_membership, args=[membership]) for membership in memberships]
for thread in threads:
    thread.start()

"""


"""
# Restore User Licenses
with open("./data/license.json") as f:
    licenses = loads(f.read())
    for license in licenses:
        payload = {
            "addLicenses": [
                {
                    "disabledPlans": [],
                    "skuId": license["skuId"]
                }
            ],
            "removeLicenses": []
        }
        res = usr.assign_user_license(user_id, payload, {})
        print(res)
"""

"""
# Restore Applications for User
with open("./data/appRoleAssignments.json") as f:
    app_roles = loads(f.read())
    for role in app_roles:
        print(usr.assign_user_to_application(user_id, role["resourceId"], {}))
"""

"""
# Restore user owned devices
"""

# Check owner and member  explicitly
# with open("./data/devices.json") as f:
#     devices =  loads(f.read())
#     for device in devices:
#         payload = {
#             "accountEnabled": True,
#             "alternativeSecurityIds": [
#                 {
#                     "type": 2,
#                     "key": "21474836"
#                 }
#             ],
#             "deviceId": device["deviceId"],
#             "displayName": device["displayName"],
#             "operatingSystem": device["operatingSystem"],
#             "operatingSystemVersion": device["operatingSystemVersion"]
#         }
#         res = dvc.create_device(payload,{})
#         print(res)
#         # print(dvc.register_devices_owner(res["id"], user_id, {}))
#         break
        

dvc.update_device('2dc155b4-8d32-4b0a-bd87-96475798c3ed',{
    "accountEnabled": True
},{})

