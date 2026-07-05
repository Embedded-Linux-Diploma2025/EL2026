"""Write a Python program to get info about your location."""

import requests


def get_info_location():
    """Write your solution here. Don't forget to return the result at the end."""
    url = "https://ipapi.co/json/"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        custom_data = {
            "ip": data.get("ip"),
            "city": data.get("city"),
            "region": data.get("region"),
            "country": data.get("country"),
            "loc": f"{data.get('latitude')},{data.get('longitude')}",  # بيدمج الإحداثيات زي ipinfo
            "org": data.get("org"),
        }
        return custom_data
    except requests.exceptions.RequestException:
        return {"ip": "", "city": "", "region": "", "country": "", "loc": "", "org": ""}


if __name__ == "__main__":
    location_info = get_info_location()
    assert "ip" in location_info, "Test case failed"
    assert "city" in location_info, "Test case failed"
    assert "region" in location_info, "Test case failed"
    assert "country" in location_info, "Test case failed"
    assert "loc" in location_info, "Test case failed"
    assert "org" in location_info, "Test case failed"
