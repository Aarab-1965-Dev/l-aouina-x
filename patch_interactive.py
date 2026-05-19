# -*- coding: utf-8 -*-
import os

def insert_interactive_dashboard():
    if not os.path.exists("index.html"):
        print("[-] خطأ: ملف index.html غير موجود!")
        return

    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()

    # صياغة لوحة المفاتيح والتحكم التفاعلي بالكامل بـ HTML و JavaScript
    interactive_html = """
        <div class="card" style="border-top: 4px solid #3d5a80; background: #ffffff;">
            <h3>🎛️ لوحة مفاتيح المنصة وأدوات التحكم التفاعلي</h3>
            <p>أدوات تفاعلية مستقلة لتتبع البيانات، تقييم الأداء، وتسجيل حضور زوار الواحة الرقمية:</p>
            
            <div style="margin-bottom: 20px; background: #f4f7f5; padding: 15px; border-radius: 6px;">
                <label style="font-weight: bold; color: #2e6f40; display: block; margin-bottom: 8px;">🔍 محرك البحث الداخلي للمنصة:</label>
                <div style="display: flex; gap: 10px;">
                    <input type="text" id="platformSearchInput" placeholder="اكتب كلمة للبحث (مثال: بئر، تين، ميثاق، رطوبة)..." style="flex: 1; padding: 10px; border: 1px solid #ccc; border-radius: 6px; font-size: 1rem;">
                    <button onclick="runPlatformSearch()" style="background: #2e6f40; color: white; border: none; padding: 0 20px; border-radius: 6px; font-weight: bold; cursor: pointer;">بحث</button>
                </div>
                <div id="searchResultsDisplay" style="margin-top: 10px; font-weight: bold; color: #3d5a80;"></div>
            </div>

            <div style="display: flex; gap: 15px; flex-wrap: wrap; margin-bottom: 20px;">
                <div style="flex: 1; min-width: 150px; background: #eef5f0; padding: 12px; border-radius: 6px; text-align: center; border: 1px solid #81b29a;">
                    <button onclick="togglePlatformLike()" style="background: none; border: none; font-size: 1.5rem; cursor: pointer;">👍</button>
                    <div style="margin-top: 5px; font-weight: bold;">عدد الإعجابات: <span id="likeCounterDisplay">0</span></div>
                </div>
                
                <div style="flex: 2; min-width: 250px; background: #f4f7f5; padding: 12px; border-radius: 6px; text-align: center; border: 1px solid #3d5a80;">
                    <span style="font-weight: bold; display: block; margin-bottom: 5px;">⭐ تقييم كفاءة المنصة وأدائها:</span>
                    <span class="star" onclick="ratePlatform(1)" style="font-size: 1.5rem; cursor: pointer; color: #ccc;">★</span>
                    <span class="star" onclick="ratePlatform(2)" style="font-size: 1.5rem; cursor: pointer; color: #ccc;">★</span>
                    <span class="star" onclick="ratePlatform(3)" style="font-size: 1.5rem; cursor: pointer; color: #ccc;">★</span>
                    <span class="star" onclick="ratePlatform(4)" style="font-size: 1.5rem; cursor: pointer; color: #ccc;">★</span>
                    <span class="star" onclick="ratePlatform(5)" style="font-size: 1.5rem; cursor: pointer; color: #ccc;">★</span>
                    <div id="ratingStatusDisplay" style="font-size: 0.9rem; margin-top: 5px; color: #2e6f40; font-weight: bold;">لم يتم التقييم بعد</div>
                </div>
            </div>

            <div style="background: #ffffff; border: 1px solid #ddd; padding: 15px; border-radius: 6px;">
                <label style="font-weight: bold; color: #3d5a80; display: block; margin-bottom: 8px;">📝 سجل زوار الواحة الرقمية والتعليقات المباشرة:</label>
                <div style="display: flex; flex-direction: column; gap: 10px; margin-bottom: 15px;">
                    <input type="text" id="visitorNameInput" placeholder="اسم الزائر الكريم أو الصفة..." style="padding: 10px; border: 1px solid #ccc; border-radius: 6px;">
                    <textarea id="visitorCommentInput" rows="2" placeholder="اكتب تعليقك أو انطباعك حول المنصة هنا..." style="padding: 10px; border: 1px solid #ccc; border-radius: 6px; font-family: inherit;"></textarea>
                    <button onclick="registerVisitorLog()" style="background: #3d5a80; color: white; border: none; padding: 10px; border-radius: 6px; font-weight: bold; cursor: pointer; transition: background 0.3s;">تسجيل الحضور ونشر التعليق</button>
                </div>
                
                <div id="visitorLogsBox" style="max-height: 200px; overflow-y: auto; background: #fafafa; padding: 10px; border-radius: 4px; border: 1px solid #eee;">
                    <p style="color: #888; font-style: italic; margin: 0; text-align: center;" id="emptyLogText">لا توجد تسجيلات حتى الآن. كن أول المسجلين في قائمة الشرف للواحة!</p>
                </div>
            </div>
        </div>

        <script>
            // 1. محرك البحث الذكي في النصوص
            function runPlatformSearch() {
                var query = document.getElementById('platformSearchInput').value.trim();
                var display = document.getElementById('searchResultsDisplay');
                if(!query) {
                    display.innerHTML = "❌ الرجاء كتابة كلمة للبحث عنها.";
                    return;
                }
                var bodyText = document.body.innerText;
                var count = (bodyText.match(new RegExp(query, 'gi')) || []).length;
                if(count > 0) {
                    display.innerHTML = "✅ تم العثور على كلمة (" + query + ") عدد " + count + " مرة في نصوص المنصة المباشرة.";
                } else {
                    display.innerHTML = "❌ لم يتم العثور على تطابق للكلمة المطلوبة في واجهات المنصة الحالية.";
                }
            }

            // 2. نظام الإعجابات المحلي المستقل
            var currentLikes = parseInt(localStorage.getItem('platform_likes') || '0');
            document.getElementById('likeCounterDisplay').innerText = currentLikes;
            function togglePlatformLike() {
                currentLikes++;
                localStorage.setItem('platform_likes', currentLikes);
                document.getElementById('likeCounterDisplay').innerText = currentLikes;
            }

            // 3. نظام تقييم النجوم التفاعلي للمنصة
            function ratePlatform(stars) {
                var starElements = document.getElementsByClassName('star');
                for(var i=0; i<5; i++) {
                    if(i < stars) {
                        starElements[i].style.color = '#ffb703';
                    } else {
                        starElements[i].style.color = '#ccc';
                    }
                }
                var messages = ["ضعيف جداً", "مقبول", "جيد", "ممتاز جداً", "سوبر ذكاء كفاءة كاملة 100% ⭐"];
                document.getElementById('ratingStatusDisplay').innerText = "تقييمك للمنصة: " + messages[stars-1];
                localStorage.setItem('platform_rating', stars);
            }

            // 4. سجل الزوار والتعليقات المكتوب يدوياً ومحلياً
            function loadVisitorLogs() {
                var logs = JSON.parse(localStorage.getItem('visitor_logs') || '[]');
                var box = document.getElementById('visitorLogsBox');
                if(logs.length > 0) {
                    box.innerHTML = '';
                    logs.forEach(function(item) {
                        var logDiv = document.createElement('div');
                        logDiv.style.padding = '8px';
                        logDiv.style.marginBottom = '8px';
                        logDiv.style.borderBottom = '1px dashed #ddd';
                        logDiv.style.fontSize = '0.95rem';
                        logDiv.innerHTML = "👤 <strong>" + item.name + "</strong>: <span style='color:#555;'>" + item.comment + "</span> <small style='color:#aaa; float:left;'>" + item.date + "</small>";
                        box.appendChild(logDiv);
                    });
                }
            }
            
            function registerVisitorLog() {
                var name = document.getElementById('visitorNameInput').value.trim();
                var comment = document.getElementById('visitorCommentInput').value.trim();
                if(!name || !comment) {
                    alert('الرجاء إدخال الاسم والتعليق لتسجيل الحضور النبيل في المنصة!');
                    return;
                }
                var logs = JSON.parse(localStorage.getItem('visitor_logs') || '[]');
                var dateStr = new Date().toLocaleDateString('ar-MA', {hour: '2-digit', minute:'2-digit'});
                logs.unshift({name: name, comment: comment, date: dateStr});
                localStorage.setItem('visitor_logs', JSON.stringify(logs));
                
                // تفريغ المدخلات وإعادة التحميل
                document.getElementById('visitorNameInput').value = '';
                document.getElementById('visitorCommentInput').value = '';
                loadVisitorLogs();
            }

            // تشغيل التغذية التلقائية عند فتح الصفحة للزائر
            window.onload = function() {
                loadVisitorLogs();
                var savedRating = localStorage.getItem('platform_rating');
                if(savedRating) ratePlatform(parseInt(savedRating));
            };
        </script>
    """

    # دمج اللوحة الجديدة والسكريبت التشغيلي فوق نهاية الـ footer مباشرة لضمان الاتساق
    if "</footer>" in content and "🎛️ لوحة مفاتيح المنصة" not in content:
        updated_content = content.replace("<footer>", interactive_html + "\n    <footer>")
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(updated_content)
        print("[✓] تم دمج لوحة مفاتيح المنصة ومحرك التحكم التفاعلي بنجاح!")
    else:
        print("[!] النظام مدمج مسبقاً أو تعذر العثور على مكان الترقيع.")

if __name__ == "__main__":
    insert_interactive_dashboard()
