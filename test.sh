#!/bin/bash
touch src/increment-build.cpp
./build.py flash && sleep 2 && particle serial monitor