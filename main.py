import streamlit as st
import random

st.set_page_config(page_title="풀 코디 추천기", page_icon="🧥", layout="centered")

st.markdown("""
    <style>
    .main-title {
        font-size: 42px;
        font-weight: bold;
        color: #2C3E50;
        text-align: center;
        margin-bottom: 30px;
    }
    .subtitle {
        font-size: 20px;
        color: #7F8C8D;
        text-align: center;
        margin-bottom: 25px;
    }
    .result-box {
        background-color: #fdfdfd;
        border-left: 6px solid #5DADE2;
        padding: 20px;
        font-size: 18px;
        color: #2C3E50;
        margin-top: 25px;
        border-radius: 6px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🧥 상황별 디테일 코디 추천기</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">상의, 하의, 가방, 모자, 액세서리까지 랜덤으로 풀코디 추천!</div>', unsafe_allow_html=True)

# 전체 색상 리스트 (포인트 색상 포함)
colors = ["화이트", "블랙", "베이지", "네이비", "카키", "그레이", "하늘색", "버건디", "브라운", "올리브"]

# 하의용 색상 (무난한 색상)
bottom_colors = ["베이지", "차콜", "블랙", "화이트"]

# 포인트 색상 (1개 이상 나오면 안 되는 색)
point_colors = ["파랑", "핑크", "오렌지"]

# 참고: "파랑" 대신 "네이비", "하늘색" 같은 유사색을 색상 리스트에 넣었는데
# 포인트 색상 카운트는 여기서 '파랑' 기준이므로, "네이비"와 "하늘색"은 포인트 색상에서 제외 처리 가능.

# 그래서 실제 색상 이름이 포인트 색상과 겹치면 안됨.
# 위 colors 리스트엔 '파랑' 없음 → 따라서, 포인트 색상 "파랑" 체크가 의미 없으니
# 포인트 색상 리스트를 '하늘색', '핑크', '오렌지'로 바꾸겠습니다!

point_colors = ["하늘색", "핑크", "오렌지"]

outfit_data = {
    "남자": {
        "상의": ["셔츠", "반팔 티셔츠", "맨투맨", "니트", "후드티"],
        "하의": ["슬랙스", "청바지", "조거팬츠", "반바지", "면바지"],
        "가방": ["백팩", "크로스백", "토트백"],
        "모자": ["볼캡", "비니", "버킷햇"],
        "액세서리": ["시계", "팔찌", "목걸이", "없음"]
    },
    "여자": {
        "상의": ["블라우스", "크롭티", "니트", "셔츠", "티셔츠"],
        "하의": ["스커트", "청바지", "와이드팬츠", "레깅스", "반바지"],
        "가방": ["크로스백", "숄더백", "클러치"],
        "모자": ["버킷햇", "볼캡", "베레모"],
        "액세서리": ["귀걸이", "목걸이", "반지", "없음"]
    }
}

situation_tags = ["데이트", "운동", "출근", "여행", "파티", "비오는 날"]

gender = st.radio("👤 성별을 선택하세요:", options=["남자", "여자"], horizontal=True)
situation = st.selectbox("📌 상황을 선택하세요:", situation_tags)

def pick_color(possible_colors, used_point_count):
    """
    포인트 색상 1개 이상이면 포인트 색상 제외 후 뽑기
    """
    if used_point_count >= 1:
        # 포인트 색상 제외
        filtered = [c for c in possible_colors if c not in point_colors]
        if filtered:
            return random.choice(filtered)
        else:
            # 만약 모두 포인트 색상이라면 그냥 뽑기
            return random.choice(possible_colors)
    else:
        return random.choice(possible_colors)

if st.button("✨ 풀코디 추천 받기"):
    point_count = 0

    # 상의 색상
    top_color = pick_color(colors, point_count)
    if top_color in point_colors:
        point_count += 1
    top = random.choice(outfit_data[gender]["상의"])

    # 하의 색상 (무조건 bottom_colors 사용)
    bottom_color = pick_color(bottom_colors, point_count)
    if bottom_color in point_colors:
        point_count += 1
    bottom = random.choice(outfit_data[gender]["하의"])

    # 가방 색상
    bag_color = pick_color(colors, point_count)
    if bag_color in point_colors:
        point_count += 1
    bag = random.choice(outfit_data[gender]["가방"])

    # 모자 색상
    hat_color = pick_color(colors, point_count)
    if hat_color in point_colors:
        point_count += 1
    hat = random.choice(outfit_data[gender]["모자"])

    accessory = random.choice(outfit_data[gender]["액세서리"])

    st.markdown(f"""
        <div class="result-box">
        <h4>📍 [{gender}] {situation} 코디 추천</h4>
        👕 상의: <strong>{top}</strong> ({top_color})<br>
        👖 하의: <strong>{bottom}</strong> ({bottom_color})<br>
        🎒 가방: <strong>{bag}</strong> ({bag_color})<br>
        🧢 모자: <strong>{hat}</strong> ({hat_color})<br>
        💍 액세서리: <strong>{accessory}</strong>
        </div>
    """, unsafe_allow_html=True)
