from PIL import Image

def change_background_to_white(input_path, output_path):
    # Buka gambar menggunakan Pillow
    img = Image.open(input_path)

    # Buat gambar baru dengan mode 'RGB' dan warna putih sebagai background
    new_img = Image.new('RGB', img.size, (255, 255, 255))

    # Jika gambar asli memiliki lapisan transparansi (alpha channel), hilangkan lapisan tersebut
    if img.mode == 'RGBA':
        img = img.convert('RGB')

    # Tempelkan gambar asli ke gambar baru
    new_img.paste(img, (0, 0))

    # Simpan gambar dengan background putih
    new_img.save(output_path, format='PNG')

if __name__ == "__main__":
    input_image_path = 'waw.png'  # Ganti dengan path gambar PNG yang diinginkan
    output_image_path = 'output.png'  # Ganti dengan path tempat Anda ingin menyimpan gambar dengan background putih

    change_background_to_white(input_image_path, output_image_path)
