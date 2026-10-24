import streamlit as st
from core.sheets_client import get_sheet_id, read_sheet, write_sheet
from core.ai_client import ask_gemini

SHEET_ID = get_sheet_id(4)

def render():
    st.header("sys.4")
    st.caption("เชื่อมต่อกับ Google Sheet + Google AI Studio")

    if st.button("โหลดข้อมูล", key=f"load_4"):
        rows = read_sheet(SHEET_ID, "Sheet1")
        st.dataframe(rows)

    user_input = st.text_input("คำสั่งให้ AI ช่วย分析/เขียน", key=f"input_4")
    if st.button("ส่งไป AI", key=f"ask_4") and user_input:
        with st.spinner("กำลังประมวลผล..."):
            answer = ask_gemini(user_input, context=f"ระบบ 4 ข้อมูลคลังพัสดุ")
        st.success("คำตอบ:")
        st.write(answer)
