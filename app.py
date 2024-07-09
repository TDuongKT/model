import streamlit as st
from PIL import Image
import os
import time
from ultralytics import YOLO

def detect_image(image_path):
    # Chạy lệnh YOLO để phát hiện đối tượng trên ảnh
    model_path = 'C:/Users/lala/OneDrive/Documents/model/last97.pt'
    model = YOLO(model_path)
    model(source=image_path, conf=0.3, save=True)

    # Tìm thư mục predict mới nhất
    run_path = 'C:/Users/lala/OneDrive/Documents/model/runs/detect'
    latest_run = max([os.path.join(run_path, d) for d in os.listdir(run_path) if os.path.isdir(os.path.join(run_path, d))], key=os.path.getmtime)
    
    # Trả về đường dẫn tới file ảnh đã được phát hiện
    result_image_path = os.path.join(latest_run, os.listdir(latest_run)[0])
    return result_image_path

def main():
    st.set_page_config(page_title="Demo Mô Hình Phát Hiện", page_icon=":camera:", layout="wide")
    
    st.title("🎥 Demo Mô Hình Phát Hiện")
    st.markdown("""
        ### Chào mừng bạn đến với ứng dụng phát hiện đối tượng!
        Ứng dụng này sử dụng mô hình YOLO để phát hiện các đối tượng trong hình ảnh của bạn. Hãy tải lên một hình ảnh và xem kết quả ngay lập tức.
    """)

    with st.sidebar:
        st.header("Menu")
        uploaded_file = st.file_uploader("Chọn một hình ảnh...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        image_dir = "C:/Users/lala/OneDrive/Documents/model/"
        if not os.path.exists(image_dir):
            os.makedirs(image_dir)
        image_path = f"{image_dir}temp_{int(time.time())}.jpg"
        image.save(image_path)

        col1, col2 = st.columns(2)

        with col1:
            st.image(image, caption='Hình ảnh đã tải lên', use_column_width=True)
            st.write("")
            st.write("Đang tìm dị vật...")

        with st.spinner('Đang xử lý...'):
            result_image_path = detect_image(image_path)
        
        with col2:
            result_image = Image.open(result_image_path)
            st.image(result_image, caption='Kết quả dự đoán', use_column_width=True)
            st.success('Tìm kiếm hoàn tất!')

if __name__ == "__main__":
    main()
