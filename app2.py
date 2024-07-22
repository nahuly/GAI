import streamlit as st
from collections import Counter

questions = [
    {
        "question": "당신은 어려운 상황에서 어떻게 행동하나요?",
        "options": [
            "정의로운 행동을 취한다",
            "기회를 잡고 결과를 얻기 위해 노력한다",
            "친구와 협력하여 문제를 해결한다",
            "지혜롭게 문제를 분석하여 해결책을 찾는다"
        ],
        "points": ["그리핀도르", "슬리데린", "후플푸프", "래번클로"]
    },
    {
        "question": "가장 중요하게 생각하는 가치는 무엇인가요?",
        "options": [
            "용기와 정의",
            "성취와 명예",
            "친절과 협동",
            "지식과 지혜"
        ],
        "points": ["그리핀도르", "슬리데린", "후플푸프", "래번클로"]
    },
    {
        "question": "어떤 유형의 사람들과 가장 잘 어울리나요?",
        "options": [
            "대담하고 용기 있는 사람들",
            "야망 있고 영리한 사람들",
            "친절하고 공정한 사람들",
            "지혜롭고 창의적인 사람들"
        ],
        "points": ["그리핀도르", "슬리데린", "후플푸프", "래번클로"]
    },
    {
        "question": "문제를 해결할 때 주로 어떤 접근 방식을 취하나요?",
        "options": [
            "용기 있게 직접 해결하려고 한다",
            "영리하게 계획을 세워 해결한다",
            "협력하여 문제를 해결한다",
            "창의적으로 접근하여 해결책을 찾는다"
        ],
        "points": ["그리핀도르", "슬리데린", "후플푸프", "래번클로"]
    },
    {
        "question": "다른 사람을 도울 때 어떤 방식으로 도움을 주나요?",
        "options": [
            "직접적인 행동으로 돕는다",
            "도움이 될 수 있는 기회를 제공한다",
            "협력하고 지원한다",
            "지식을 나누어 돕는다"
        ],
        "points": ["그리핀도르", "슬리데린", "후플푸프", "래번클로"]
    },
    {
        "question": "당신은 새로운 것을 배울 때 어떤 방식을 선호하나요?",
        "options": [
            "도전적인 상황에서 배우는 것을 선호한다",
            "목표를 설정하고 그 목표를 이루기 위해 배운다",
            "다른 사람들과 함께 배우는 것을 선호한다",
            "책이나 자료를 통해 스스로 배우는 것을 선호한다"
        ],
        "points": ["그리핀도르", "슬리데린", "후플푸프", "래번클로"]
    },
    {
        "question": "당신이 가장 자랑스러워하는 성취는 무엇인가요?",
        "options": [
            "용기를 내어 어려운 일을 해낸 것",
            "큰 목표를 달성한 것",
            "다른 사람과 함께 협력하여 성과를 낸 것",
            "새로운 지식을 얻고 이를 활용한 것"
        ],
        "points": ["그리핀도르", "슬리데린", "후플푸프", "래번클로"]
    },
    {
        "question": "어떤 상황에서 가장 편안함을 느끼나요?",
        "options": [
            "모험이나 도전에 직면했을 때",
            "목표를 향해 나아가고 있을 때",
            "다른 사람들과 협력하고 있을 때",
            "지식을 탐구하고 있을 때"
        ],
        "points": ["그리핀도르", "슬리데린", "후플푸프", "래번클로"]
    },
    {
        "question": "어떤 종류의 친구와 가장 가까운가요?",
        "options": [
            "용기 있는 친구 (그리핀도르)",
            "야망 있는 친구 (슬리데린)",
            "친절한 친구 (후플푸프)",
            "지혜로운 친구 (래번클로)"
        ],
        "points": ["그리핀도르", "슬리데린", "후플푸프", "래번클로"]
    },
    {
        "question": "어떤 방식으로 스트레스를 해소하나요?",
        "options": [
            "활동적이거나 모험적인 일을 하며 해소한다",
            "목표를 재정립하고 그 목표를 향해 나아간다",
            "친구와 이야기를 나누거나 도움을 주고받는다",
            "책을 읽거나 새로운 것을 배운다"
        ],
        "points": ["그리핀도르", "슬리데린", "후플푸프", "래번클로"]
    }
]

def main():
    st.title("호그와트 기숙사 배정 테스트")
    st.write("각 질문에 대해 가장 적합한 답변을 선택해주세요.")

    answers = []

    for i, q in enumerate(questions, 1):
        answer = st.radio(f"{i}. {q['question']}", q['options'])
        answers.append(q['points'][q['options'].index(answer)])

    if st.button('결과 보기'):
        result = Counter(answers).most_common(1)[0][0]
        
        st.write("## 당신의 호그와트 기숙사는...")
        st.write(f"# {result}입니다!")

        descriptions = {
            "그리핀도르": "용기와 대담함, 기사도 정신을 가진 당신! 그리핀도르에 어울립니다.",
            "슬리데린": "야망과 교활함, 지략을 가진 당신! 슬리데린에 어울립니다.",
            "후플푸프": "성실함과 공정함, 인내심을 가진 당신! 후플푸프에 어울립니다.",
            "래번클로": "지혜와 창의성, 학구열을 가진 당신! 래번클로에 어울립니다."
        }
        
        st.write(descriptions[result])

        st.write("## 상세 결과")
        for house in ["그리핀도르", "슬리데린", "후플푸프", "래번클로"]:
            count = answers.count(house)
            st.write(f"{house}: {count}문항")

if __name__ == "__main__":
    main()
