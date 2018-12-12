#!/usr/bin/env sh

cat ../resources/namelist.txt | redis-cli -h myredis -p 6379
cat ../resources/name-area.txt | redis-cli -h myredis -p 6379
