import streamlit as st
import cv2
from ultralytics import YOLO
import os

# Load your trained YOLOv8 model
model_path = "runs/detect/train/weights/best.pt"  # Update if needed
model = YOLO(model_path)

st.title("Logo Detection App")

# Sidebar with options
st.sidebar.title("Options")
option = st.sidebar.radio("Select an option:", ("Use Model", "Performance Details"))

if option == "Performance Details":
    st.header("Performance Details")

    # Display performance metrics (replace with your actual values)
    st.write("**Metrics from training:**")
    st.write(f"- Precision: {0.63}")
    st.write(f"- Recall: {0.67}")
    st.write(f"- mAP@0.5: {0.65}")

    # Display performance images (update the path if needed)
    st.write("**Performance Images:**")
    for filename in os.listdir("runs/detect/train"):
        if filename.endswith((".png", ".jpg")):
            st.image(os.path.join("runs/detect/train", filename))

elif option == "Use Model":
    

    # Upload a video file
    uploaded_file = st.file_uploader("Drag & Drop file", type=["mp4", "avi"])

    if uploaded_file is not None:
        # 1. Save the uploaded video temporarily
        file_bytes = uploaded_file.read()
        with open("temp_video.mp4", "wb") as out:
            out.write(file_bytes)

        # 2. Process the video
        video = cv2.VideoCapture("temp_video.mp4")
        total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        frames_with_logos = {}

        # 3. Create placeholders
        video_placeholder = st.empty()
        appearance_count_placeholder = st.empty()

        # Initialize metrics display
        appearance_count_placeholder.header("LOGO APPEARANCE COUNT")

        # 4. Process frame by frame
        current_frame = 0
        while video.isOpened():
            ret, frame = video.read()
            if not ret:
                break
            current_frame += 1

            # 5. Perform logo detection
            results = model(frame)

            # 6. Check for logos and update counts
            detected_classes = set()
            for r in results:
                if r.boxes.cls is not None:
                    for box in r.boxes:
                        cls = int(box.cls[0])
                        class_name = model.names[cls]

                        # Update appearance count
                        if class_name not in frames_with_logos:
                            frames_with_logos[class_name] = 0
                        frames_with_logos[class_name] += 1

                        detected_classes.add(class_name)

            # 7. Draw bounding boxes
            for r in results:
                boxes = r.boxes
                for box in boxes:
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # 8. Display the frame
            video_placeholder.image(frame, channels="BGR")

            # 9. Update metrics display
            appearance_counts = []
            for class_name, count in frames_with_logos.items():
                appearance_counts.append(f"{class_name} Appeared {count} times until {current_frame} frames \n")
            appearance_count_placeholder.write("\n".join(appearance_counts))

        video.release()