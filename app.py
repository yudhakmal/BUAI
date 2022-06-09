# Import libraries
from preprocessing import preprocess
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
from PIL import Image
import pickle




# Load model
filename = 'final_model.pkl'
model = pickle.load(open(filename, "rb"))



st.set_page_config(
    page_title= "BUAI",
    page_icon= "star",
    layout= "wide",
    menu_items={
         'Get Help': None,
         'Report a bug': None,
         'About': "Aplikasi ini dibuat untuk memenuhi tugas projek akhir program kampus merdeka"
     }

)


def main():
    html = unsafe_allow_html=True

    # Load image
    image = Image.open('App.jpg')

    #st.image(image, use_column_width="always")

    #Bootstrap css
    st.markdown("""
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous" />
        """, html)
    
    #Style css
    st.markdown("""<style> 
    html {scroll-behavior: smooth;} 
    .heading3 {font-family: sans-serif; margin-bottom: 3px; font-size: 18px;}
    </style> 
    """, html)

    # Tittle, Navbar, dan Menu
    st.markdown("""
    <header id="header">
     <div class="container-fluid bg-gradient rounded mx-auto" style="background-color:rgba(255, 0, 0, 0.633); ">
        <p class="fw-bold text-center text-black" style="font-size: 50px; padding-bottom: 40px; padding-top: 5px">
            BUAI
        </p>
     </div>   
    <div class="container-fluid bg-black rounded-bottom mx-auto" style="margin-bottom:1px; margin-top:-45px">
        <p class="fw-bold text-center text-light" style="font-size: 30px;"> 
            PREDIKSI PELANGGAN BERHENTI MENGGUNAKAN LAYANAN 
        </p>
    </div>
    <div class="border-bottom rounded-3 container-fluid bg-black mx-auto" style=" margin-bottom: 0px; margin-top: -3px;">
        <p class="fw-semibold text-center text-light" style="font-size: 25px; margin-bottom:5px "> 
            Menu 
        </p>
    </div>
    </header> 
    """, html)

    selected = option_menu(
            menu_title="",
            options=["Home", "Prediksi Satuan", "Prediksi Batch", "Lainnya"],
            icons=["house", "star", "square", "list"],
            menu_icon="list",
            orientation="horizontal",
            styles={
            "container": {"text-align":"center", "background-color": "black", "margin": "auto"},
            "icon": {"text-align":"center","color": "white", "font-size": "18px"}, 
            "nav-link": {"color":"white","font-size": "18px", "text-align": "center", "margin":"0px", "--hover-color": ""},
            "nav-link-selected": {"background-color": "" },  
            }
            )
    
    
   
    with st.container():
        

        #Membuat halaman menu Prediksi Satuan
        if selected == "Prediksi Satuan":
            
            st.markdown("""<h1 id="prediksisatuan" class="fw-bold text-center">Silahkan Masukkan Data</h1>""", html)
        
            st.markdown("""<h2 class="fw-bold"> Data Pelanggan </h2>""", html)
            

            st.markdown('<p class="fw-bold heading3">Jenis Kelamin</p>', html)
            jenis_kelamin = st.radio(
                "Silahkan pilih jenis kelamin:", ('Laki-laki', 'Perempuan'))
                
        
            st.markdown('<p class="fw-bold heading3">Bekerja</p>', html)
            bekerja = st.radio(
                'Apakah pelanggan saat ini memiliki pekerjaan:', ('Ya', 'Tidak'), disabled= False)

            st.markdown('<p class="fw-bold heading3"> Telah Menikah </p>', html)
            telah_menikah = st.radio(
                'Apakah pelanggan saat ini telah menikah/berkeluarga :', ('Ya', 'Tidak'))

            st.markdown('<p class="fw-bold heading3">Tanggungan</p>', html)
            tanggungan = st.radio(
                'Apakah pelanggan memiliki tanggungan:', ('Ya', 'Tidak'))

            #Input data mengenai pembayaran customer
            st.markdown("""<h2 class="fw-bold"> Data Pembayaran Pelanggan </h2>""", html)

            st.markdown('<p class="fw-bold heading3">Lama Berlanggangan</p>', html)
            lama_berlangganan = st.slider(
                'Jumlah bulan pelanggan telah berlangganan:', min_value=0, max_value=100, value=0)
            
            st.markdown('<p class="fw-bold heading3">Kontrak</p>', html)
            kontrak = st.selectbox(
                'Jenis Kontrak:', ('Perbulan', 'Per 1 Tahun', 'Per 2 Tahun'))

            st.markdown('<p class="fw-bold heading3">Promo</p>', html)
            promo = st.radio(
                'Apakah pelanggan menggunakan promo', ('Ya', 'Tidak'))

            st.markdown('<p class="fw-bold heading3">Metode Pembayaran</p>', html)
            metode_pembayaran = st.selectbox(
                'Metode pembayaran yang digunakan', ('Transfer Bank', 'E-Wallets', 'Kartu Kredit', 'Lainnya'))
            
            st.markdown('<p class="fw-bold heading3">Tagihan Bulanan</p>', html)
            tagihan_bulanan = st.number_input(
                'Jumlah tagihan bulanan', min_value=0, max_value=2000000, value=0)

            #Input data layanan yang digunakan
            st.markdown("""<h2 class="fw-bold"> Layanan Yang Digunakan </h2>""", html)

            st.markdown('<p class="fw-bold heading3">Telepon</p>', html)

            jasa_telepon = st.radio(
                'Apakah pelanggan menggunakan layanan telepon:', ('Ya', 'Tidak'))

            if (jasa_telepon) == "Tidak":
                index_tel = 2
            else: index_tel = 0
           
                
            st.markdown('<p class="fw-bold heading3">Multi Jaringan</p>', html)    
            multi_jaringan = st.selectbox(
                "Apakah pelanggan menggunakan layanan Multi Jaringan", ('Ya', 'Tidak', 'Tidak ada layanan telepon'), index = index_tel)
            
            st.markdown('<p class="fw-bold heading3">Internet</p>', html)
            layanan_internet = st.selectbox(
                "Jenis layanan internet yang digunakan", ('FUP', 'Unlimited', 'Tidak'))

            if (layanan_internet) == "Tidak":
                index_net = 2
            else: index_net = 0
            
            st.markdown('<p class="fw-bold heading3">VPN</p>', html)
            vpn = st.selectbox(
                "Apakah pelanggan menggunakan layanan VPN", ('Ya', 'Tidak', 'Tidak berlangganan internet'), index = index_net)
            
            st.markdown('<p class="fw-bold heading3">Backup Data</p>', html)
            backup_data = st.selectbox(
                "Apakah pelanggan menggunakan layanan backup data", ('Ya', 'Tidak', 'Tidak berlangganan internet'), index = index_net)
            
            st.markdown('<p class="fw-bold heading3">Perlindungan Device</p>', html)
            perlindungan_device = st.selectbox(
                "Apakah pelanggan menggunakan layanan perlindungan device", ('Ya', 'Tidak', 'Tidak berlangganan internet'), index = index_net)

            st.markdown('<p class="fw-bold heading3">Layaanan Teknisi</p>', html)
            bantuan_teknisi = st.selectbox(
                "Apakah pelanggan menggunakan layanan jasa pengawasan oleh teknisi", ('Ya', 'Tidak', 'Tidak berlangganan internet'), index = index_net)
            
            st.markdown('<p class="fw-bold heading3">Streaming TV</p>', html)
            streaming_tv = st.selectbox(
                "Apakah pelanggan menggunakan layanan streaming TV", ('Ya', 'Tidak', 'Tidak berlangganan internet'), index = index_net)
            
            st.markdown('<p class="fw-bold heading3">Streaming Film</p>', html)
            streaming_film = st.selectbox(
                "Apakah pelanggan menggunakan layanan streaming film", ('Ya', 'Tidak', 'Tidak berlangganan internet'), index = index_net)

            data = {
                'Jenis Kelamin': jenis_kelamin,
                'Bekerja': bekerja,
                'Telah Menikah': telah_menikah,
                'Tanggungan': tanggungan,
                'Lama Berlangganan': lama_berlangganan,
                'Layanan Telepon': jasa_telepon,
                'Multi Jaringan': multi_jaringan,
                'Layanan Internet': layanan_internet,
                'VPN': vpn,
                'Backup Data': backup_data,
                'Perlindungan Device': perlindungan_device,
                'Bantuan Teknisi': bantuan_teknisi,
                'Streaming TV': streaming_tv,
                'Streaming Film': streaming_film,
                'Kontrak': kontrak,
                'Promo': promo,
                'Metode Pembayaran': metode_pembayaran,
                'Tagihan Bulanan': tagihan_bulanan,
            }

            features_df = pd.DataFrame.from_dict([data])
            st.markdown('<h2 class="fw-bold text-center"> Hasil Input </h2>', html)
            st.dataframe(features_df)

            #Preprocess input
            preprocess_df = preprocess(features_df, 'Prediksi Satuan')

            prediction = model.predict(preprocess_df)

            if st.button('Mulai Prediksi'):
                if prediction == 1:
                    st.warning(
                        'Pelanggan akan berhenti menggunakan layanan.')
                else:
                    st.success(
                        'Pelanggan akan bertahan menggunakan layanan.')



    if selected == "Prediksi Batch":
        st.markdown("""<h2 class="fw-bold text-center"> Upload Dataset </h2>""", html)
        st.info("Silahkan masukkan dataset yang disesuaikan dengan nama kolom dan pilihan kategori dari contoh berikut:")
        

        kolom = pd.DataFrame({
                'ID Pelanggan': ['0000-XXXXX','','',''],
                'Jenis Kelamin': ['Laki-Laki','Perempuan','',''],
                'Bekerja': ['Ya','Tidak','',''],
                'Telah Menikah': ['Ya','Tidak','',''],
                'Tanggungan': ['Ya','Tidak','',''],
                'Lama Berlangganan': ['Ya','Tidak','',''],
                'Layanan Telepon': ['Ya','Tidak','',''],
                'Multi Jaringan': ['Ya','Tidak','Tidak berlangganan telepon',''],
                'Layanan Internet': ['Ya','Tidak','',''],
                'VPN':['Ya','Tidak','Tidak berlangganan internet',''],
                'Backup Data': ['Ya','Tidak','Tidak berlangganan internet',''],
                'Perlindungan Device': ['Ya','Tidak','Tidak berlangganan internet',''],
                'Bantuan Teknisi': ['Ya','Tidak','Tidak berlangganan internet',''],
                'Streaming TV': ['Ya','Tidak','Tidak berlangganan internet',''],
                'Streaming Film': ['Ya','Tidak','Tidak berlangganan internet',''],
                'Kontrak': ['Perbulan','Per 1 Tahun','Per 2 Tahun',''],
                'Promo': ['Ya','Tidak','',''],
                'Metode Pembayaran': ['Transfer bank','E-Wallets','Kartu Kredit','Lainnya'],
                'Tagihan Bulanan': ['Jumlah tagihan perbulan','','',''],
        }
        )
        st.dataframe(kolom)

        uploaded_file = st.file_uploader("")
        if uploaded_file is not None:
            data = pd.read_excel(uploaded_file)
            # Get overview of data
            st.write(data.head())
            # Preprocess inputs
            pelanggan = data['ID Pelanggan']
            preprocess_df = preprocess(data, "Batch")
            if st.button('Mulai Prediksi'):
                # Get batch prediction
                prediction = model.predict(preprocess_df)
                prediction_data = prediction
                prediction_df = pd.DataFrame(data= (pelanggan, prediction_data), index=["ID Pelanggan","Hasil Prediksi"])
                prediction_df = prediction_df.replace({1: 'Ya, pelanggan akan berhenti menggunakan layanan.',
                                                       0: 'Tidak, pelanggan akan bertahan menggunakan layanan.'}).T

                st.subheader('Prediction')
                st.write(prediction_df)

        #Membuat halaman menu Home
    if selected == "Home":
        st.markdown('<h1 class=" fw-bold text-center"> Selamat datang! </h1>', html)
        st.markdown('<p class="heading3 text-center"> Ini merupakan aplikasi bla bla bla </p>', html)
        

    # Tombol kembali keatas
    st.markdown("""
    <style>
        #top a {
        padding: 1rem;
        color: #007bff;
        position: fixed;
        right: 1rem;
        bottom: 1rem;
        }
        #top a:hover {
        color: #085eb9;
        }
    </style>
    <div id="top">
    <a href="#header">
        <svg width="2em" height="2em" viewBox="0 0 16 16" class="bi bi-arrow-up-square-fill" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
        <path fill-rule="evenodd" d="M2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2zm3.354 8.354a.5.5 0 1 1-.708-.708l3-3a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1-.708.708L8.5 6.207V11a.5.5 0 0 1-1 0V6.207L5.354 8.354z"/>
        </svg>
    </a>
    </div>
    """,html)


if __name__ == '__main__':
    main()
