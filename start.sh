#!/usr/bin/env bash

# shellcheck disable=SC1091

[[ -d "venv" ]] || python3 -m venv ./venv
source venv/bin/activate
pip install -U -r requirements.txt
python3 -m bot
