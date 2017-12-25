#!/bin/bash

sudo apt install -y python3-pip python3-dev && pip3 install -r requirements.txt && python3 ./server/server.py
