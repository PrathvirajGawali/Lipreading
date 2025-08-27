# Lipreading
Lip Reading System 🎥

A deep learning-based lip reading system that recognizes spoken words and phrases from video input. The project combines Computer Vision (OpenCV) and Deep Learning (TensorFlow/Keras) with a Streamlit frontend for real-time prediction and visualization.

Features
Detects and processes lip movements from video.
Trains a CNN + LSTM (or TimeDistributed CNN) deep learning model.
Supports real-time lip reading through a web-based Streamlit app.
Provides text output of recognized words/phrases.

Optional: Kannada translation via API.

📂 Project Structure
LipReading/
│── data/              # Dataset (MIRACL-VC1 or custom video dataset)
│── notebooks/         # Training and preprocessing notebooks
│── src/               # Source code for preprocessing, models, utils
│── app.py             # Streamlit application
│── requirements.txt   # Dependencies
│── README.md          # Project documentation

🛠️ Tech Stack
Python 3.8+
TensorFlow / Keras (Deep Learning)
OpenCV (Video processing)
Streamlit (Web app interface)
NumPy, Pandas (Data handling)

📊 Dataset
This project uses the MIRACL-VC1 dataset (or your chosen dataset).
Dataset contains videos of isolated words/phrases for lip reading.
Preprocessing includes face detection, lip region extraction, frame resizing, normalization.

⚙️ Installation
Clone the repository and install dependencies:

git clone https://github.com/yourusername/LipReading.git
cd LipReading
pip install -r requirements.txt

▶️ Usage
1. Train the Model
python train.py

2. Run the Streamlit App
streamlit run app.py


Upload a video or record through webcam → Get predicted text output.
Future Enhancements
Improve accuracy with transformer-based models.
Expand dataset for better generalization.
Deploy as a cloud-based API service.

👨‍💻 Author
Developed by Prathviraj Gawali(Computer Science Student)
