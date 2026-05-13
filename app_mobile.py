import streamlit as st

st.set_page_config(page_title="My Links", layout="centered")

st.title("📱 Quản Lý Liên Kết")

# Dữ liệu mẫu ban đầu
if 'links' not in st.session_state:
    st.session_state.links = [
        {"ten": "Google", "url": "https://google.com"},
        {"ten": "YouTube", "url": "https://youtube.com"},
        {"ten": "Facebook", "url": "https://facebook.com"}
    ]

tab1, tab2 = st.tabs(["⚡ Sử dụng", "⚙️ Cài đặt"])

with tab1:
    search = st.text_input("🔍 Tìm nhanh")
    for item in st.session_state.links:
        if search.lower() in item['ten'].lower():
            col1, col2 = st.columns([3, 1])
            col1.write(f"### {item['ten']}")
            col2.link_button("MỞ WEB", item['url'])
            st.divider()

with tab2:
    st.subheader("Thêm liên kết mới")
    new_name = st.text_input("Tên hiển thị")
    new_url = st.text_input("Địa chỉ (URL)")
    if st.button("Lưu lại"):
        if new_name and new_url:
            st.session_state.links.append({"ten": new_name, "url": new_url})
            st.success("Đã thêm thành công!")
            st.rerun()