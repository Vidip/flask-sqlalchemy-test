#!/bin/bash

if [ -d ".venv" ]
then
    source .venv/bin/activate
else
    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install --upgrade pip
fi

pip install -r requirements.txt
python3 wsgi.py
