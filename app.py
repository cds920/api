# app.py
import os
import streamlit as st

# OpenAI SDK (v1.x)
try:
    from openai import OpenAI
except Exception as e:
    st.error("❌ `openai` 패키지가 설치되지 않았습니다. requirements.txt를 확인하세요.")
    st.stop()

# 환경변수에서 API 키 불러오기
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.info("⚙️ 환경변수 `OPENAI_API_KEY`가 없습니다.\nStreamlit Cloud에서 **Settings → Secrets**에 설정하세요.")
    st.stop()

# OpenAI 클라이언트 생성
client = OpenAI(api_key=api_key)

# --- Streamlit UI ---
st.title("💬 ChatGPT API 테스트")
st.write("OpenAI API를 활용한 간단한 Streamlit 챗봇입니다.")

# 사용자 입력
user_input = st.text_input("질문을 입력하세요:")

# 응답 생성
if user_input:
    with st.spinner("답변 생성 중..."):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "당신은 친절한 AI 교사입니다."},
                    {"role": "user", "content": user_input},
                ],
            )
            st.success(response.choices[0].message.content)
        except Exception as e:
            st.error(f"API 호출 중 오류가 발생했습니다: {e}")
