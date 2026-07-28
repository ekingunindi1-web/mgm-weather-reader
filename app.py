from playwright.sync_api import sync_playwright
from openpyxl import Workbook
from urllib.parse import quote

CITIES = [
    "ADANA",
    "ANKARA",
    "ANTALYA",
    "AYDIN",
    "BALIKESİR",
    "BİLECİK",
    "BOLU",
    "BURSA",
    "ÇANAKKALE",
    "ÇORUM",
    "DENİZLİ",
    "DİYARBAKIR",
    "DÜZCE",
    "ERZURUM",
    "ESKİŞEHİR",
    "GAZİANTEP",
    "HATAY",
    "İSTANBUL",
    "İZMİR",
    "KAYSERİ",
    "KIRIKKALE",
    "KIRKLARELİ",
    "KOCAELİ",
    "KONYA",
    "MANİSA",
    "MERSİN",
    "MUĞLA",
    "SAKARYA",
    "SAMSUN",
    "ŞANLIURFA",
    "TEKİRDAĞ",
    "TRABZON",
    "UŞAK"
]

BASE_URL = "https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il={}"

wb = Workbook()
ws = wb.active
ws.title = "MGM"

ws.append([
    "İl",
    "Anlık Sıcaklık",
    "Yarın En Düşük",
    "Yarın En Yüksek"
])

with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)

    page = browser.new_page(
        viewport={"width": 1600, "height": 3000}
    )

    for city in CITIES:

        try:

            print(f"{city} okunuyor...")

            url = BASE_URL.format(quote(city))

            page.goto(url, wait_until="networkidle")
            page.wait_for_timeout(2000)

            current = page.locator(
                'div[ng-bind*="sondurum[0].sicaklik"]'
            ).inner_text().strip()

            tomorrow_min = page.locator(
                'td[ng-bind*="enDusukGun2"]'
            ).inner_text().strip()

            tomorrow_max = page.locator(
                'td[ng-bind*="enYuksekGun2"]'
            ).inner_text().strip()

            ws.append([
                city,
                current,
                tomorrow_min,
                tomorrow_max
            ])

            print(f"✓ {city}: {current}°C")

        except Exception as e:

            print(f"✗ {city}: HATA -> {e}")

            ws.append([
                city,
                "HATA",
                "HATA",
                "HATA"
            ])

    browser.close()

wb.save("weather.xlsx")

print("\nİşlem tamamlandı.")
print("weather.xlsx oluşturuldu.")