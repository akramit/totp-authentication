# Time-Based One-Time Password Algorithm
Time-Based One-Time Password Algorithm or TOTP in short is a time based codes for single use, which is valid only for short duration of time, which protects against any kind of compromise due to short lived nature. This is often used in 2FA (2 Factor authentication) systems. 2FA provides an extra layer of security, by requiring two kind of passwords - something a user knows (like password) and something a user have (like phone to generate OTP). 

Here, I provide a simple implementation of TOTP in python which anyone can use for their own purpose (or better - write your own;). Below, I have explained the algorithm. 

TOTP is an extension of HOTP (HMAC based One-Time Password) and follows an open standard documented in [RFC6238](https://datatracker.ietf.org/doc/html/rfc6238). 

Authentication Apps supporting TOTP - *Authy, Google Authenticator*
<!-- Put image of Google Authenticator here. -->
<!-- Example of TOTP  by using Zerodha -->


## Algorithm 


## Use Case
