import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "7Oqsg95xwiZOxPVO4WzH8xClWqjL6IDX"  # Replace with your API key

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break

    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break

    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    print("URL: " + url)

    # Send a request to the MapQuest API
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        # Extract route information from the JSON response
        route = json_data["route"]
        legs = route["legs"][0]
        maneuvers = legs["maneuvers"]
        distance_miles = route["distance"]
        distance_kilometers = distance_miles * 1.61

        print("API Status: " + str(json_status) + " = A successful route call.")
        print("=============================================")
        print("Directions from " + orig + " to " + dest)
        print("Trip Duration:   " + route["formattedTime"])
        print("Miles:           " + str(distance_miles))
        print("Kilometers:      " + str("{:.2f}".format(distance_kilometers)))
        print("=============================================")

        # Display the step-by-step directions
        for i, maneuver in enumerate(maneuvers):
            print(f"{i + 1}. {maneuver['narrative']} ({maneuver['distance']} miles / {maneuver['distance'] * 1.61:.2f} km)")

        print("=============================================\n")

        # Additional enhancements:
        # You can add more features here, such as displaying highway, bridge, and tunnel information.

    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Status Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")