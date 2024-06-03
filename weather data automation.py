import requests

def WEATHER_DATA():
    api_key = "22c205bf90f1b5ce6006f4a355ffbe1f"
    api_url = "https://api.openweathermap.org/data/2.5/weather"
    City = input("please mention the city: ").lower()
    response = requests.get(
        url=api_url,
        params={
            "q": City,
            "appid": api_key,
             "units": "metric"}
    )

    Weather_data = response.json()
    print(Weather_data["main"]['temp'])

while True:
    WEATHER_DATA()
    USER = input("Do you want to search again?(Y/N) ").lower()
    if USER != "y":
        print("Thanks,come again!")
        break


