import requests

# Mike Shalaby
# Module: 9 Assignment 9.2 - CSD325
# Bellevue University

API = "https://api.zippopotam.us/us/"
WELCOME_MSG = "Hello! Please enter a United States ZIP code to get started."


def get_loc_info(loc):
    country = loc.get("country")
    place = loc["places"][0]
    city = place.get("place name")
    state = place.get("state")
    zip_code = loc.get("post code")

    print(f"Here is the requested information for: {zip_code}\n"
          f"City: {city}\n"
          f"State: {state}\n"
          f"Country: {country}\n")


def main():
    while True:
        print(WELCOME_MSG)
        zip_code = input(">> ").strip()
        zip_response = requests.get(API + zip_code)

        if zip_response.status_code == 200:
            get_loc_info(zip_response.json())
        elif zip_response.status_code == 404:
            print(f"The ZIP code entered: {zip_code} was not found.\nError: {zip_response.status_code}\nPlease try "
                  f"again.")
        else:
            print(f"An error has occurred! Error: {zip_response.status_code}\nPlease try again.")


main()
