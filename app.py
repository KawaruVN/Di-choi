import streamlit as st

st.set_page_config(page_title="Thiệp Mời Đi Chơi 💌", page_icon="🌸")

# Custom CSS style for cuteness
st.markdown("""
    <style>
    .title {
        font-size: 40px;
        text-align: center;
        color: #ff69b4;
        font-weight: bold;
        font-family: 'Comic Sans MS', cursive;
    }
    .subtitle {
        font-size: 20px;
        text-align: center;
        color: #555;
    }
    .menu-box {
        background-color: #ffe6f0;
        padding: 20px;
        border-radius: 15px;
        font-size: 18px;
    }
    .button-container {
        text-align: center;
        margin-top: 30px;
    }
    .note {
        font-style: italic;
        color: #c94f7c;
    }
    </style>
""", unsafe_allow_html=True)

# Nội dung chính
st.markdown('<div class="title">💌 Thiệp Mời Đặc Biệt 💌</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Gửi đến Dương Phan Vân Ngọc - Cậu rảnh không? Mình có kèo nè 😚</div>', unsafe_allow_html=True)

st.divider()

st.write("📍 **Thời gian**: 2h chiều | Ngày đi chơi nè!")  
st.write("📍 **Đón tại**: 02 Cửu Long")  
st.write("🎒 **Dresscode**: Mặc gì cũng được, miễn là cậu thấy xinh ✨")

st.markdown('<br>', unsafe_allow_html=True)

# Menu cuộc hẹn
st.markdown('<div class="menu-box">', unsafe_allow_html=True)
st.markdown("### 🍡 Lịch Trình Cuộc Hẹn")
menu = [
    "🏹 Bắn cung tại Vincom Plaza 3/2",
    "🍜 Ăn mì tương đen Hàn tại Hẻm 107 Trần Hưng Đạo",
    "🌳 Chill chill ở công viên Gia Định"
]
for item in menu:
    st.markdown(f"- {item}")
st.markdown('</div>', unsafe_allow_html=True)

# Lời nhắn
st.markdown('<br>', unsafe_allow_html=True)
st.markdown("""
> 📝 *Chuyến đi này mình lên plan sẵn hết rồi, chỉ còn thiếu một điều làm nó hoàn hảo hơn… là cậu đó ☺️*  
> *Nếu cậu đi, mình hứa sẽ là người guide dễ thương nhất ngày hôm đó!* 💖
""")

# Nút lựa chọn
col1, col2 = st.columns(2)
with col1:
    if st.button("✅ Tui đi nè 😎"):
        st.success("Yeahhhh 🥳 Cậu đồng ý rồi! Hẹn gặp nhaaaa 💕")
with col2:
    if st.button("❌ Tiếc ghê, tui bận mất rồi 🥲"):
        st.warning("Tèn ten... Vậy để hôm khác mình rủ lại nha 😢")

st.markdown('<br><div class="note">(Sau khi cậu chọn, nhớ nhắn mình biết nữa nha 😄)</div>', unsafe_allow_html=True)

# Ảnh bé Pam sẽ được thêm sau khi bạn gửi
