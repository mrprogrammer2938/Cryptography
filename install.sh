#!/usr/bin/env bash
# This Programm Write by Mr.nope
# Cryptographt v1.3.0
if [[ "$(id -u)" -ne 0 ]]; then
  echo "
Please, Run This Programm as Root!
"
  exit 1
fi
main() {
      printf '\033];2Cryptography\a'
      clear
      echo "Installing..."
      chmod +x crypt.py
      sleep 2
      apt install python && apt install python3
      apt install python3-pip
      pip3 install --upgrade pip
      echo "
Finish...!

Usage:
      python3 crypt.py
"
      exit 1
}
main
