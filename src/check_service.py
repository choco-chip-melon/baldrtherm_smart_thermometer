import asyncio
from bleak import BleakClient
from device_info import DEVICE_ID

async def main():
    async with BleakClient(DEVICE_ID) as client:
        services = client.services  

        for s in services:
            print(s.uuid)
            for c in s.characteristics:
                print("  ", c.uuid, c.properties)

asyncio.run(main())
