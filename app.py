import streamlit as st
from openai import OpenAI
import os

# 환경변수에 저장된 OPENAI API 키 불러오기
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("💬 ChatGPT API 테스트")
st.write("OpenAI API를 활용한 간단한 Streamlit 챗봇입니다.")

# 사용자 입력
user_input = st.text_input("질문을 입력하세요:")

if user_input:
    with st.spinner("답변 생성 중..."):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "당신은 친절한 AI 교사입니다."},
                {"role": "user", "content": user_input}
            ]
        )
        st.success(response.choices[0].message.content)

import os
import streamlit as st

# OpenAI SDK 1.x
try:
    from openai import OpenAI
except Exception as e:
    st.error("`openai` 패키지가 설치되지 않았습니다. requirements.txt를 확인하세요.")
    st.stop()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.info("환경변수 `OPENAI_API_KEY`가 없습니다. Streamlit Cloud에서 **Settings → Secrets**에 설정하세요.")
client = OpenAI(api_key=api_key)

st.title("💬 ChatGPT API 테스트")
user_input = st.text_input("질문을 입력하세요:")

if user_input:
    with st.spinner("답변 생성 중..."):
        resp = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "당신은 친절한 AI 교사입니다."},
                {"role": "user", "content": user_input},
            ],
        )
        st.write(resp.choices[0].message.content)
