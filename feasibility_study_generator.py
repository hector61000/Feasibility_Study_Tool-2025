#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
نظام توليد دراسات الجدوى - 2025
نظام متكامل لتوليد دراسات جدوى تفصيلية للمشاريع المختلفة في السوق المصري
جميع الحقوق محفوظة لشركة Green Light © 2025
"""

import os
import json
import time
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from dotenv import load_dotenv
import google.generativeai as genai

class FeasibilityStudyGenerator:
    def __init__(self):
        """تهيئة المولد"""
        try:
            # تحميل مفتاح API
            load_dotenv()
            api_key = os.getenv("GOOGLE_API_KEY")
            
            if not api_key:
                api_key = "AIzaSyCV9Xr7syuMEeXW7-H9Favc4er7GORNgxM"  # مفتاح احتياطي للتطوير
                print("تحذير: تم استخدام مفتاح API الاحتياطي")
            
            # تهيئة Google Gemini
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-pro')
            print("✅ تم تهيئة النموذج بنجاح")
            
        except Exception as e:
            print(f"❌ حدث خطأ أثناء التهيئة: {str(e)}")
            raise
        
        # هيكل الأقسام
        self.sections = {
            "مقدمة": ["أهمية دراسات الجدوى وفوائدها"],
            "القسم الأول: دراسة الجدوى الاقتصادية": [
                "المقدمة", "الهدف", "رأس المال المطلوب", "التكاليف الاستثمارية الأولية",
                "التكاليف التشغيلية السنوية", "الإيرادات السنوية", "حساب الإيرادات اليومية والسنوية",
                "إجمالي التكاليف السنوية", "التحليل المالي", "صافي الربح"
            ],
            "القسم الثاني: دراسة الجدوى الفنية": [
                "الهدف", "اختيار الموقع", "تقدير استهلاك العلف السنوي", 
                "المعدات اللازمة", "العمالة اللازمة"
            ],
            "القسم الثالث: دراسة الجدوى التسويقية": [
                "الهدف", "تحليل السوق المستهدف", "الشرائح المستهدفة",
                "تحليل المنافسة", "استراتيجيات التسويق", "التوزيع",
                "التسعير", "الترويج"
            ],
            "القسم الرابع: دراسة الجدوى القانونية": [
                "الهدف", "التراخيص والتصاريح اللازمة", "قوانين العمل والعمالة",
                "اللوائح الصحية", "القوانين البيئية"
            ],
            "القسم الخامس: دراسة الجدوى الاجتماعية والبيئية": [
                "الهدف", "التأثير الاجتماعي", "خلق فرص العمل",
                "تحسين مستوى معيشة المجتمع", "التأثير على الصحة العامة",
                "التأثير البيئي", "التأثير على الموارد الطبيعية",
                "إدارة المخلفات البيئية", "الانبعاثات الكربونية",
                "الاستدامة البيئية والاجتماعية", "الاستدامة الاجتماعية",
                "الاستدامة البيئية", "الفوائد المستقبلية"
            ],
            "القسم السادس: المخاطر المحتملة وكيفية التعامل معها": [
                "المخاطر المالية", "كيفية التعامل مع المخاطر المالية",
                "المخاطر الفنية", "المخاطر القانونية",
                "خطط واضحة للتقليل من التأثير السلبي"
            ],
            "القسم السابع: الخطة التوسعية والتوقعات المستقبلية": [
                "الخطة التوسعية", "تنويع المنتجات", "التوسع في الأسواق",
                "استخدام التكنولوجيا الحديثة", "التوقعات المستقبلية للمشروع"
            ],
            "القسم الثامن: الخاتمة": [""]
        }

    def generate_content(self, project_name, section):
        """توليد محتوى لقسم معين من دراسة الجدوى"""
        try:
            current_year = "2025"
            prompts = {
                "مقدمة": f"""اكتب مقدمة شاملة لدراسة جدوى {project_name} في مصر لعام {current_year}.
                يجب أن تتضمن المقدمة:
                - أهمية المشروع في السوق المصري
                - الفرص المتاحة في السوق
                - لماذا يعتبر هذا المشروع مناسباً للسوق المصري
                - التحديات والفرص في السوق المصري
                اكتب المحتوى باللغة العربية، واستخدم العملة المصرية (الجنيه المصري) في جميع التكاليف.""",
                
                "القسم الأول: دراسة الجدوى الاقتصادية": f"""اكتب دراسة الجدوى الاقتصادية التفصيلية ل{project_name} في مصر لعام {current_year}.
                يجب أن تتضمن:
                - التكاليف الاستثمارية بالجنيه المصري
                - تكاليف التشغيل الشهرية
                - الإيرادات المتوقعة
                - فترة استرداد رأس المال
                - معدل العائد على الاستثمار
                - تحليل نقطة التعادل
                استخدم أسعار وتكاليف واقعية للسوق المصري في {current_year}.""",
                
                "القسم الثاني: دراسة الجدوى الفنية": f"""اكتب دراسة الجدوى الفنية التفصيلية ل{project_name} في مصر لعام {current_year}.
                يجب أن تتضمن:
                - المتطلبات الفنية للمشروع
                - المعدات والآلات المطلوبة مع أسعارها بالجنيه المصري
                - المساحة المطلوبة والموقع المناسب
                - العمالة المطلوبة ومؤهلاتهم
                - خطوات الإنتاج أو تقديم الخدمة
                استخدم معلومات تقنية حديثة ومناسبة للسوق المصري.""",
                
                "القسم الثالث: دراسة الجدوى التسويقية": f"""اكتب دراسة الجدوى التسويقية التفصيلية ل{project_name} في مصر لعام {current_year}.
                يجب أن تتضمن:
                - تحليل السوق المصري
                - المنافسين في السوق
                - الفئة المستهدفة
                - استراتيجيات التسويق المناسبة للسوق المصري
                - قنوات التوزيع
                - تحليل الأسعار في السوق المصري""",
                
                "القسم الرابع: دراسة الجدوى القانونية": f"""اكتب دراسة الجدوى القانونية التفصيلية ل{project_name} في مصر لعام {current_year}.
                يجب أن تتضمن:
                - الشكل القانوني للمشروع
                - التراخيص المطلوبة
                - الإجراءات القانونية
                - التكاليف القانونية بالجنيه المصري
                - المتطلبات الحكومية
                استخدم المعلومات القانونية الحديثة المطبقة في مصر.""",
                
                "القسم الخامس: دراسة الجدوى الاجتماعية والبيئية": f"""اكتب دراسة الجدوى الاجتماعية والبيئية ل{project_name} في مصر لعام {current_year}.
                يجب أن تتضمن:
                - الأثر الاجتماعي للمشروع
                - فرص العمل التي سيوفرها
                - الآثار البيئية
                - إجراءات الحماية البيئية
                - المسؤولية الاجتماعية""",
                
                "القسم السادس: المخاطر المحتملة وكيفية التعامل معها": f"""اكتب تحليلاً للمخاطر المحتملة ل{project_name} في مصر لعام {current_year}.
                يجب أن تتضمن:
                - المخاطر السوقية
                - المخاطر المالية
                - المخاطر التشغيلية
                - المخاطر القانونية
                - استراتيجيات إدارة المخاطر""",
                
                "القسم السابع: الخطة التوسعية والتوقعات المستقبلية": f"""اكتب الخطة التوسعية والتوقعات المستقبلية ل{project_name} في مصر لعام {current_year}.
                يجب أن تتضمن:
                - خطط التوسع المستقبلية
                - التوقعات المالية للسنوات القادمة
                - فرص النمو في السوق المصري
                - التطورات المتوقعة في المجال
                استخدم توقعات واقعية تناسب السوق المصري.""",
                
                "القسم الثامن: الخاتمة": f"""اكتب خاتمة لدراسة جدوى {project_name} في مصر لعام {current_year}.
                يجب أن تتضمن:
                - ملخص لأهم النقاط في الدراسة
                - توصيات نهائية
                - نظرة مستقبلية للمشروع"""
            }
            
            try:
                print(f"جاري توليد المحتوى لـ {project_name} - {section}")
                
                prompt = prompts.get(section, "")
                if not prompt:
                    print(f"لم يتم العثور على قسم {section} في قوائم الأقسام")
                    return ""
                
                time.sleep(2)  # تأخير لتجنب تجاوز حدود API
                response = self.model.generate_content(prompt)
                if response and response.text:
                    print(f"تم توليد المحتوى بنجاح لـ {section}")
                    return response.text
                else:
                    print(f"فشل في توليد المحتوى لـ {section}: لا يوجد نص في الاستجابة")
                    return ""
                    
            except Exception as e:
                print(f"خطأ في توليد محتوى القسم {section}: {str(e)}")
                return ""
                
        except Exception as e:
            print(f"خطأ في توليد محتوى القسم {section}: {str(e)}")
            return ""

    def create_document(self, project_name, project_type):
        """إنشاء مستند دراسة الجدوى"""
        try:
            doc = Document()
            
            # إعداد العنوان
            title = doc.add_heading(f'دراسة جدوى مشروع {project_name}', 0)
            title.alignment = WD_ALIGN_PARAGRAPH.CENTER
            
            # إضافة معلومات الشركة
            company_info = doc.add_paragraph()
            company_info.alignment = WD_ALIGN_PARAGRAPH.CENTER
            company_info.add_run('تم إعداد هذه الدراسة بواسطة\nشركة Green Light للتكنولوجيا والتطوير\n').bold = True
            company_info.add_run('معتمد من Google Cloud Platform').italic = True
            
            # إضافة التاريخ
            date_paragraph = doc.add_paragraph()
            date_paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT
            date_paragraph.add_run(f'تاريخ الإصدار: {time.strftime("%Y-%m-%d")}')
            
            # إضافة معلومات حقوق النشر
            footer = doc.sections[0].footer
            footer_paragraph = footer.paragraphs[0]
            footer_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            footer_paragraph.add_run('© 2025 جميع الحقوق محفوظة لشركة Green Light للتكنولوجيا والتطوير').font.size = Pt(8)
            
            return doc
            
        except Exception as e:
            print(f"❌ حدث خطأ أثناء إنشاء المستند: {str(e)}")
            return None

    def create_feasibility_study(self, project_name, output_dir):
        """إنشاء دراسة جدوى كاملة لمشروع محدد"""
        try:
            doc = Document()
            
            # إعداد الصفحة
            sections = doc.sections
            for section in sections:
                section.top_margin = Inches(1)
                section.bottom_margin = Inches(1)
                section.left_margin = Inches(1)
                section.right_margin = Inches(1)
            
            # جدول المحتويات
            doc.add_heading("جدول المحتويات", level=1)
            for section_name, subsections in self.sections.items():
                p = doc.add_paragraph()
                p.add_run(section_name).bold = True
                for subsection in subsections:
                    if subsection:
                        p = doc.add_paragraph()
                        p.paragraph_format.left_indent = Pt(20)
                        p.add_run(subsection)
            
            doc.add_page_break()
            
            # إنشاء محتوى الدراسة
            for section_name, subsections in self.sections.items():
                # إضافة عنوان القسم
                doc.add_heading(section_name, level=1)
                
                # إضافة المحتوى لكل قسم فرعي
                for subsection in subsections:
                    if subsection:
                        doc.add_heading(subsection, level=2)
                        content = self.generate_content(project_name, section_name)
                        doc.add_paragraph(content)
                
                # إضافة فاصل صفحات بين الأقسام الرئيسية
                doc.add_page_break()
            
            # حفظ الملف
            output_file = os.path.join(output_dir, f"{project_name}.docx")
            doc.save(output_file)
            print(f"تم إنشاء دراسة الجدوى لـ {project_name} بنجاح")
            
        except Exception as e:
            print(f"خطأ في إنشاء دراسة الجدوى لـ {project_name}: {str(e)}")

    def generate_all_studies(self):
        """توليد دراسات جدوى لجميع المشاريع"""
        try:
            print("بدء عملية توليد دراسات الجدوى...")
            
            # قراءة قائمة المشاريع من الملف
            print("جاري قراءة ملف المشاريع...")
            with open('projects.json', 'r', encoding='utf-8') as f:
                projects = json.load(f)
            
            # إنشاء المجلدات إذا لم تكن موجودة
            print("جاري إنشاء المجلدات...")
            base_dir = "generated_studies"
            industrial_dir = os.path.join(base_dir, "المشاريع_الصناعية")
            agricultural_dir = os.path.join(base_dir, "المشاريع_الزراعية")
            service_dir = os.path.join(base_dir, "المشاريع_الخدمية")
            multi_service_dir = os.path.join(base_dir, "المشاريع_متعددة_الخدمات")
            
            os.makedirs(industrial_dir, exist_ok=True)
            os.makedirs(agricultural_dir, exist_ok=True)
            os.makedirs(service_dir, exist_ok=True)
            os.makedirs(multi_service_dir, exist_ok=True)
            print(f"تم إنشاء المجلدات في {os.path.abspath(base_dir)}")
            
            # توليد دراسات للمشاريع الصناعية
            print("\nجاري توليد دراسات الجدوى للمشاريع الصناعية...")
            for project in projects["industrial_projects"]:
                print(f"\nبدء العمل على: {project}")
                self.create_feasibility_study(project, industrial_dir)
            
            # توليد دراسات للمشاريع الزراعية
            print("\nجاري توليد دراسات الجدوى للمشاريع الزراعية...")
            for project in projects["agricultural_projects"]:
                print(f"\nبدء العمل على: {project}")
                self.create_feasibility_study(project, agricultural_dir)
            
            # توليد دراسات للمشاريع الخدمية
            print("\nجاري توليد دراسات الجدوى للمشاريع الخدمية...")
            for project in projects["service_projects"]:
                print(f"\nبدء العمل على: {project}")
                self.create_feasibility_study(project, service_dir)
            
            # توليد دراسات للمشاريع متعددة الخدمات
            print("\nجاري توليد دراسات الجدوى للمشاريع متعددة الخدمات...")
            for project in projects["multi_service_projects"]:
                print(f"\nبدء العمل على: {project}")
                self.create_feasibility_study(project, multi_service_dir)
            
            print("\nتم الانتهاء من توليد جميع دراسات الجدوى")
            
        except Exception as e:
            print(f"خطأ في توليد دراسات الجدوى: {str(e)}")
            import traceback
            print(traceback.format_exc())

if __name__ == "__main__":
    generator = FeasibilityStudyGenerator()
    generator.generate_all_studies()
