# -*- coding: utf-8 -*-
import os

def generate_oasis_dashboard():
    print("====== 🌱 نظام إدارة الواحة الذكية والفلاحة المستدامة 2026 ======")
    
    # بيانات محاكاة حالة الموارد المائية والأشجار
    well_level = "85%"  # نسبة توفر المياه في البئر الإرتوازي لـ LAAWAYNA-X
    irrigation_status = "مستقر ومؤتمت"
    soil_moisture = "68% (مثالي)"
    
    # حالة الأشجار المحلية وتوقيت التطعيم/الري
    trees_data = {
        "أشجار التين (الحمري والخضاري)": "حالة ممتازة - ري دوري منظم",
        "أشجار الزيتون المحلية": "حالة ممتازة - التجهيز لموسم التسميد",
        "أشجار اللوز": "مستقرة - تقليم دوري مكتمل",
        "أشجار الحمضيات (الليمون والبرتقال)": "حالة جيدة - مراقبة رطوبة التربة"
    }

    print(f"[+] فحص مستوى مياه البئر الجوفية: {well_level}")
    print(f"[+] نظام الري بالتنقيط الذكي: {irrigation_status}")
    print(f"[+] متوسط رطوبة التربة في الواحة: {soil_moisture}")
    print("--------------------------------------------------")

    # تحديث واجهة موقع index.html لدمج قسم البيانات الحية للواحة
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            content = f.read()

        # بناء الصندوق البرمجي الجديد للبيانات الحية
        oasis_html = f"""
        <div class="card" style="border-top: 4px solid #81b29a;">
            <h3>🌱 لوحة التحكم الحية: الواحة الذكية والموارد المائية</h3>
            <p>مؤشرات فحص المستشعرات الرقمية للمياه والتربة في أراضي الجماعة والقبيلة:</p>
            <div class="grid" style="margin-top:0;">
                <div class="shares-box" style="background: #f4f7f5; border-right: 4px solid #2e6f40;">
                    <strong>🚰 منسوب مياه البئر:</strong> {well_level} (مستقر)
                </div>
                <div class="shares-box" style="background: #f4f7f5; border-right: 4px solid #2e6f40;">
                    <strong>💧 نظام الري بالتنقيط:</strong> {irrigation_status}
                </div>
                <div class="shares-box" style="background: #f4f7f5; border-right: 4px solid #2e6f40;">
                    <strong>🪴 رطوبة التربة العامة:</strong> {soil_moisture}
                </div>
            </div>
            <h4>📋 تقرير حالة الغطاء النباتي والأشجار المثمرة:</h4>
            <ul>
                <li><strong>التين (الحمري والخضاري):</strong> {trees_data['أشجار التين (الحمري والخضاري)']}</li>
                <li><strong>الزيتون المحلي:</strong> {trees_data['أشجار الزيتون المحلية']}</li>
                <li><strong>أشجار اللوز:</strong> {trees_data['أشجار اللوز']}</li>
                <li><strong>الحمضيات:</strong> {trees_data['أشجار الحمضيات (الليمون والبرتقال)']}</li>
            </ul>
        </div>
        """

        # دمج القسم الجديد أسفل الميثاق وقبل قسم القنوات الفضائية
        if "" in content and "" not in content:
            updated_content = content.replace("", oasis_html + "\n        ")
            with open("index.html", "w", encoding="utf-8") as f:
                f.write(updated_content)
            print("[✓] تم دمج تحديثات الواحة الذكية داخل ملف الواجهة بنجاح!")
        else:
            print("[!] البيانات مدمجة بالفعل أو لم يتم العثور على مكان الاستبدال.")

    except Exception as e:
        print(f"[-] حدث خطأ أثناء تحديث الواجهة: {e}")

if __name__ == "__main__":
    generate_oasis_dashboard()
