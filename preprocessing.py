
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


def preprocess(data, option):

    # Mengisi missing value dengan median jika ada
    #data = data.fillna(data.median())
    
    # Menghilangkan spasi, simbol dan mengecilkan huruf

    # merubah keseluruhan tulisan pada isi data

    symbol_list = [" ","!",'"',"#","%","&","'","(",")",
                "*","+",",","-",".","/",":",";","<",
                "=",">","?","@","[","\\","]","^","_",
                "`","{","|","}","~","–", "$", "Rp"]

    for char in symbol_list:
        data = data.applymap(lambda x: x.replace(char, '').lower() if type(x) == str else x)

    # merubah tulisan nama kolom
        data.columns = (data.columns.str.replace(char, '',regex=True).str.lower())

    ## Encoding data kategorikal
    def binary_map(feature):
        return feature.map({'ya': 1, 'tidak': 0})


    # Encoding label lainnya yang berkategori Ya dan Tidak
    binary_list = ['bekerja', 'telahmenikah', 'tanggungan', 'layanantelepon', 'promo']
    data[binary_list] = data[binary_list].apply(binary_map)

    # Encoding  label jenis kelamin
    data['jeniskelamin'] = data['jeniskelamin'].map({'lakilaki':1, 'perempuan':0})


    ## Mengubah/memastikan data tagihan bulanan menjadi numerik

    data['tagihanbulanan'] = pd.to_numeric(data['tagihanbulanan'], errors='coerce')

    # Mengubah data object menjadi float
    data['tagihanbulanan'] = data['tagihanbulanan'].astype(int)


    # Memasukan atribut sesuai fitur selection
    if (option == "Prediksi Satuan"):
        columns = ['bekerja', 'tanggungan', 'lamaberlangganan', 'layanantelepon', 'promo', 'multijaringan_tidakberlangganantelepon', 'multijaringan_ya', 'layananinternet_tidak', 'layananinternet_unlimited', 'vpn_ya', 'perlindungandevice_tidakberlanggananinternet', 'bantuanteknisi_tidakberlanggananinternet', 'bantuanteknisi_ya', 'streamingtv_tidakberlanggananinternet', 'streamingtv_ya', 'streamingfilm_ya', 'kontrak_per2tahun', 'kontrak_perbulan', 'metodepembayaran_kartukredit', 'metodepembayaran_lainnya', 'metodepembayaran_transferbank'
                   ]
        # Encoding label lainnya yang berkategori lebih dari 2
        data = pd.get_dummies(data).reindex(columns=columns, fill_value=0)


    elif (option == "Batch"):

        pass
        # List kolom yang dijadikan data
        data = data[[ 'idpelanggan','jeniskelamin', 'bekerja', 'telahmenikah', 'tanggungan', 'lamaberlangganan', 'layanantelepon', 'multijaringan', 'layananinternet','vpn', 'backupdata', 'perlindungandevice', 'bantuanteknisi', 'streamingtv', 'streamingfilm',
        'kontrak', 'promo', 'metodepembayaran', 'tagihanbulanan', 'totaltagihan']]

        # Memasukan atribut sesuai fitur selection
        columns = ['bekerja', 'tanggungan', 'lamaberlangganan', 'layanantelepon', 'promo', 'multijaringan_tidakberlangganantelepon', 'multijaringan_ya', 'layananinternet_tidak', 'layananinternet_unlimited', 'vpn_ya', 'perlindungandevice_tidakberlanggananinternet', 'bantuanteknisi_tidakberlanggananinternet', 'bantuanteknisi_ya', 'streamingtv_tidakberlanggananinternet', 'streamingtv_ya', 'streamingfilm_ya', 'kontrak_per2tahun', 'kontrak_perbulan', 'metodepembayaran_kartukredit', 'metodepembayaran_lainnya', 'metodepembayaran_transferbank']
        
        # Encoding label lainnya yang berkategori lebih dari 2
        data = pd.get_dummies(data).reindex(columns=columns, fill_value=0)
    else:
        print("Error")

    # feature scaling
    sc = MinMaxScaler()
    data['lamaberlangganan'] = sc.fit_transform(data[['lamaberlangganan']])
    #ata['tagihanbulanan'] = sc.fit_transform(data[['tagihanbulanan']])
    return data
