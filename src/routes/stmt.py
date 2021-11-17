import json

from src.db import execute

schema = 'AGENT_BANKING'

#
# def stm(method, path, body={}):
#     query = ''''''
#
#     if method == 'GET':
#
#         query = f'''SELECT * FROM {schema}.reginfo'''
#
#     elif method == 'POST':
#         query = f'''SELECT * FROM {schema}.reginfo'''
#
#     # elif method == 'PUT':
#     #     query = f'''UPDATE {schema} SET `Name` = "{body["name"]}" WHERE {schema}.`ID` = {body["id"]};'''
#     # elif method == 'PATCH':
#     #     query = f'''UPDATE {schema} SET `{body["name"]}` = "{body["value"]}" WHERE {schema}.`ID` = {body["id"]}'''
#     # elif method == 'DELETE':
#     #     query = f'''DELETE FROM {schema} WHERE {schema}.`ID` = {body["id"]}'''
#
#     payload = execute(query)
#     print(payload)
#     return json.dumps(payload, indent=4)



def stmt(method, path, body={}):
    print('Process now accessing resource massage')
    query = ''''''

    if method == 'GET':
        query = query = f'''SELECT * FROM {schema}.reginfo'''
        print(query)
        payload = execute(query)
        return json.dumps(payload, indent=4)
