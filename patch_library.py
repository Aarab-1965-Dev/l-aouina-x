# -*- coding: utf-8 -*-
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

library_html = """
<div class="card" style="border-top: 4px solid #b58900; background: #fffdf0; margin-top: 20px; padding: 15px; border-radius: 8px;">
    <h3>📚 المكتبة العلمية الموسوعية</h3>
    <p>مرجع شامل لأمهات كتب التفسير والحديث النبوي الشريف لخدمة الباحثين وطلاب العلم:</p>
    
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
        <div style="background: #fdf6e3; padding: 10px; border-radius: 5px;">
            <h4 style="color: #859900;">📖 موسوعة التفسير</h4>
            <ul style="padding-right: 20px; font-size: 0.9rem;">
                <li>تفسير الطبري (جامع البيان)</li>
                <li>تفسير ابن كثير (القرآن العظيم)</li>
                <li>القرطبي (الجامع لأحكام القرآن)</li>
            </ul>
        </div>
        
        <div style="background: #fdf6e3; padding: 10px; border-radius: 5px;">
            <h4 style="color: #268bd2;">✨ موسوعة الحديث</h4>
            <ul style="padding-right: 20px; font-size: 0.9rem;">
                <li>صحيح البخاري</li>
                <li>صحيح مسلم</li>
                <li>سنن الترمذي / أبي داود</li>
            </ul>
        </div>
    </div>
    <p style="font-size: 0.8rem; color: #555; margin-top: 10px;">نظام المكتبة مجهز للوصول السريع للمصادر المعتمدة.</p>
</div>
"""

# دمج القسم الجديد في الواجهة
if "📚" not in content:
    updated = content.replace("<h3>🎛️ لوحة مفاتيح المنصة", library_html + "\n<h3>🎛️ لوحة مفاتيح المنصة")
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(updated)
    print("[✓] تم دمج المكتبة العلمية في المنصة بنجاح!")
