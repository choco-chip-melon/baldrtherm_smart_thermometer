import asyncio
from bleak import BleakScanner
from device_info import DEVICE_ID, SERVICE_UUID

def callback(device, adv):
    if device.address.upper() == DEVICE_ID:
        print("=== FOUND ===")
        print("RSSI:", adv.rssi)  #
        print("Manufacturer:", adv.manufacturer_data)
        print("Service Data:", adv.service_data)
        
        data = adv.service_data[SERVICE_UUID]
        print("data: ", data.hex())

async def main():
    scanner = BleakScanner(callback)
    await scanner.start()
    await asyncio.sleep(15)
    await scanner.stop()

asyncio.run(main())
