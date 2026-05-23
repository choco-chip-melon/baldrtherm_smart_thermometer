import asyncio
from bleak import BleakScanner
from device_info import DEVICE_ID, SERVICE_UUID

TEMP_COEFFICIENT_A = 0.055879
TEMP_CONFIGURATION_B = -18.012711
TEMP_OFFSET = 0

def callback(device, adv):
    if device.address.upper() == DEVICE_ID:
        print("=== FOUND ===")
        print("RSSI:", adv.rssi)  #
        print("Manufacturer:", adv.manufacturer_data)
        print("Service Data:", adv.service_data)
        
        data = adv.service_data[SERVICE_UUID]
        print("data: ", data.hex())

        temp_raw = int.from_bytes(data[10:12], "little")
        print("temp_raw: ", temp_raw)
        
        temp =  round(TEMP_COEFFICIENT_A* temp_raw + TEMP_CONFIGURATION_B, 1) + TEMP_OFFSET # 
        print("temp: ", temp)

        hum_raw = data[13]
        print("hum : ", hum_raw)

        print()

async def main():
    scanner = BleakScanner(callback)
    await scanner.start()
    await asyncio.sleep(15)
    await scanner.stop()

asyncio.run(main())
