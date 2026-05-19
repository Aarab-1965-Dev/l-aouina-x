# إضافة زر نداء الواحة للواجهة
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

sos_button = """
<div style="margin-top: 15px; padding: 15px; background: #fff0f0; border: 2px dashed #d00000; border-radius: 8px; text-align: center;">
    <h4 style="color: #d00000; margin: 0 0 10px 0;">🚨 نداء الواحة (SOS)</h4>
    <p style="font-size: 0.9rem;">هل رصدت عطلاً ميدانياً؟ أرسل تنبيهاً فورياً لفريق الصيانة الميداني:</p>
    <button onclick="alert('تم استلام التنبيه الميداني بنجاح! سيتم فحص بئر الجمعية أو المسلك فوراً.')" 
            style="background: #d00000; color: white; border: none; padding: 10px 20px; border-radius: 5px; font-weight: bold; cursor: pointer;">
        إرسال تنبيه عاجل
    </button>
</div>
"""
if "🚨" not in content:
    updated = content.replace("", sos_button + "\n")
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(updated)
    print("[✓] تم دمج ميزة نداء الواحة (SOS) بنجاح!")
