from cities import CITIES
from mgm import get_weather
from excel_utils import save_to_excel


def main():

    results = []

    for city in CITIES:
        print(f"{city} okunuyor...")

        data = get_weather(city)
        results.append(data)

    save_to_excel(results)


if __name__ == "__main__":
    main()