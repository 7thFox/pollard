# pollard

This project was done as a part of my cryptography class.
The program takes the public key (e, N) and attacks they key using Pollard's p-1 attack.
It will then output either the private key (d, N), or an error.

# example usage

 ```
$ python pollard.py
Please enter N: 7029871
Please enter e: 15
Private Key (d, N): (6561213, 7029871)
```
