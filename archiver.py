import json
import os
from datetime import datetime

def archive_platform_data():
    # المسار المفترض للبيانات في المتصفح هو localStorage، سنقوم هنا بإنشاء نسخة محلية
    print("[*] بدء عملية أرشفة سجلات المنصة...")
    # محاكاة لعملية النسخ الاحتياطي
    if not os.path.exists("archives"):
        os.makedirs("archives")
    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"archives/platform_backup_{timestamp}.txt"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write("سجل أرشفة منصة LAAWAYNA-X التفاعلية\n")
        f.write("التاريخ: " + timestamp + "\n")
        f.write("--- حالة النظام: مؤرشف ---")
    
    print(f"[✓] تم حفظ النسخة الاحتياطية بنجاح في: {filename}")

if __name__ == "__main__":
    archive_platform_data()
