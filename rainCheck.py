import requests
import sys


def checkDateInBetween(startDate, endDate, currDate) :
    if startDate <= currDate and currDate <= endDate:
        return True
    return False

def rain_check(startDate, endDate, cityName):
    
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={cityName}&appid=1f381c8b0af1955d40ae9971ccdbb09b"
    try:
        response = requests.get(url)
    except:
        print("Failed to Fetch data. Please Fix the API!")
        sys.exit(1)
    # print(response.status_code)
    if response.status_code == 200 :
        data = response.json()
        for weather in data['list']:
            if checkDateInBetween(startDate, endDate, weather['dt_txt'][:10]):
                if 'rain' in weather:
                
                
                
                    return True
        return False
    else: 
        print("Failed to Fetch data. Please Try Again!")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Give Proper Inputs in the Format : StartDate, EndDate, CityName")
        sys.exit(1)
    startDate = sys.argv[1]
    endDate = sys.argv[2]
    cityName = sys.argv[3]
    if(rain_check(startDate, endDate, cityName)):
        print("ShouldTakeUmbrella")
    else: 
        print("NoNeedOfUmbrella")
