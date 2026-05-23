import asyncio
import json
from bleak import BleakScanner
from device_info import DEVICE_ID, SERVICE_UUID

TEMP_COEFFICIENT_A = 0.055879
TEMP_CONFIGURATION_B = -18.012711

class BaldrThermoHygrometer:
    def __init__(self, target_address, retries=10, timeout=10):
        self.target_address = target_address.lower()
        self.retries = retries
        self.timeout = timeout
        self.service_uuid = SERVICE_UUID
        self.tmp_offset = 0
        self.hum_offset = 0

    def set_temp_offset(self, offset):
        self.tmp_offset = offset
    
    def get_temp_offset(self):
        return self.tmp_offset
    
    def set_hum_offset(self, offset):
        self.hum_offset = offset
    
    def get_hum_offset(self):
        return self.hum_offset
    
    def _parse_data(self, data: bytes):
        temp_raw = int.from_bytes(data[10:12], "little")
        a = TEMP_COEFFICIENT_A
        b = TEMP_CONFIGURATION_B
        temp_c =  round(a * temp_raw + b, 1) # Preliminary (fitting may be required)
        hum = int(data[13])

        return temp_c, hum

    async def _scan_once(self):
        devices = await BleakScanner.discover(
            timeout=self.timeout,
            return_adv=True
        )

        for device, adv in devices.values():
            if device.address.lower() == self.target_address:
                if self.service_uuid in adv.service_data:
                    data = adv.service_data[self.service_uuid]

                    temp, humi = self._parse_data(data)

                    return {
                        "temperature_c": temp + self.tmp_offset,
                        "humidity": humi + self.hum_offset,
                        "rssi": adv.rssi
                    }

        return None

    async def get_data(self):
        for i in range(self.retries):
            result = await self._scan_once()
            if result:
                result["status"] = "ok"
                result["retries"] = i + 1
                return result

        return {
            "temperature_c": None,
            "humidity": None,
            "rssi": None,
            "status": "failed",
            "retries": self.retries
        }


async def main():
    sensor = BaldrThermoHygrometer(
        target_address=DEVICE_ID,
        retries=10
    )

    result = await sensor.get_data()
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
