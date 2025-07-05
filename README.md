# Decrypter

Decrypter is a modular command line tool for decrypting, or reversing a string, or message in as many steps as you want, using various techniques.

## Installation

To use this tool, ensure you have python and any required dependencies and libraries installed.

### Cloning the Repository

```
git clone https://github.com/cDenton1/Decrypter.git
cd Decrypter
```

### Usage

For __Linux__ run the `install.sh` file or the below commands to set it up as a typical command line tool: 

```
mv decrypter.py decrypter
chmod +x decrypter
sudo ln -sf "$(pwd)/decrypter" /usr/local/bin/decrypter

gzip -c decrypter.1 > decrypter.1.gz
sudo mv decrypter.1.gz /usr/share/man/man1/
sudo mandb
```

Once setup, you don't require `python` everytime you run it, instead use:
```
decrypter <encrypted string> <options>
```

For __Windows__, the easiest way to run it, would be in whatever directory Decrypter is in and using the following command:
```
python decrypter <encrypted string>
```