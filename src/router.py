from routes.stmt import *



def router(method, path, body={}):
    route = path[1:]
    payload = None

    if route == '/':
        payload = "Welcome to Regalia API. Version:0.1 Alpha, BuildDate:30062021"
    elif route == 'whoareyou':
        payload = "I'm Regalia API."
    elif route == 'version':
        payload = "Version:0.1 Alpha, BuildDate:30/06/2021"
    elif route == 'whoisyourmaker':
        payload = "Tanbin"
    elif route == 'whatyoudo':
        payload = "Im a bypass api that work for Standard Bank Agent Banking"
    elif route == 'stmt':
        payload = stmt(method, path)
    return payload
