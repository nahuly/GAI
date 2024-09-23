import streamlit as st
import pandas as pd

# 데이터 로드
@st.cache_data
def load_data():
    file_path = 'ever.csv'
    spirits_data = pd.read_csv(file_path)
    spirits_data_cleaned = spirits_data.dropna().T
    spirits_data_cleaned.columns = spirits_data_cleaned.iloc[0]
    return spirits_data_cleaned.drop(spirits_data_cleaned.index[0])

data = load_data()

# 웹사이트 제목
st.title("당신의 최애 정령 찾기")

# 질문 리스트
questions = [
    "당신이 선호하는 신장은?",
    "어떤 취미를 가진 정령을 좋아하시나요?",
    "어떤 특기를 가진 정령을 선호하시나요?",
    "정령이 좋아하는 것 중 당신의 취향과 맞는 것은?",
    "어떤 색상의 정령을 선호하시나요?"
]

# 사용자 응답 저장
responses = {}

# 질문 표시 및 응답 수집
for question in questions:
    response = st.text_input(question)
    responses[question] = response

# 결과 계산 버튼
if st.button("결과 보기"):
    scores = {spirit: 0 for spirit in data.index}
    
    for question, response in responses.items():
        if response:
            for spirit in data.index:
                if question == "당신이 선호하는 신장은?":
                    if response in data.loc[spirit, '신장']:
                        scores[spirit] += 1
                elif question == "어떤 취미를 가진 정령을 좋아하시나요?":
                    if response in data.loc[spirit, '취미']:
                        scores[spirit] += 1
                elif question == "어떤 특기를 가진 정령을 선호하시나요?":
                    if response in data.loc[spirit, '특기']:
                        scores[spirit] += 1
                elif question == "정령이 좋아하는 것 중 당신의 취향과 맞는 것은?":
                    if response in data.loc[spirit, '좋아하는 것']:
                        scores[spirit] += 1
                elif question == "어떤 색상의 정령을 선호하시나요?":
                    if response.lower() in data.loc[spirit, '캐릭터 색상'].lower():
                        scores[spirit] += 1
    
    # 점수에 따라 정령 정렬
    ranked_spirits = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    
    # 결과 표시
    st.subheader("당신의 최애 정령 순위:")
    for rank, (spirit, score) in enumerate(ranked_spirits[:3], 1):
        st.write(f"{rank}위: {spirit}")
        st.write(f"소속: {data.loc[spirit, '소속']}")
        st.write(f"특기: {data.loc[spirit, '특기']}")
        st.write(f"취미: {data.loc[spirit, '취미']}")
        st.write("---")
