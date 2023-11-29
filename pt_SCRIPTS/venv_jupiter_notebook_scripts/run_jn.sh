#! /usr/bin/env bash

jptntbk="folium_test_d.ipynb"

if [ ! -d venv ]; then
    echo "Must run inside 'venv' virtual environment!"
    exit 1
else
    ./venv/bin/jupyter notebook ${jptntbk}
fi


