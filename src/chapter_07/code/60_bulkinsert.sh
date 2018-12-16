#!/usr/bin/env sh

for file in `\find ../resources/ -maxdepth 1 -name name-to-area-*.txt`; do
  cat ../resources/${file} | redis-cli -h myredis -p 6379
done

for file in `\find ../resources/ -maxdepth 1 -name namelist-*.txt`; do
  cat ../resources/${file} | redis-cli -h myredis -p 6379
done
