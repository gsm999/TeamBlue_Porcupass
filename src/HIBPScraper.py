#!/usr/bin/env python3
from typing import Union

import getpass
import hashlib
import requests

def hashP(pw_in) -> tuple:
    pw_hash = hashlib.sha1()
    pw_hash.update(str.encode(pw_in))
    digest = pw_hash.hexdigest()
    return (digest[:5], digest[5:])

def getHash(api_param) -> list:
    returnedHashes = []
    res = requests.get(f"https://api.pwnedpasswords.com/range/{api_param}", stream=True)
    for line in res.iter_lines():
        if line:
            returnedHashes.append(line.decode().split(":"))
    return returnedHashes

def check(password: str) -> Union[tuple, bool]:
    pw_hash_array = hashP(password)
    possible_hashes = getHash(pw_hash_array[0])
    for possible_hash in possible_hashes:
        if pw_hash_array[1].upper() == possible_hash[0]:
            identified_hash = pw_hash_array[0] + pw_hash_array[1]
            occurences = possible_hash[1]
            return (True, identified_hash, occurences)
    return False

def main() -> None:
    password = getpass.getpass()
    result = check(password)
    if isinstance(result, tuple) and result[0]:
        #print(f"Password found as hash {result[1]}")
        print(f"Password found: {result[2]} times")
    else:
        print("Password not found.")

if __name__ == "__main__":
    main()