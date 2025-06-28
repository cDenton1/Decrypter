#!/bin/bash

mv decrypter.py decrypter
chmod +x decrypter
sudo ln -sf "$(pwd)/decrypter" /usr/local/bin/decrypter

gzip -c decrypter.1 > decrypter.1.gz
sudo mv decrypter.1.gz /usr/share/man/man1/
sudo mandb

echo "Installed or updated Decrypter"
