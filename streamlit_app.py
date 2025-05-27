import streamlit as st

st.title("🎈Hai selamat datang di web ini")
st.write(
    "Belajar ngoding bareng mayra"
)
st.image("IMG-20250526-WA0018.jpg", width=200) 

st.title("Aplikasi Sederhana") 
st.header= st.("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1) 

if (angka % 2) == 0:
    st.write(f"(angka) adalah Bilangan Genap") 
else :
    st.write(f"(angka) adalah Bilangan Ganjil") -! 
