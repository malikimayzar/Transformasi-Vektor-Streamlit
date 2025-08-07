import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

# Import fungsi dari tiap file
import rotasi
import refleksi
import scaling
import shearing

# =============== UI Streamlit ===============
st.set_page_config(page_title="Transformasi Linear 2D", layout="centered")
st.title("🔄 Aplikasi Visualisasi Transformasi Linear 2D")

# Input vektor awal
x = st.number_input("Komponen X", value=1.0)
y = st.number_input("Komponen Y", value=2.0)
v = np.array([x, y])

# Pilih jenis transformasi
transformasi = st.selectbox("Pilih Jenis Transformasi", ["Rotasi", "Refleksi", "Scaling", "Shearing"])
tampilkan_animasi = st.checkbox("Tampilkan Animasi", value=True)

# Transformasi sesuai pilihan
if transformasi == "Rotasi":
    sudut = st.slider("Sudut Rotasi (derajat)", -180, 180, 45)
    v_hasil = rotasi.vektor_rotasi(vektor=v, theta_derajat=sudut)
    nama_gif = "HasilTransformasi/animasi_rotasi.gif"
    if tampilkan_animasi:
        rotasi.animasi_rotasi(v, v_hasil, nama_file=nama_gif)

elif transformasi == "Refleksi":
    sumbu = st.selectbox("Sumbu Refleksi", ["x", "y", "y = x", "y = -x"])
    v_hasil = refleksi.vektor_refleksi(vektor=v, jenis_refleksi=sumbu)
    nama_gif = "HasilTransformasi/animasi_refleksi.gif"
    if tampilkan_animasi:
        refleksi.animasi_refleksi(v, v_hasil, nama_file=nama_gif)

elif transformasi == "Scaling":
    sx = st.number_input("Skala X", value=1.0)
    sy = st.number_input("Skala Y", value=1.0)
    v_hasil = scaling.vektor_scaling(vektor=v, scale_kamu=(sx, sy))
    nama_gif = "HasilTransformasi/animasi_scaling.gif"
    if tampilkan_animasi:
        scaling.animasi_scaling(vektor_awal=v, vektor_akhir=v_hasil, nama_file=nama_gif)

elif transformasi == "Shearing":
    arah = st.selectbox("Arah Shearing", ["x", "y"])
    k = st.number_input("Faktor Shearing", value=1.0)
    v_hasil = shearing.vektor_shearing(vektor=v, jenis_shearing=arah, k=k)
    nama_gif = "HasilTransformasi/animasi_shearing.gif"
    if tampilkan_animasi:
        shearing.animasi_shearing(v, v_hasil, nama_file=nama_gif)

# ================= OUTPUT =================
st.subheader("🔢 Hasil Transformasi:")
st.write("Vektor awal:", v)
st.write("Vektor hasil:", v_hasil)

# Tampilkan animasi
if tampilkan_animasi and os.path.exists(nama_gif):
    st.image(Image.open(nama_gif), caption="Animasi Transformasi", use_column_width=True)
