if [ "$#" -ne 1 ]; then
    echo "illegal number of paramters"
else 

multiprogram=$1
multiexec="${multiprogram%.*}"
extension="${multiprogram##*.}"

if [ "$extension" = "cpp" ]; then
if g++ -pthread ~/${multiprogram} -o ~/${multiexec}; then
    echo  "-------------------------------------------------------" 
    echo -e  "\t\t"${multiprogram}" is a c++ program\t\t"
    echo  "-------------------------------------------------------"
./${multiexec}
else
    echo  "-------------------------------------------------------" 
    echo -e  "\t\t"${multiprogram}" has failed!\t\t"
    echo  "-------------------------------------------------------"
fi
else
if gcc -pthread ~/${multiprogram} -o ~/${multiexec}; then
    echo  "-------------------------------------------------------" 
    echo -e  "\t\t"${multiprogram}" is a c program\t\t"
    echo  "-------------------------------------------------------"


./${multiexec}
else
    echo  "-------------------------------------------------------" 
    echo -e  "\t\t"${multiprogram}" has failed!\t\t"
    echo  "-------------------------------------------------------"
fi
fi
fi