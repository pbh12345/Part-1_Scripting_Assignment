import requests
import sys


def mac_detailer(mac):
    url = "https://api.macaddress.io/v1"
    payload = {"search": mac}
    headers = {"X-Authentication-Token": "at_1QGwf7yBnfrFCU6sd8GEgqWOGKUCo"}
    data = requests.get(url=url, params=payload, headers=headers)
    return data.text


if __name__ == "__main__":
    mac_address = sys.argv[1]
    company_name = mac_detailer(mac_address)
    print(company_name)

