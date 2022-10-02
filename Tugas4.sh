echo -n "Masukkan angka ganjil: ";
read a

until [ ! $a -ge 1 ]
do
  echo $a
  a=$((a - 2))
done
