#!/bin/bash

DIR_HOME=$(pwd)

export PYTHONPATH="${PYTHONPATH}:$DIR_HOME"

python3 agreement/manage.py $1 $2