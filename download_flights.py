import requests
import zipfile
import io
import os
import time

# Create data folder
os.makedirs("data", exist_ok=True)

years  = [2019, 2020, 2021, 2022, 2023, 2024, 2025]
months = range(1, 13)

base_url = "https://transtats.bts.gov/PREZIP/On_Time_Reporting_Carrier_On_Time_Performance_1987_present_{year}_{month}.zip"

downloaded = 0
failed     = []

for year in years:
    for month in months:
        filename = f"data/flights_{year}_{month:02d}.csv"

        if os.path.exists(filename):
            print(f"⏭️  {year}-{month:02d} already exists — skipping")
            downloaded += 1
            continue

        url = base_url.format(year=year, month=month)
        print(f"📥 Downloading {year}-{month:02d}...", end=" ", flush=True)

        try:
            response = requests.get(url, timeout=120)

            if response.status_code == 200:
                z = zipfile.ZipFile(io.BytesIO(response.content))
                csv_name = [n for n in z.namelist() if n.endswith(".csv")][0]

                with z.open(csv_name) as zf:
                    with open(filename, "wb") as f:
                        f.write(zf.read())

                size_mb = os.path.getsize(filename) / 1e6
                print(f"✅ {size_mb:.1f} MB")
                downloaded += 1

            else:
                print(f"⚠️ Status {response.status_code} — not available")
                failed.append(f"{year}-{month:02d}")

        except Exception as e:
            print(f"❌ {e}")
            failed.append(f"{year}-{month:02d}")

        time.sleep(1)  # be polite to the server

print(f"\n🎉 Done — {downloaded} files downloaded")
if failed:
    print(f"⚠️  Not available: {failed}")