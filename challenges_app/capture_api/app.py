import datetime
import requests


def get_nine_day_forecast():
    url = "https://pda.weather.gov.hk/locspc/data/fnd_uc.xml"
    response = requests.get(url)
    assert response.status_code == 200
    response_data = response.json()
    return response_data


def get_forecast_detail(data: dict):
    return data["forecast_detail"]


if __name__ == "__main__":
    timedelta = 2
    data = get_nine_day_forecast()
    forecast_detail_data = get_forecast_detail(data)
    print(f"{forecast_detail_data[timedelta]['min_rh']} - {forecast_detail_data[timedelta]['max_rh']}%")
