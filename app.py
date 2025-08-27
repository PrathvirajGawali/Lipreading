import streamlit as st
import cv2
import numpy as np
import base64
import tempfile
import os
from tensorflow.keras.models import load_model
from config import LABELS, IMG_SIZE, MAX_LEN
from utils.kannada_translation import get_kannada_translation

# ----------------------
# Page Setup + Compact Styling
# ----------------------
st.set_page_config(page_title="Lip Reading App", layout="centered")

# Shrink margins, padding, and font sizes
st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
            padding-left: 2rem;
            padding-right: 2rem;
        }
        h1 {
            font-size: 1.5rem;
        }
        .stSelectbox label, .stFileUploader label {
            font-size: 0.9rem;
        }
        .stMarkdown, .stSpinner, .stButton, .stSelectbox, .stFileUploader {
            font-size: 0.9rem;
        }
    </style>
""", unsafe_allow_html=True)

# ----------------------
# Helper Dictionaries
# ----------------------
label_dict = {k: i for i, k in enumerate(LABELS)}
reverse_dict = {v: k for k, v in label_dict.items()}

# ----------------------
# Video Preprocessing
# ----------------------
def preprocess_video(video_path, max_len=MAX_LEN, img_size=IMG_SIZE):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(gray, (img_size, img_size))
        frames.append(resized)
    cap.release()

    if len(frames) < 8:
        raise ValueError("Video does not have enough frames (minimum 8).")

    if len(frames) < max_len:
        frames += [np.zeros((img_size, img_size)) for _ in range(max_len - len(frames))]
    else:
        frames = frames[:max_len]

    frames = np.array(frames).reshape(max_len, img_size, img_size, 1).astype('float32') / 255.0
    return np.expand_dims(frames, axis=0)

# ----------------------
# Prediction Logic
# ----------------------
def predict_from_video(video_path, model_path):
    model = load_model(model_path)
    input_tensor = preprocess_video(video_path)
    prediction = model.predict(input_tensor)
    predicted_index = np.argmax(prediction)
    predicted_key = list(label_dict.keys())[list(label_dict.values()).index(predicted_index)]
    predicted_label = LABELS.get(predicted_key, "Unknown")
    return predicted_label

# ----------------------
# Streamlit UI
# ----------------------
st.title("🧠 Visual Speech Recognition")
st.write("Upload a video of lip movements to classify the spoken word or phrase.")

model_choice = st.selectbox("Choose a model", ["Words", "Phrases"], index=0)
video_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])

# Create placeholders to show prediction before upload
english_placeholder = st.markdown("**🔤 English Prediction:** `—`")
kannada_placeholder = st.markdown("**🌐 Kannada Translation:** `—`")

if video_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp:
        tmp.write(video_file.read())
        tmp_path = tmp.name

    # Display video in smaller size (300x200)
    video_bytes = open(tmp_path, 'rb').read()
    base64_video = base64.b64encode(video_bytes).decode()
    video_html = f"""
    <video width="300" height="200" controls>
      <source src="data:video/mp4;base64,{base64_video}" type="video/mp4">
      Your browser does not support the video tag.
    </video>
    """
    st.markdown(video_html, unsafe_allow_html=True)

    model_path = "models/model_words.keras" if model_choice == "Words" else "models/model_phrases.keras"

    with st.spinner("Processing and predicting..."):
        try:
            predicted_label = predict_from_video(tmp_path, model_path)
            kannada_translation = get_kannada_translation(predicted_label)

            st.success("Prediction Complete 🎉")
            english_placeholder.markdown(f"**🔤 English Prediction:** `{predicted_label}`")
            kannada_placeholder.markdown(f"**🌐 Kannada Translation:** `{kannada_translation}`")

        except Exception as e:
            st.error(f"❌ Error during prediction: {e}")

    os.remove(tmp_path)
