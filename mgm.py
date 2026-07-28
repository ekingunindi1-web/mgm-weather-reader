from playwright.sync_api import sync_playwright


def get_weather(city):
    """
    Bir şehir için hava durumu verilerini döndürür.

    Dönen değer:
    {
        "city": "...",
        "current": "...",
        "tomorrow_min": "...",
        "tomorrow_max": "..."
    }
    """

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-setuid-sandbox"
            ]
        )

        page = browser.new_page(
            viewport={"width": 1600, "height": 3000}
        )

        # Şimdilik test amacıyla
        page.goto("https://mgm.gov.tr")

        print(f"{city} sayfası açıldı.")

        browser.close()

    return {
        "city": city,
        "current": "",
        "tomorrow_min": "",
        "tomorrow_max": ""
    }