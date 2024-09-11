'''
Helper functions for authentication module
'''
import secrets
import jwt

'''
A function that generates and returns a JWT
payload:    Dictionary that contains user data (username, password hash, timestamp, etc...)
key:        Environment variable
'''
def GenerateToken(User):
    # Generate and return a random 16 bit URL safe token
    return jwt.encode(payload=User, key="change_me!")

'''
A function that generates and returns a JWT
User:       Dictionary that contains user data (username, password hash, etc...)
Secret:     Environment variable
'''
def VerifyToken():
    return 1



def VerifyTimestamp(timestamp, token_duration):
    return True