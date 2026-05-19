# -*- coding: utf-8 -*-

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# التأكد من عدم تكرار القسم إذا كان موجوداً
if "لوحة التحكم الحية: الواحة الذكية" not in content:
    
    oasis_html = """
        <div class="card" style="border-top: 4px solid #81b29a; background: #ffffff; padding: 20px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
            <h3 style="color: #2e6f40; margin-top: 0;">🌱 لوحة التحكم الحية: الواحة الذكية والموارد المائية</h3>
            <p>مؤشرات فحص المستشعرات الرقمية للمياه والتربة في أراضي الجماعة والقبيلة لـ LAAWAYNA-X:</p>
            
            <div style="display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 15px;">
                <div style="flex: 1; min-width: 200px; background: #f4f7f5; border-right: 4px solid #2e6f40; padding: 10px; border-radius: 4px;">
                    <strong>🚰 منسوب مياه البئر الجوفية:</strong> 85% (مستقر)
                </div>
                <div style="flex: 1; min-width: 200px; background: #f4f7f5; border-right: 4px solid #2e6f40; padding: 10px; border-radius: 4px;">
                    <strong>💧 نظام الري بالتنقيط:</strong> مستقر ومؤتمت
                </div>
                <div style="flex: 1; min-width: 200px; background: #f4f7f5; border-right: 4px solid #2e6f40; padding: 10px; border-radius: 4px;">
                    <strong>🪴 رطوبة التربة العامة:</strong> 68% (مثالي)
                </div>
            </div>
            
            <h4 style="color: #3d5a80; margin-bottom: 8px;">📋 تقرير حالة الغطاء النباتي والأشجار المثمرة الممتازة:</h4>
            <ul style="padding-right: 20px; margin-top: 0;">
                <li><strong>التين (الحمري والخضاري):</strong> حالة ممتازة - ري دوري منظم لتجهيز موسم الثمار</li>
                <li><strong>الزيتون المحلي الأصيل:</strong> حالة ممتازة - التجهيز لموسم التسميد العضوي</li>
                <li><strong>أشجار اللوز المحمية:</strong> مستقرة - تقليم دوري مكتمل بنجاح</li>
                <li><strong>الحمضيات (الليمون والبرتقال):</strong> حالة جيدة - مراقبة دقيقة لرطوبة التربة المحيطة</li>
            </ul>
        </div>
    """
    
    # وضع القسم مباشرة فوق بداية الـ footer لضمان التناسق
    if "<footer>" in content:
        updated_content = content.replace("<footer>", oasis_html + "\n    <footer>")
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(updated_content)
        print("[✓] تم دمج لوحة الواحة الذكية في واجهة الموقع بنجاح يدوياً!")
    else:
        print("[-] لم يتم العثور على وسم footer في الملف.")
else:
    print("[✓] القسم مدمج بالفعل في واجهة الموقع!")
