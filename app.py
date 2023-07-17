from fastapi import FastAPI
from endpoint.endpoint import router as smit_router
from model.model import init
import asyncio
from uvicorn import Config, Server

loop = asyncio.new_event_loop()
loop.run_until_complete(init())

app_test = FastAPI() 

app_test.include_router(smit_router)

if __name__ == "__main__":
    config = Config(app=app_test, loop=loop, host="0.0.0.0")
    server = Server(config)
    loop.run_until_complete(server.serve())
    loop.close()