import streamlit as st
import pandas as pd

# 데이터 로드
@st.cache_data
def load_data():
    file_path = 'ever.csv'
    spirits_data = pd.read_csv(file_path)
    spirits_data_cleaned = spirits_data.set_index('이름').T
    return spirits_data_cleaned

data = load_data()

# 웹사이트 제목
st.title("당신의 최애 정령 찾기")

# 질문 및 선택지 설정
questions = {
    "당신이 선호하는 신장은?": ["155cm", "167cm"],
    "어떤 취미를 가진 정령을 좋아하시나요?": ["고양이 관찰", "보석 관리"],
    "어떤 특기를 가진 정령을 선호하시나요?": ["데이터 분석", "정보 수집"],
    "정령이 좋아하는 것 중 당신의 취향과 맞는 것은?": ["케이크", "꽃"],
    "어떤 색상의 정령을 선호하시나요?": ["#F5F1EB", "#8F735E"]
}

# 사용자 응답 저장
responses = {}

# 질문 표시 및 응답 수집
for question, options in questions.items():
    response = st.selectbox(question, options)
    responses[question] = response

# 결과 계산 버튼
if st.button("결과 보기"):
    scores = {spirit: 0 for spirit in data.columns}
    
    for question, response in responses.items():
        for spirit in data.columns:
            if question == "당신이 선호하는 신장은?":
                if response == data.loc['신장', spirit]:
                    scores[spirit] += 1
            elif question == "어떤 취미를 가진 정령을 좋아하시나요?":
                if response == data.loc['취미', spirit]:
                    scores[spirit] += 1
            elif question == "어떤 특기를 가진 정령을 선호하시나요?":
                if response == data.loc['특기', spirit]:
                    scores[spirit] += 1
            elif question == "정령이 좋아하는 것 중 당신의 취향과 맞는 것은?":
                if response == data.loc['좋아하는 것', spirit]:
                    scores[spirit] += 1
            elif question == "어떤 색상의 정령을 선호하시나요?":
                if response.lower() == data.loc['캐릭터 색상', spirit].lower():
                    scores[spirit] += 1
    
    # 점수에 따라 정령 정렬
    ranked_spirits = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    
    # 결과 표시
    st.subheader("당신의 최애 정령 순위:")
    for rank, (spirit, score) in enumerate(ranked_spirits[:3], 1):
        st.write(f"{rank}위: {spirit}")
        st.write(f"소속: {data.loc['소속', spirit]}")
        st.write(f"특기: {data.loc['특기', spirit]}")
        st.write(f"취미: {data.loc['취미', spirit]}")
        st.write("---")
