# Decrypter

Decrypter is a modular command-line tool for decoding or reversing strings using various techniques. You can apply multiple decoding methods step-by-step, and some techniques even include other options for brute forcing, digit shifting, and even character substitution.

## Installation

To use this tool, ensure you have python and any required dependencies and libraries installed.

### Cloning the Repository

```
git clone https://github.com/cDenton1/Decrypter.git
cd Decrypter
```

### Usage

#### Windows

```
python decrypter <encrypted string> [-f <file>] [-o] [-m] [-h]
```

#### Linux

Run the `install.sh` file or the below commands to set it up as a typical command line tool: 

```
mv decrypter.py decrypter
chmod +x decrypter
sudo ln -sf "$(pwd)/decrypter" /usr/local/bin/decrypter

gzip -c decrypter.1 > decrypter.1.gz
sudo mv decrypter.1.gz /usr/share/man/man1/
sudo mandb
```
```
decrypter <encrypted string> [-f <file>] [-o] [-m] [-h]
```

![Usage Example Kali Linux](/assets/output1.png "Usage Example Kali Linux")

## Module Expansion

Adding a new module requires the following:

- The file must be in the __modules__ subfolder
- The filename must start with 'mod' and end with '.py'
- Must include a callable function, 'conv'
