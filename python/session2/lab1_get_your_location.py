"""Write a Python program to get info about your location."""

import requests


def get_info_location():
    """Write your solution here. Don't forget to return the result at the end."""
    url = requests.get("https://api.ipify.org/?format=json", timeout=10)
    place = requests.get(f"https://ipinfo.io/{url.json()["ip"]}/geo", timeout=10)
    # for key, value in place.json().items():
    #     print(f"{key}: {value}")
    return place.json()

get_info_location()

if __name__ == "__main__":
    location_info = get_info_location()
    assert "ip" in location_info, "Test case failed"
    assert "city" in location_info, "Test case failed"
    assert "region" in location_info, "Test case failed"
    assert "country" in location_info, "Test case failed"
    assert "loc" in location_info, "Test case failed"
    assert "org" in location_info, "Test case failed"
