import math
from datetime import datetime

# إحداثيات المحطة الأرضية الأساسية بالعوينة
h_lat, h_lon = 29.6874, -9.7317

db = {
    'Radar & Water Detection': [
        ('SENTINEL-1A (ESA)', 'SAR Radar', 31.2, -8.1, '📡 رادار يخترق السحب: مثالي لمراقبة رطوبة التربة الجوفية وتدفق المياه في الواحة.'),
        ('NASA GRACE-FO 1', 'Gravity Wave', 24.5, -11.3, '💧 مستشعر الجاذبية: يقيس التغير في مخزون المياه الجوفية وعيون الماء المحلية.'),
        ('SMAP (NASA)', 'Radiometer', 27.3, -9.1, '🌱 رطوبة السطح: مؤشر حاسم لمعرفة أنسب الأوقات لحرث الأرض وتجهيز التربة.')
    ],
    'Minerals & Geology Identification': [
        ('LANDSAT 9 (NASA)', 'SWIR/Thermal', 29.95, -9.6, '🌳 المسح الحراري الطيفي: ممتاز لمتابعة صحة أشجار التين واللوز ومعالجة الإجهاد المائي.'),
        ('SENTINEL-2B (ESA)', 'Multi-spectral', 28.1, -10.2, '🍃 الغطاء النباتي: يعطي مؤشر النماء الرعوي ومتابعة جودة الغطاء الأخضر محلياً.')
    ],
    'Archaeological & Truffle Fields': [
        ('TERRASAR-X (DLR)', 'X-band Radar', 30.5, -9.1, '🍄 رادار الأعماق الدقيق: يمسح التغيرات الجيولوجية الخفيفة، ويساعد في تحديد بيئة نمو الترفاس مع ظهور نبات الأروص.')
    ]
}

html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>L'Aouina Ethical Super Intelligence Server 2026</title>
    <style>
        body {{ font-family: sans-serif; background: #0f172a; color: #e2e8f0; padding: 20px; }}
        .container {{ max-width: 800px; margin: 0 auto; background: #1e293b; padding: 20px; border-radius: 12px; }}
        h1 {{ text-align: center; color: #38bdf8; font-size: 1.25rem; }}
        .meta {{ background: #0f172a; padding: 15px; border-radius: 8px; border-right: 4px solid #38bdf8; margin-bottom: 20px; }}
        .cat {{ margin-top: 20px; background: #334155; padding: 8px; border-radius: 6px; font-weight: bold; }}
        .card {{ background: #1e293b; border: 1px solid #334155; padding: 15px; margin: 10px 0; border-radius: 8px; }}
        .header {{ display: flex; justify-content: space-between; color: #fbbf24; font-weight: bold; }}
        .tip {{ margin-top: 8px; color: #34d399; background: #0f172a; padding: 8px; border-radius: 4px; font-size: 14px; }}
    </style>
</head>
<body>
<div class="container">
    <h1>🛰️ L'Aouina Ethical Super Intelligence Server 2026 🛰️</h1>
    <div class="meta">
        <p>📍 <b>المحطة الأرضية:</b> العوينة، تيزنيت ({h_lat} , {h_lon})</p>
        <p>📊 <b>وقت التحديث لجيو-الفضاء:</b> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
        <p>🟢 <b>حالة النظام:</b> LIVE ECO-JUGGERNAUT ACTIVE</p>
    </div>
'''

for cat, sats in db.items():
    html += f'<div class="cat">📂 {cat}</div>'
    for name, sens, s_lat, s_lon, tip in sats:
        r_lat1, r_lon1, r_lat2, r_lon2 = map(math.radians, [h_lat, h_lon, s_lat, s_lon])
        d = 2 * 6371.0 * math.asin(math.sqrt(math.sin((r_lat2 - r_lat1)/2)**2 + math.cos(r_lat1) * math.cos(r_lat2) * math.sin((r_lon2 - r_lon1)/2)**2))
        html += f'''<div class="card">
            <div class="header"><span>🔹 {name}</span><span>المسافة الحالية: {d:.1f} كم</span></div>
            <div>مستشعر الرصد: {sens}</div>
            <div class="tip">{tip}</div>
        </div>'''

html += '</div></body></html>'
open('index.html', 'w', encoding='utf-8').write(html)
print('[+] SUCCESS: index.html generated properly!')
