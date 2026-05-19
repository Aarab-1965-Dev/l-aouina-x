# -*- coding: utf-8 -*-
import os

def insert_field_operations():
    if not os.path.exists("index.html"):
        print("[-] خطأ: ملف index.html غير موجود!")
        return

    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()

    # صياغة واجهة العمليات الميدانية ومؤشرات البنية التحتية
    operations_html = """
        <div class="card" style="border-top: 4px solid #2e6f40; background: #ffffff; margin-top: 20px;">
            <h3>🗺️ غرفة العمليات الميدانية ومتابعة الأشغال</h3>
            <p>لوحة شفافة ومستقلة لرصد تقدم مشاريع البنية التحتية والموارد المائية في منطقة لـْعوينة:</p>
            
            <div style="margin-bottom: 15px; background: #fafafa; padding: 12px; border-radius: 6px; border-right: 4px solid #e76f51;">
                <div style="display: flex; justify-content: space-between; font-weight: bold; margin-bottom: 5px;">
                    <span>🌉 الترافع لبناء قنطرة لـْعوينة وفك العزلة</span>
                    <span style="color: #e76f51;">45% (مرحلة الدراسات والطلب المدني)</span>
                </div>
                <div style="background: #ddd; border-radius: 4px; height: 10px; width: 100%; overflow: hidden;">
                    <div style="background: #e76f51; height: 100%; width: 45%;"></div>
                </div>
                <p style="font-size: 0.85rem; color: #666; margin: 5px 0 0 0;">الحالة الحالية: صياغة المراسلات الموجهة للمجالس المحلية وتوثيق حاجة الساكنة الميدانية الملحة للمنشأة الفنية.</p>
            </div>

            <div style="margin-bottom: 15px; background: #fafafa; padding: 12px; border-radius: 6px; border-right: 4px solid #3d5a80;">
                <div style="display: flex; justify-content: space-between; font-weight: bold; margin-bottom: 5px;">
                    <span>🚰 صيانة قنوات السقي وحماية مياه البئر الجوفية</span>
                    <span style="color: #3d5a80;">90% (مستقر ومراقب بكفاءة)</span>
                </div>
                <div style="background: #ddd; border-radius: 4px; height: 10px; width: 100%; overflow: hidden;">
                    <div style="background: #3d5a80; height: 100%; width: 90%;"></div>
                </div>
                <p style="font-size: 0.85rem; color: #666; margin: 5px 0 0 0;">الحالة الحالية: حراسة وتتبع منسوب العين والآبار بالتنسيق المدني المستدام لضمان عدالة التوزيع للكسيبة والفلاحة.</p>
            </div>

            <div style="margin-bottom: 5px; background: #fafafa; padding: 12px; border-radius: 6px; border-right: 4px solid #2e6f40;">
                <div style="display: flex; justify-content: space-between; font-weight: bold; margin-bottom: 5px;">
                    <span>🌴 حملة تطعيم الأشجار (التين، الزيتون، اللوز، الحمضيات)</span>
                    <span style="color: #2e6f40;">75% (موسم النمو والتتبع الحركي)</span>
                </div>
                <div style="background: #ddd; border-radius: 4px; height: 10px; width: 100%; overflow: hidden;">
                    <div style="background: #2e6f40; height: 100%; width: 75%;"></div>
                </div>
                <p style="font-size: 0.85rem; color: #666; margin: 5px 0 0 0;">الحالة الحالية: رصد ومتابعة تطعيم الأصناف الممتازة وحماية رطوبة التربة المحيطة بالجذور من التبخر.</p>
            </div>
        </div>
    """

    # دمج القسم الجديد فوق الـ footer لضمان بقائه في ذيل اللوحات وبشكل منسق
    if "</footer>" in content and "غرفة العمليات الميدانية" not in content:
        updated_content = content.replace("<footer>", operations_html + "\n    <footer>")
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(updated_content)
        print("[✓] تم دمج غرفة العمليات الميدانية بنجاح داخل الواجهة!")
    else:
        print("[!] القسم مدمج مسبقاً أو تعذر العثور على نقطة الترقيع المناسبة.")

if __name__ == "__main__":
    insert_field_operations()
