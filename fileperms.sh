#!/bin/bash

filename="$1"
if [ "$filename" = "" ] ; then
    echo Usage: pathperms.sh filename
    exit 1
fi

ls -ld "$filename"
dir=$( realpath "$filename")
dir=$( dirname "$dir")
while [ "$dir" != "/" ]
do
    ls -ld "$dir"
    dir=$( dirname "$dir")
done
exit 0

