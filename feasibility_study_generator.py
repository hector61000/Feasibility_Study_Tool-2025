#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
نظام توليد دراسات الجدوى - 2025
نظام متكامل لتوليد دراسات جدوى تفصيلية للمشاريع المختلفة باستخدام Google Gemini AI
"""

import os
from docx import Document
import google.generativeai as genai
from dotenv import load_dotenv
import time

# تحميل مفتاح API
load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

class FeasibilityStudyGenerator:
    def __init__(self):
        """تهيئة المولد"""
        self.model = genai.GenerativeModel('gemini-pro')
        
    def generate_content(self, project_name, section_name):
        """
        توليد محتوى للقسم المحدد باستخدام Google Gemini API
        """
        try:
            prompt = f"""اكتب محتوى تفصيلي (1000 كلمة) لقسم {section_name} في دراسة جدوى {project_name} في السوق السعودي.
            المحتوى يجب أن يكون:
            1. باللغة العربية مع شرح مفصل لكل نقطة
            2. يشمل أمثلة عملية وحالات دراسية من السوق السعودي 2025
            3. الميزانية في حدود 400 ألف ريال سعودي
            4. يحتوي على:
               - شرح تفصيلي للمفاهيم والمصطلحات
               - أمثلة واقعية من مشاريع مشابهة في السعودية
               - خطوات تنفيذية مفصلة مع مراعاة القوانين السعودية
               - نصائح وإرشادات عملية للسوق السعودي
               - تحليل مفصل للأرقام والإحصائيات في السعودية
               - دراسات حالة من مشاريع ناجحة في السعودية
               - متطلبات التراخيص والسجلات في السعودية
               - خطوات عملية للتنفيذ في السوق السعودي
               - تحديات متوقعة وحلول مقترحة
            5. يستخدم جداول وأرقام تفصيلية محدثة 2025 للسوق السعودي
            6. يشرح كل خطوة بالتفصيل مع الأسباب والنتائج
            7. يشمل:
               - تكاليف التأسيس بالريال السعودي
               - الرسوم الحكومية والتراخيص
               - تكاليف العمالة حسب نظام العمل السعودي
               - متطلبات السعودة
               - التكاليف التشغيلية في السوق السعودي
            8. يوضح كيفية تجنب المشاكل الشائعة في السوق السعودي
            9. يقدم بدائل وخيارات مختلفة ضمن الميزانية المحددة
            10. يشرح الجوانب المالية والفنية بتفصيل عملي
            """
            
            # إضافة وقت انتظار بين الطلبات
            time.sleep(2)
            response = self.model.generate_content(prompt)
            return response.text if response and response.text else ""
                
        except Exception as e:
            print(f"خطأ في توليد محتوى المشروع {project_name}: {str(e)}")
            return ""

    def create_feasibility_study(self, project_name, output_dir):
        """إنشاء دراسة جدوى كاملة"""
        try:
            doc = Document()
            
            sections = [
                "جدول المحتويات",
                "الملخص التنفيذي",
                "الخطة التوسعية",
                "دراسة السوق والتسويق",
                "الدراسة الفنية",
                "الدراسة المالية",
                "دراسة المخاطر",
                "مصادر التمويل",
                "الخاتمة والتوصيات"
            ]
            
            print(f"بدء توليد دراسة الجدوى لـ {project_name}...")
            
            for section in sections:
                print(f"توليد قسم: {section}")
                content = self.generate_content(project_name, section)
                if content:
                    doc.add_heading(section, level=1)
                    doc.add_paragraph(content)
                else:
                    print(f"تحذير: فشل في توليد محتوى لقسم {section}")
            
            # إنشاء المجلد إذا لم يكن موجوداً
            os.makedirs(f"generated_studies/{output_dir}", exist_ok=True)
            
            # حفظ الملف
            output_path = f"generated_studies/{output_dir}/{project_name}.docx"
            doc.save(output_path)
            print(f"تم حفظ الدراسة في: {output_path}")
            
            return True
            
        except Exception as e:
            print(f"خطأ في إنشاء دراسة الجدوى: {str(e)}")
            return False

    def generate_studies(self, projects, output_dir):
        """توليد مجموعة من دراسات الجدوى"""
        success_count = 0
        for project in projects:
            if self.create_feasibility_study(project, output_dir):
                success_count += 1
            
        print(f"تم إنشاء {success_count} من {len(projects)} دراسة جدوى")
        return success_count

def main():
    """
    المثال الرئيسي لاستخدام النظام
    """
    # إنشاء مولد دراسات الجدوى
    generator = FeasibilityStudyGenerator()
    
    # مشروع في السعودية بميزانية 400 ألف ريال
    saudi_projects = [
        "مشروع مركز صيانة سيارات فاخرة",  # مشروع مربح في السعودية مع الطلب المتزايد على السيارات الفاخرة
    ]
    
    # توليد دراسة الجدوى
    print("توليد دراسة جدوى للمشروع في السعودية...")
    generator.generate_studies(saudi_projects, "مشاريع_السعودية")

if __name__ == "__main__":
    main()
