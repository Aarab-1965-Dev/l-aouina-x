# -*- coding: utf-8 -*-
import os

def insert_leadership_charter():
    if not os.path.exists("index.html"):
        print("[-] خطأ: ملف index.html غير موجود!")
        return

    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()

    charter_html = """
        <div class="card" style="margin-top: 20px; border-right: 4px solid #3d5a80;">
            <h3>🏛️ ميثاق القيادة الخدمية وإدارة الواحة</h3>
            <p><strong>مبدأ الخدمة أولاً:</strong> نؤمن بأن القيادة الحقيقية هي تكليف لخدمة الساكنة ورعاية الموارد. نلتزم في مشروع <strong>LAAWAYNA-X</strong> بالاستماع الفعال لمتطلبات المجتمع وتعميق أواصر التعاون والتضامن الإنساني المستقل.</p>
            <ul style="padding-right: 20px; margin-top: 5px;">
                <li><strong>الإنصات الميداني العادل:</strong> رصد وتوثيق متطلبات البنية التحتية وحماية منابع المياه الجوفية.</li>
                <li><strong>التعاطف والتفهم المؤسسي:</strong> تغليب المصلحة العامة للقبيلة ودعم استقرار الواحة ونموها الطبيعي وثقتها.</li>
                <li><strong>الاستقلالية الرقمية الهادفة:</strong> توظيف البيئة البرمجية المستقلة لتقديم محتوى ونزاهة تعزز الأداء الإنساني والتنموي.</li>
            </ul>
        </div>
"""

    if "</footer>" in content and "🏛️ ميثاق القيادة الخدمية" not in content:
        updated_content = content.replace("<footer>", charter_html + "\n    <footer>")
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(updated_content)
        print("[✓] تم دمج ميثاق القيادة الخدمية بنجاح داخل واجهة index.html")
    else:
        print("[!] الميثاق مدمج بالفعل أو أن الهيكل مختلف.")

if __name__ == "__main__":
    insert_leadership_charter()
