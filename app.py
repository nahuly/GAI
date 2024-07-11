import streamlit as st

def main():
    st.title("간단한 심리 테스트")

    st.write("아래 질문들에 답해주세요.")

    q1 = st.radio(
        "1. 스트레스 받을 때 주로 어떻게 대처하시나요?",
        ('운동한다', '음악을 듣는다', '친구와 대화한다', '잠을 잔다')
    )

    q2 = st.slider('2. 1부터 10까지 스케일에서 당신의 외향성 정도는?', 1, 10, 5)

    q3 = st.selectbox(
        '3. 다음 중 가장 선호하는 색깔은?',
        ('빨강', '파랑', '초록', '노랑')
    )

    q4 = st.text_input('4. 당신의 꿈은 무엇인가요?')

    if st.button('결과 보기'):
        st.write("당신의 응답:")
        st.write(f"1. 스트레스 대처 방법: {q1}")
        st.write(f"2. 외향성 정도: {q2}")
        st.write(f"3. 선호하는 색깔: {q3}")
        st.write(f"4. 꿈: {q4}")

        st.write("심리 분석 결과:")
        if q2 > 7:
            st.write("당신은 매우 외향적인 성격을 가지고 있습니다.")
        elif q2 < 4:
            st.write("당신은 내향적인 성격을 가지고 있습니다.")
        else:
            st.write("당신은 균형 잡힌 성격을 가지고 있습니다.")

        if q3 == '빨강':
            st.write("빨간색을 선호하는 당신은 열정적이고 활동적인 성향을 가지고 있습니다.")
        elif q3 == '파랑':
            st.write("파란색을 선호하는 당신은 차분하고 신중한 성향을 가지고 있습니다.")
        elif q3 == '초록':
            st.write("초록색을 선호하는 당신은 자연을 사랑하고 조화를 추구하는 성향을 가지고 있습니다.")
        else:
            st.write("노란색을 선호하는 당신은 밝고 긍정적인 성향을 가지고 있습니다.")

if __name__ == "__main__":
    main()
