import streamlit as st
import json
import random
import time

# 캐싱 적용 (의도적으로 2초 지연 추가)
@st.cache_data
def load_quiz_data():
    time.sleep(2)
    with open("quiz_data.json", "r", encoding="utf-8") as file:
        return json.load(file)

st.title("음악 장르 퀴즈 앱")
st.write("학번: 2025404002")
st.write("이름: 이준성")

st.divider()

# 로그인 상태 초기화
if "login" not in st.session_state:
    st.session_state.login = False

st.subheader("로그인")

user_id = st.text_input("아이디")
user_pw = st.text_input("비밀번호", type="password")

# 로그인 조건 변경
if st.button("로그인"):
    if user_id == "ssam3782" and user_pw == "leejs0421!":
        st.session_state.login = True
        st.success("로그인 성공!")
    else:
        st.error("로그인 실패!")

# 로그인 이후
if st.session_state.login:
    st.success("로그인 상태입니다.")
    st.divider()

    # 🔥 캐싱 시연 영역 (특색 추가 핵심)
    st.subheader("캐싱 기능 시연")

    st.write("퀴즈 데이터는 JSON 파일에서 불러오며 캐싱이 적용되어 있습니다.")
    st.write("처음에는 로딩 시간이 걸리지만, 이후에는 빠르게 불러옵니다.")

    if st.button("캐시 초기화"):
        st.cache_data.clear()
        st.success("캐시를 초기화했습니다. 새로고침하면 다시 로딩됩니다.")

    with st.spinner("퀴즈 데이터를 불러오는 중입니다..."):
        all_quiz_data = load_quiz_data()

    st.success("퀴즈 데이터 로딩 완료")

    st.divider()

    # 퀴즈 시작
    st.subheader("음악 장르 퀴즈")

    quiz_data = random.sample(all_quiz_data, 10)
    st.write(f"전체 {len(all_quiz_data)}개 문제 중 {len(quiz_data)}문제가 출제됩니다.")

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