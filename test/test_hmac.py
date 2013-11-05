from unittest import TestCase
from hashlib import sha512
import hmac
import binascii
import binhex
import bcrypt

__author__ = 'modulus'


class TestHmac(TestCase):

    def testHmac(self):
        # If you dont have a token yet, the key should be only "CONSUMER_SECRET&"
        key = "CONSUMER_SECRET&TOKEN_SECRET"

        # The Base String as specified here:
        raw = "BASE_STRING" # as specified by oauth

        hashed = hmac.new(key, raw, sha512)

        # The signature
        print binascii.b2a_base64(hashed.digest())[:-1]
        print hashed.hexdigest()

        sha = sha512("password")
        print sha.hexdigest()

        sha2 = sha512("password")
        print sha.hexdigest() == sha2.hexdigest()

    def test(self):

        hash1 = bcrypt.hashpw("Jadda", bcrypt.gensalt())
        hash2 = bcrypt.hashpw("Jadda", hash1)

        print hash1
        print hash1 == hash2