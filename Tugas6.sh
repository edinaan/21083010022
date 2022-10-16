echo -n "Input jumlah semester yang telah diikuti :";
read semester

declare -a IPSMahasiswa

i=0
let jmlsemester=$semester-1

while [ $i -le $jmlsemester ];
do
  let angka=$i+1
  printf "Nilai semester %.1i: " $angka;
  read nilaisemester;
  IPSMahasiswa[$i]=$nilaisemester;
  let total=total+$nilaisemester;
  let i=$i+1;
done

let IPKMahasiswa=$total/$semester
echo "IPSMahasiswa: " $total /  $semester
echo "IPKMahasiswa: " $IPKMahasiswa
