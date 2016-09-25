cython="test_server.c"


OUTPUT="$(find -name $cython)"
echo ${OUTPUT}

if echo "$OUTPUT" | grep -q "$cython"; then
    rm "$cython"
    echo "matched";
else
    echo "file not present";
fi

cython test_server.py -o test_server.c --embed

gcc $CFLAGS -I/usr/include/python2.7    -o test_server test_server.c -lpython2.7 -lpthread -lm -lutil -ldl