import pickle
import streamlit as st

# Membaca model
diabetes_model  = pickle.load(open('diabetes_model.sav', 'rb'))

#  Judul web
st.title('Data Mining Prediksi Diabetes')

# Memabagi kolomnya
col1, col2 = st.columns(2)

with col1 :
    Pregnancies = st.text_input ('Masukkan jumlah kehamilan yang pernah dialami (Pregnancies)')

with col2 : 
    Glucose = st.text_input ('Masukkan nilai Kadar gula dalam darah (Glucose)')

with col1 :
    BloodPressure = st.text_input ('Masukkan nilai Tekanan darah (Blood Pressure)')

with col2 :
    SkinThickness = st.text_input ('Masukkan nilai Ketebalan kulit (Skin Thickness)')

with col1 :
    Insulin = st.text_input ('Masukkan nilai Insulin')

with col2 :
    BMI = st.text_input ('Masukkan nilai Indeks massa tubuh (BMI)')

with col1 :
    DiabetesPedigreeFunction = st.text_input ('Masukkan nilai Diabetes Pedigree Function(Skor yang menggambarkan riwayat diabetes dalam keluarga seseorang.)')

with col2 :
    Age = st.text_input ('Masukkan usia (Age)')

# Membuat tombol untuk prediksi
if st.button('Cek Predisi Diabetes'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    
    if(diab_prediction[0] == 1):
        diab_diagnosis = 'Pasien terkena Diabetes'
    else : 
        diab_diagnosis = 'Pasien tidak terkena Diabetes'
        
    st.success(diab_diagnosis)