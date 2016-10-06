cython="socket_listner.c"


OUTPUT="$(find -name $cython)"
echo ${OUTPUT}

if echo "$OUTPUT" | grep -q "$cython"; then
    rm "$cython"
    echo "matched";
else
    echo "file not present";
fi

cython socket_listner.py -o c_files/socket_listner.c --embed

gcc $CFLAGS -I/usr/include/python2.7    -o socket_listner c_files/socket_listner.c -lpython2.7 -lpthread -lm -lutil -ldl