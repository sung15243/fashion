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

# 색상 리스트
colors = ["화이트", "블랙", "베이지", "네이비", "카키", "그레이", "하늘색", "버건디", "브라운", "올리브"]
bottom_colors = ["베이지", "차콜", "블랙", "화이트"]  # 부담 없는 하의 색상
bag_colors = ["블랙", "베이지", "브라운", "네이비", "카키", "그레이", "화이트"]  # 톤 다운 가방 색상

point_colors = ["하늘색", "핑크", "오렌지"]  # 포인트 색상 최대 1개 허용

# 보색(충돌) 리스트
color_clash = {
    "화이트": [],
    "블랙": [],
    "베이지": ["버건디"],
    "네이비": ["카키", "오렌지"],
    "카키": ["네이비", "버건디"],
    "그레이": [],
    "하늘색": ["브라운"],
    "버건디": ["베이지", "카키"],
    "브라운": ["하늘색"],
    "올리브": ["버건디"],
}

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
        filtered = [c for c in possible_colors if c not in point_colors]
        if filtered:
            return random.choice(filtered)
        else:
            return random.choice(possible_colors)
    else:
        return random.choice(possible_colors)

def pick_color_no_clash(possible_colors, used_colors, used_point_count):
    tries = 0
    while tries < 10:
        color = pick_color(possible_colors, used_point_count)
        clash = False
        for uc in used_colors:
            if color in color_clash.get(uc, []) or uc in color_clash.get(color, []):
                clash = True
                break
        if not clash:
            return color
        tries += 1
    return color

if st.button("✨ 풀코디 추천 받기"):
    point_count = 0
    used_colors = []

    top_color = pick_color_no_clash(colors, used_colors, point_count)
    if top_color in point_colors:
        point_count += 1
    used_colors.append(top_color)
    top = random.choice(outfit_data[gender]["상의"])

    bottom_color = pick_color_no_clash(bottom_colors, used_colors, point_count)
    if bottom_color in point_colors:
        point_count += 1
    used_colors.append(bottom_color)
    bottom = random.choice(outfit_data[gender]["하의"])

    bag_color = pick_color_no_clash(bag_colors, used_colors, point_count)
    if bag_color in point_colors:
        point_count += 1
    used_colors.append(bag_color)
    bag = random.choice(outfit_data[gender]["가방"])

    hat_color = pick_color_no_clash(colors, used_colors, point_count)
    if hat_color in point_colors:
        point_count += 1
    used_colors.append(hat_color)
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
