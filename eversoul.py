import streamlit as st
import pandas as pd

# 데이터 로드
@st.cache_data
def load_data():
    file_path = 'ever.csv'
    spirits_data = pd.read_csv(file_path)
    return spirits_data

data = load_data()

# 웹사이트 제목
st.title("당신의 최애 정령 찾기")

# 질문 및 선택지 설정
questions = {
    "당신이 선호하는 신장은?": data['신장'].unique().tolist(),
    "어떤 취미를 가진 정령을 좋아하시나요?": data['취미'].unique().tolist(),
    "어떤 특기를 가진 정령을 선호하시나요?": data['특기'].unique().tolist(),
    "정령이 좋아하는 것 중 당신의 취향과 맞는 것은?": data['좋아하는 것'].unique().tolist(),
    "어떤 색상의 정령을 선호하시나요?": data['캐릭터 색상'].unique().tolist()
}

# 사용자 응답 저장
responses = {}

# 질문 표시 및 응답 수집
for question, options in questions.items():
    response = st.selectbox(question, options)
    responses[question] = response

# 결과 계산 버튼
if st.button("결과 보기"):
    scores = {spirit: 0 for spirit in data['이름']}
    
    for question, response in responses.items():
        for _, spirit in data.iterrows():
            if question == "당신이 선호하는 신장은?":
                if response == spirit['신장']:
                    scores[spirit['이름']] += 1
            elif question == "어떤 취미를 가진 정령을 좋아하시나요?":
                if response == spirit['취미']:
                    scores[spirit['이름']] += 1
            elif question == "어떤 특기를 가진 정령을 선호하시나요?":
                if response == spirit['특기']:
                    scores[spirit['이름']] += 1
            elif question == "정령이 좋아하는 것 중 당신의 취향과 맞는 것은?":
                if response == spirit['좋아하는 것']:
                    scores[spirit['이름']] += 1
            elif question == "어떤 색상의 정령을 선호하시나요?":
                if response.lower() == spirit['캐릭터 색상'].lower():
                    scores[spirit['이름']] += 1
    
    # 점수에 따라 정령 정렬
    ranked_spirits = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    
    # 결과 표시
    st.subheader("당신의 최애 정령 순위:")
    for rank, (spirit, score) in enumerate(ranked_spirits[:3], 1):
        spirit_data = data[data['이름'] == spirit].iloc[0]
        st.write(f"{rank}위: {spirit}")
        st.write(f"소속: {spirit_data['소속']}")
        st.write(f"특기: {spirit_data['특기']}")
        st.write(f"취미: {spirit_data['취미']}")
        st.write("---")
