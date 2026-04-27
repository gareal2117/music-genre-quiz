import streamlit as st
import json
import random

@st.cache_data
def load_quiz_data():
    with open("quiz_data.json", "r", encoding="utf-8") as file:
        return json.load(file)

st.title("음악 장르 퀴즈 앱")
st.write("학번: 2025404002")
st.write("이름: 이준성")

st.divider()

if "login" not in st.session_state:
    st.session_state.login = False

st.subheader("로그인")

user_id = st.text_input("아이디")
user_pw = st.text_input("비밀번호", type="password")

if st.button("로그인"):
    if user_id == "music" and user_pw == "1234":
        st.session_state.login = True
        st.success("로그인 성공!")
    else:
        st.error("로그인 실패!")

if st.session_state.login:
    st.success("로그인 상태입니다.")
    st.divider()

    st.subheader("음악 장르 퀴즈")

    quiz_data = random.sample(load_quiz_data(), 10)
    st.write(f"총 {len(quiz_data)}문제가 출제됩니다.")

    score = 0
    user_answers = []

    with st.form("quiz_form"):
        for i, quiz in enumerate(quiz_data):
            answer = st.radio(
                f"Q{i+1}. {quiz['question']}",
                quiz["options"],
                key=f"q{i}"
            )
            user_answers.append(answer)

        submitted = st.form_submit_button("제출하기")

    if submitted:
        for i, quiz in enumerate(quiz_data):
            if user_answers[i] == quiz["answer"]:
                score += 1

        st.subheader("결과")
        st.write(f"{len(quiz_data)}문제 중 {score}문제 정답")

        if score >= 8:
            st.success("훌륭합니다!")
        elif score >= 5:
            st.info("괜찮습니다!")
        else:
            st.warning("더 공부해봅시다!")