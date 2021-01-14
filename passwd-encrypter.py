from cryptography.fernet import Fernet
import sys
string = sys.argv[1]

byte_str = bytes(string, encoding='utf8')
key = Fernet.generate_key()
cipher_suite = Fernet(key)

cipher_text = cipher_suite.encrypt(byte_str)
plain_text = cipher_suite.decrypt(cipher_text)

return(f"The cipher text for {byte_str} is {cipher_text}.")
