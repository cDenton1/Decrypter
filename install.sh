#!/bin/bash

mv decrypter.py decrypter
chmod +x decrypter
sudo ln -sf "$(pwd)/decrypter" /usr/local/bin/decrypter
echo "Installed or updated Decrypter"
