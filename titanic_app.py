import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Telco Customer Churn App")

st.write("Aplikasi ini menampilkan dataset Telco Customer Churn dan visualisasi sederhana.")

# Upload file CSV
uploaded_file = st.file_uploader("Upload CSV dataset Telco Churn", type="csv")

if uploaded_file:
    # Baca dataset
    df = pd.read_csv(uploaded_file)
    st.success("Dataset berhasil diupload!")
    
    # Tampilkan beberapa data teratas
    st.subheader("Preview Dataset")
    st.dataframe(df.head())

    # Info dataset
    st.subheader("Info Dataset")
    buffer = df.info(buf=None)
    st.text(df.info())

    # Statistik deskriptif
    st.subheader("Statistik Deskriptif")
    st.write(df.describe())

    # Visualisasi churn
    if 'Churn' in df.columns:
        st.subheader("Distribusi Churn")
        fig, ax = plt.subplots()
        sns.countplot(x='Churn', data=df, ax=ax)
        ax.set_title("Jumlah Churn vs Non-Churn")
        st.pyplot(fig)
    else:
        st.warning("Kolom 'Churn' tidak ditemukan di dataset.")
