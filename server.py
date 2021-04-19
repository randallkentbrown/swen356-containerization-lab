from aiohttp import web
import json

CONFIG_ROUTE = "./config.json"
DATA_ROUTE = "./data.json"

DATA_KEY = "data"
HOST_KEY = "host"
PORT_KEY = "port" #sadly, not boot

def get_config():
    with open(CONFIG_ROUTE) as config_file:
        config = json.load(config_file)
        return config
        
async def say_hello(request):
    return web.Response(
        text="Hello, world!"
    )
        
async def get_data(request):
    if DATA_KEY in request.query:
        requested_key = request.query[DATA_KEY]
        with open(DATA_ROUTE) as data_file:
            data = json.load(data_file)
            if requested_key in data:
                return web.Response(
                    text=f"{data[requested_key]}"
                )
            else:
                return web.Response(
                    text=f"{requested_key} is not a key in {DATA_ROUTE}"
                )
    else:
        web.Response(
            text=f"The request is missing the query parameter {DATA_KEY}"
        )

config = get_config()
server = web.Application()
server.router.add_routes([web.get('/hello', say_hello)])
server.router.add_routes([web.get('/data', get_data)])

web.run_app(server, host=config[HOST_KEY], port=int(config[PORT_KEY]))