#!/bin/bash
install() {

pip3 install -r requirements.txt
mkdir database && cd database/
> database/Records.db
echo "Now , run the Python Script by the command : 'python3 employee.py'"
}

install

