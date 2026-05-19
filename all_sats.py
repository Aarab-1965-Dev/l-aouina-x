import requests

print("⏳ Connecting to Space-Track / Celestrak Server...")
# رابط جلب البيانات الكاملة لجميع الأقمار الاصطناعية النشطة في الفضاء
url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle"

try:
    response = requests.get(url, timeout=20)
    if response.status_code == 200:
        lines = response.text.strip().split('\n')
        total_satellites = len(lines) // 3
        
        # حفظ كل البيانات في ملف نصي منظم داخل الهاتف
        filename = "all_satellites_database.txt"
        with open(filename, "w") as file:
            file.write(response.text)
            
        print("\n✅ [ DATABASE UPDATED SUCCESSFULY ]")
        print(f"🔹 Total Active Satellites Found: {total_satellites}")
        print(f"🔹 Database saved as: {filename}")
        print("[-] You can now search for (Sentinel, NOAA, LANDSAT) inside the file.")
        
    else:
        print("[!] Server returned error status:", response.status_code)
except Exception as e:
    print("[!] Failed to fetch global satellite data:", e)
