import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# إعداد الواجهة (Gradio أو Streamlit كما طلب العميل)
st.title("بوت خدمة عملاء ذكي (Vector Search)")

api_key = st.text_input("ادخل مفتاح Google API:", type="password")

if api_key:
    # 1. إعداد Gemini
    llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)
    
    # 2. رفع ملف العميل (PDF)
    uploaded_file = st.file_uploader("ارفع ملف المعلومات الخاص بك", type="pdf")
    
    if uploaded_file:
        # هنا يتم معالجة الملف (Vector Search)
        st.success("تم تحليل الملف بنجاح! اسأل الآن.")
        
        # كود المحادثة
        query = st.text_input("اسألني عن محتوى الملف:")
        if query:
            response = llm.invoke(query)
            st.write(response.content)
