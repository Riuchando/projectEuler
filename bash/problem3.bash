ar=(factor 600851475143)
#IFS=$'\n'
#echo "${ar[*]}" | sort -nr | head -n2

max=0
for n in "${ar[@]}" ; do
    ((n > max)) && max=$n
done
echo $max
