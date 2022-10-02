echo -n "Masukkan angka1 yang akan dioperasikan : ";
read angka1 ;
echo -n "Masukkan angka2 yang akan dioperasikan : ";
read angka2 ;

let kali=angka1*angka2
let bagi=angka1/angka2
let mod=angka1%angka2

echo "Operasi apa yang ingin kamu lakukan?"
echo "perkalian ?"
echo "pembagian ?"
echo "modulus ?"

read operasi

case "$operasi" in
  "perkalian")
    echo "angka1 * angka2 = $kali"
    ;;
  "pembagian")
    echo "angka1 / angka2 = $bagi"
    ;;
  "modulus")
    echo "sisa bagi = $mod"
    ;;
  *)
    echo "Tidak dapat dioperasikan"
    ;;
esac
