from skimage.io import imread
from skimage.color import rgb2gray
from skimage.filters import sobel
import matplotlib.pyplot as plt
import os
import numpy as np 

# Membaca gambar
gambar = imread(r'img\DSC01202.jpg')

gambar = np.rot90(gambar, k=1)

# Konversi ke grayscale
gambar_gray = rgb2gray(gambar)

# Deteksi tepi menggunakan Sobel
tepi_sobel = sobel(gambar_gray)

# Menampilkan hasil
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1), plt.imshow(gambar), plt.title('Citra Asli')
plt.subplot(1, 2, 2), plt.imshow(tepi_sobel, cmap='gray'), plt.title('Deteksi Tepi Sobel')

output_folder = "output"
os.makedirs(output_folder, exist_ok=True)

save_path = os.path.join(output_folder, "hasil_sobel_output.png")
plt.savefig(save_path)

plt.show()
