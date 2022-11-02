# Mendeklarasikan fungsi
luas_persegi() {
            echo "Masukkan Panjang : "
            read a
            echo "Masukkan Lebar : "
            read b
            luas
}
luas() {
            let kali=$a*$b
            echo -e "Luas Persegi : \n$kali"
}

# Memanggil fungsi
luas_persegi

