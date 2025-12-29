🧠 EEG Mental State Prediction using Machine Learning

This project implements a machine learning–based EEG signal classification system to predict human mental/eye state (Open / Closed) using EEG channel data.
The best-performing Neural Network (MLP) model is deployed as an interactive Streamlit web application.

🚀 Live Demo

👉 Streamlit App:
https://<your-streamlit-app-link>.streamlit.app

📌 Problem Statement

Electroencephalogram (EEG) signals capture electrical activity of the brain.
The goal of this project is to classify EEG signals into two mental states using supervised machine learning techniques.

📊 Dataset

EEG Eye State Dataset

Multiple EEG channels as input features

Target variable:

0 → Eye Open / Relaxed State

1 → Eye Closed / Active State

🧠 Models Used
Model	Description
Random Forest	Ensemble-based classical ML model
Neural Network (MLP)	Multi-layer Perceptron with ReLU activation

📌 Best Model Selected: Neural Network (MLP)

⚙️ Project Workflow
EEG Dataset
   ↓
Data Preprocessing & Scaling
   ↓
Model Training (RF & MLP)
   ↓
Model Evaluation & Comparison
   ↓
Best Model Selection
   ↓
Streamlit Deployment

📂 Project Structure
EEG-Mental-State-Prediction/
│
├── app/
│   └── streamlit_app.py
│
├── models/
│   ├── best_model.pkl
│   └── scaler.pkl
│
├── data/
│   └── test.csv
│
├── notebooks/
│   └── eeg_data_project.ipynb
│
├── requirements.txt
├── README.md
└── .gitignore

📈 Model Performance
Model	Accuracy
Random Forest	~95%
Neural Network (MLP)	~96%
🖥️ Streamlit Web App Features

User-friendly EEG channel input

Real-time prediction

Neural Network inference

Lightweight & fast deployment

▶️ How to Run Locally
1️⃣ Clone Repository
git clone https://github.com/your-username/EEG-Mental-State-Prediction.git
cd EEG-Mental-State-Prediction

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run Streamlit App
streamlit run app/streamlit_app.py

📦 Requirements
streamlit
numpy
scikit-learn
joblib

🎯 Use Cases

Brain–Computer Interface (BCI)

Cognitive state analysis

EEG-based healthcare research

Human–computer interaction

🧪 Future Enhancements

Deep Learning (CNN/LSTM on raw EEG signals)

Real-time EEG hardware integration

Multi-class mental state classification

CSV upload for batch predictions

Cloud deployment (AWS / GCP)

👨‍💻 Author

Ashish Rakshe
Bachelor of Science | Aspiring Data Scientist
📌 GitHub: https://github.com/your-username

📌 LinkedIn: https://linkedin.com/in/your-profile

📜 License

This project is licensed under the MIT License.
