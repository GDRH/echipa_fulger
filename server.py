#!/usr/bin/env python

# WS server that sends messages at random intervals

import asyncio
import datetime
import random
import websockets


def printmsg(msg):
    print (msg) 

async def time(websocket, path):
    async for message in websocket:
        printmsg(message)
        #await websocket.send(message)
        #now = datetime.datetime.utcnow().isoformat() + 'Z'
        #await websocket.send(now)

start_server = websockets.serve(time, '127.0.0.1', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
