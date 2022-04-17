#!/bin/bash
python3 -m pip install --upgrade virtualenv
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload