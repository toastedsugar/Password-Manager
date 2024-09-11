from flask import Blueprint, request
import functools
import bcrypt

from .authUtils import GenerateToken, VerifyToken

# Create blueprint
AuthBlueprint = Blueprint("auth", __name__, url_prefix="/auth")

# Before the blueprint, check if user exists. If not, return error.

# Handle register 
@AuthBlueprint.route("/register", methods=["GET"])
def Register():
    # Extract username and password from the request
    # Hash the password with a salt
    # Generate access token and refresh token
    # Create new <User> and store the username, hashed password, salt, refresh token and access token
    # However if user exists, return error
    # return access token.
    return "Trying to register!"


# Handle  login here
@AuthBlueprint.route("/login", methods=["GET"])
def Login():
    # Extract username and password from the request
    # Check if username exists in database. If user does not exist return error, otherwise look up username, hashed password and salt.
    # Compare hashed password with extracted password. 
    # If match, generate access token jwt containing username and timestamp.
    # Store token in cookie and send it to client
    return "Trying to login!"
    
    
@AuthBlueprint.route("/register", methods=["GET"])
def Logout():
    # Remove access and refresh tokens from database
    return "Logged out!"


# Handle Access token stuff
@AuthBlueprint.route("/accessToken", methods=["GET", "POST", "DELETE", "PATCH"])
def AccessToken():
    return "Access"


# Handle refresh token stuff
@AuthBlueprint.route("/refreshToken", methods=["GET", "POST", "DELETE", "PATCH"])
def RefreshToken():
    return "Refresh"