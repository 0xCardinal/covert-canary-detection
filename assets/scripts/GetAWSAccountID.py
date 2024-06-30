# https://medium.com/@TalBeerySec/a-short-note-on-aws-key-id-f88cc4317489

import base64
import binascii
import argparse

def AWSAccount_from_AWSKeyID(AWSKeyID):
    trimmed_AWSKeyID = AWSKeyID[4:]  # remove KeyID prefix
    x = base64.b32decode(trimmed_AWSKeyID)  # base32 decode
    y = x[0:6]
    
    z = int.from_bytes(y, byteorder='big', signed=False)
    mask = int.from_bytes(binascii.unhexlify(b'7fffffffff80'), byteorder='big', signed=False)
    
    e = (z & mask) >> 7
    return e

def main():
    parser = argparse.ArgumentParser(description='Convert AWS Key ID to AWS Account ID.')
    parser.add_argument('AWSKeyID', type=str, help='The AWS Key ID to convert')
    args = parser.parse_args()
    
    account_id = AWSAccount_from_AWSKeyID(args.AWSKeyID)
    print("AWS Account ID: " + "{:012d}".format(account_id))

if __name__ == "__main__":
    main()
