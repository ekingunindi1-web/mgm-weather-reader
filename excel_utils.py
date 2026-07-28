from openpyxl import Workbook


def save_to_excel(weather_data, filename="weather.xlsx"):
    wb = Workbook()
    ws = wb.active
    ws.title = "Hava Durumu"

    # Başlıklar
    ws.append([
        "İl",
        "Anlık Sıcaklık (°C)",
        "Yarın En Düşük (°C)",
        "Yarın En Yüksek (°C)"
    ])

    # Veriler
    for row in weather_data:
        ws.append([
            row["city"],
            row["current"],
            row["tomorrow_min"],
            row["tomorrow_max"]
        ])

    wb.save(filename)
    print(f"\n✅ Excel dosyası oluşturuldu: {filename}")