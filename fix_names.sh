#! /usr/bin/env bash

if [ $# -lt 1 ]; then
  echo "Usage: $0 OUTPUT_DIR"
  exit 1
fi

if [ ! -d "$1" ]; then
  echo "$1 is not a directory"
  exit 2
fi

cd "$1"
mkdir ".tmp"

n=0
find -maxdepth 1 -type f -iname "*.png" | sort | while read i; do
  let "n+=1"
  fn=$(printf "frame_%07d.png" $n)
  mv "$i" ".tmp/$fn"
done

mv .tmp/* .
rmdir .tmp
cd -
