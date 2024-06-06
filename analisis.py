import pandas as pd
import matplotlib.pyplot as plt

# Membaca data penjualan
data1 = pd.read_csv('data_penjualan1.csv')
data2 = pd.read_csv('data_penjualan2.csv')
data3 = pd.read_csv('data_penjualan3.csv')

# Visualisasi jumlah barang terjual untuk setiap jenis barang
fig, axes = plt.subplots(3, 1, figsize=(8, 12))

for i, data in enumerate([data1, data2, data3]):
    ax = axes[i]
    ax.bar(data['Jenis_Barang'], data['Jumlah_Barang'], color='skyblue')
    ax.set_title(f'Data Penjualan {i+1}')
    ax.set_xlabel('Jenis Barang')
    ax.set_ylabel('Jumlah Barang Terjual')

plt.tight_layout()
plt.show()
