import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from babel.numbers import format_currency

sns.set(style='dark')

# Kumpulan DataSet
day_bike = pd.read_csv("day.csv")

# Menghapus duplikat
day_bike.drop_duplicates(inplace=True)

# Mengubah kolom 'dteday' Menjadi datetime
day_bike['dteday'] = pd.to_datetime(day_bike['dteday'])

# Sidebar
st.sidebar.title("Data Exploration")

# Menampilkan Informasi DataSet
st.sidebar.subheader("Dataset Information")
st.sidebar.text(day_bike.info())

# Menampilkan nilai yang hilang
st.sidebar.subheader("Missing Values")
st.sidebar.text(day_bike.isna().sum())

# Menampilkan duplikat
st.sidebar.subheader("Duplicates")
st.sidebar.text("Jumlah duplikasi: {}".format(day_bike.duplicated().sum()))

# Menampilkan Deskripsi statistik
st.sidebar.subheader("Descriptive Statistics")
st.sidebar.text(day_bike.describe(include="all"))

# isi utama
st.title("Bike Rental Analysis")

# Tren Penyewaan Sepeda Bulanan pada Tahun 2011
st.subheader("Monthly Bike Rentals in 2011")
monthly_rentals_2011 = day_bike[day_bike['dteday'].dt.year == 2011].groupby(day_bike['dteday'].dt.month)['cnt'].sum()
st.line_chart(monthly_rentals_2011)

# Total Penyewaan Sepeda Berdasarkan cuaca
st.subheader("Total Bike Rentals Based on Weather")
cuaca = day_bike.groupby('weathersit')['cnt'].sum()
st.bar_chart(cuaca)

# Total Penyewaan Sepeda Berdasarkan hari
st.subheader("Total Bike Rentals Based on Holiday")
hari = day_bike.groupby('holiday')['cnt'].sum()
st.bar_chart(hari)

