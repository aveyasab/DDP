import streamlit as streamlit

st.title("Form Data Diri")
st.write("Silahkan Isi Data Diri Anda")
st.write("Made by Basa")

with st.form("form_data_diri")
     nama = st.text_input("Nama")
     alamat = st.text_input("Alamat")
     usia = st.number_input("Usia")
     submit = st.form_submit_button("Submit")