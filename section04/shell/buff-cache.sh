#!/usr/bin/bash

echo "show the size of used memory before creating file"
free

echo "make new 1GB file. 1GB page cache on the memory"
dd if=/dev/zero of=testfile bs=1M count=1K

echo "show the size of used memory with page cache"
free

echo "show the size of used memory after removing the file"
rm testfile
free
