#!/usr/bin/python3
"""Alta3 Research | <your name here>
   Using an HTTP GET to determine when the ISS will pass over head"""

# python3 -m pip install requests
import requests

ISSURL = "http://api.open-notify.org/iss-pass.json"

def main():
    """your code goes below here"""
    
    # stuck? you can always write comments
    # Try describe the steps you would take manually
    ISSURL = "http://api.open-notify.org/iss-pass.json"
    lat = 41.9
    lon = -87.6
    iss = requests.get(f"{ISSURL}?lat={lat}&lon={lon}")
    iss = iss.json()
    
    overhead = []

    for i in iss.get("response"):
        overhead.append(iss)

    print(overhead)


if __name__ == "__main__":
    main()

