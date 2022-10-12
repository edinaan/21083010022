# deklarasikan array (explicit declaration)
declare -a angka

# clear
i=0;
while [ $i -le 4 ];
do
  let isi=$i*2;
  angka[$i]=$isi;
  let i=$i+1;
done

# tampilkan semua elemen array
# dengan indexnya berisi "*" atau "@"
echo ${angka[@]}
