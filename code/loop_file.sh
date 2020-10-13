while read p; 
do   python3 wp_ssrf_exploit.py "$p" $2; 
done < $1
