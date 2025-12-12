import streamlit as st
import math

st.set_page_config(page_title="Bangun Datar", page_icon="📐")

st.title("Hello, Streamlit!")
st.write("Welcome to your first Streamlit app.")

# =====================
# FUNGSI
# =====================
def luas_persegi(sisi):
    return sisi * sisi

def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def luas_lingkaran(r):
    return math.pi * r * r

# =====================
# SIDEBAR
# =====================
menu = st.sidebar.selectbox(
    "Pilih Bangun Datar",
    ("Luas Persegi", "Luas Segitiga", "Luas Lingkaran")
)

# =====================
# LUAS PERSEGI
# =====================
if menu == "Luas Persegi":
    st.header("Luas Persegi")

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Square_example.svg/512px-Square_example.svg.png",
        width=300
    )

    sisi = st.number_input("Masukkan panjang sisi persegi", min_value=0.0)
    if st.button("Hitung Luas Persegi"):
        luas = luas_persegi(sisi)
        st.success(f"Luas persegi = {luas}")

# =====================
# LUAS SEGITIGA
# =====================
elif menu == "Luas Segitiga":
    st.header("Luas Segitiga")

    st.image(
        "https://media.suara.com/pictures/970x544/2021/11/11/76640-rumus-luas-segitiga-jadijuaracom.jpg",
        width=300
    )

    alas = st.number_input("Masukkan alas segitiga", min_value=0.0)
    tinggi = st.number_input("Masukkan tinggi segitiga", min_value=0.0)

    if st.button("Hitung Luas Segitiga"):
        luas = luas_segitiga(alas, tinggi)
        st.success(f"Luas segitiga = {luas}")

# =====================
# LUAS LINGKARAN
# =====================
elif menu == "Luas Lingkaran":
    st.header("Luas Lingkaran")

    st.image(
        "https://www.nesabamedia.com/wp-content/uploads/2019/04/rumus-luas-lingkarang.png",
        width=300
    )

    jari_jari = st.number_input("Masukkan jari-jari lingkaran", min_value=0.0)

    if st.button("Hitung Luas Lingkaran"):
        luas = luas_lingkaran(jari_jari)
        st.success(f"Luas lingkaran = {luas:.2f}")
