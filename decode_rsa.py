from base64 import b64decode
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA

public_key = b''
cipher_text = ''
sig = ''

def decrypt_rsa():
    keyDER = b64decode(public_key)
    rsa_key = RSA.importKey(keyDER)
    raw_cipher_data = b64decode(cipher_text)
    decrypted = rsa_key.decrypt(raw_cipher_data)
    print decrypted
    return decrypted

def verify_data():
    keyDER = b64decode(public_key)
    rsa_key = RSA.importKey(keyDER)

    verifier = PKCS1_v1_5.new(rsa_key)

    h = SHA.new('mohit')
    raw_sig = b64decode(sig) 

    if verifier.verify(h, raw_sig):
        print "Success"
    else:
        print "Failure"

if __name__ == '__main__':
    verify_data()
