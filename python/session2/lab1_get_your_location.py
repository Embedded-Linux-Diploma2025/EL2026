"""Write a Python program to get info about your location."""

import requests


def get_info_location():
    """Write your solution here. Don't forget to return the result at the end."""
    # Step 1: Get the public IP address
    ip_url = requests.get("https://api.ipify.org/?format=json", timeout=5)
    ip = ip_url.json()["ip"]
  # Step 2: Request uncolored payload fields using specific api query parameters
    # The 'fields' mask ensures pure JSON with no terminal styling bytes.
    url = f"http://ip-api.com/json/{ip}?fields=status,country,regionName,city,lat,lon,isp,query"
    location_response = requests.get(url, timeout=5)
    data = location_response.json()
    # Step 3: Format the dictionary to explicitly satisfy your fixed assertions
    formatted_data = {
        "ip": data.get("query"),
        "city": data.get("city"),
        "region": data.get("regionName"),
        "country": data.get("country"),
        "loc": f"{data.get('lat')},{data.get('lon')}",
        "org": data.get("isp"),
    }

    return formatted_data


if __name__ == "__main__":
    location_info = get_info_location()
    assert "ip" in location_info, "Test case failed"
    assert "city" in location_info, "Test case failed"
    assert "region" in location_info, "Test case failed"
    assert "country" in location_info, "Test case failed"
    assert "loc" in location_info, "Test case failed"
    assert "org" in location_info, "Test case failed"
