audio_player = """
<div style="margin-top: 15px; padding: 15px; background: #eef5f0; border-radius: 8px;">
    <h4>📻 مكتبة الأذان الرقمية</h4>
    <audio controls style="width: 100%;">
        <source src="adhan.mp3" type="audio/mpeg">
        متصفحك لا يدعم مشغل الصوت المدمج.
    </audio>
</div>
"""
# دمج المشغل في صفحة الـ index
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()
if "📻" not in content:
    updated = content.replace("<h3>🎛️ لوحة مفاتيح المنصة", audio_player + "\n<h3>🎛️ لوحة مفاتيح المنصة")
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(updated)
    print("[✓] تم دمج مكتبة الصوت الرقمية!")
