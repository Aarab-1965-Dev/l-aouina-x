import requests
from skyfield.api import load, EarthSatellite
from datetime import datetime

print("[-] Connecting to Celestrak Satellite Server...")
url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle"

try:
    response = requests.get(url, timeout=15)
    if response.status_code == 200:
        lines = response.text.strip().split('\n')
        
        target_satellite = "ISS (ZARYA)" 
        sat_data = []
        
        for i in range(0, len(lines), 3):
            if i+2 < len(lines):
                name = lines[i].strip()
                tle1 = lines[i+1].strip()
                tle2 = lines[i+2].strip()
                if target_satellite in name:
                    sat_data = [name, tle1, tle2]
                    break

        if sat_data:
            ts = load.timescale()
            t = ts.now()
            satellite = EarthSatellite(sat_data[1], sat_data[2], sat_data[0], ts)
            
            geocentric = satellite.at(t)
            subpoint = geocentric.subpoint()
            
            print("\n🛰️  [ SATELLITE LIVE DATA ] 🛰️")
            print(f"Name      : {sat_data[0]}")
            print(f"Time (UTC): {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Latitude  : {subpoint.latitude.degrees:.4f}°")
            print(f"Longitude : {subpoint.longitude.degrees:.4f}°")
            print(f"Altitude  : {subpoint.elevation.km:.2f} km")
        else:
            print("[!] Satellite not found in active list.")
    else:
        print("[!] Server error, status code:", response.status_code)
except Exception as e:
    print("[!] Connection error:", e)
import requests
from skyfield.api import load, EarthSatellite
from datetime import datetime

print("⏳ جاري جلب بيانات الأقمار الاصطناعية المباشرة من الخادم...")
url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle"

try:
    response = requests.get(url, timeout=15)
    if response.status_code == 200:
        lines = response.text.strip().split('\n')
        
        # سنبحث عن قمر مشهور كمثال للبث المباشر
        target_satellite = "ISS (ZARYA)" 
        sat_data = []
        
        for i in range(0, len(lines), 3):
            if i+2 < len(lines):
                name = lines[i].strip()
                tle1 = lines[i+1].strip()
                tle2 = lines[i+2].strip()
                if target_satellite in name:
                    sat_data = [name, tle1, tle2]
                    break

        if sat_data:
            ts = load.timescale()
            t = ts.now()
            satellite = EarthSatellite(sat_data[1], sat_data[2], sat_data[0], ts)
            
            geocentric = satellite.at(t)
            subpoint = geocentric.subpoint()
            
            print("\n🛰️ [ تم جلب البيانات المباشرة بنجاح ] 🛰️")
            print(f"🔹 اسم القمر: {sat_data[0]}")
            print(f"🔹 الوقت الحالي: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"📍 خط العرض: {subpoint.latitude.degrees:.4f}°")
            print(f"📍 خط الطول: {subpoint.longitude.degrees:.4f}°")
            print(f"📏 الارتفاع: {subpoint.elevation.km:.2f} كلم")
        else:
            print("لم يتم العثور على القمر المحدد في قائمة الأقمار النشطة حالياً.")
    else:
        print("فشل الاتصال بالخادم، رمز الاستجابة:", response.status_code)
except Exception as e:
    print("حدث خطأ أثناء جلب البيانات المباشرة:", e)
