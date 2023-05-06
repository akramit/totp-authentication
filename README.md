# Time-Based One-Time Password Algorithm
Time-Based One-Time Password Algorithm or TOTP in short is a time based codes for single use, which is valid only for short duration of time, which protects against any kind of compromise due to short lived nature. This is often used in 2FA (2 Factor authentication) systems. 2FA provides an extra layer of security, by requiring two kind of passwords - something a user knows (like password) and something a user have (like phone to generate OTP). 

The TOTP value is calculated by both the authenticator and authenticatee. The verification is successful only if the provided value matches with the locally generated value. TOTP credentials are based on a shared secret key, and security can be compromised if someone steals the secret key. 

Here, I provide a simple implementation of TOTP in python which anyone can use for their own purpose (or better - write your own;). Below, I have explained the algorithm. 

TOTP is an extension of HOTP (HMAC based One-Time Password) and follows an open standard documented in [RFC6238](https://datatracker.ietf.org/doc/html/rfc6238). 

Authentication Apps supporting TOTP - *Authy, Google Authenticator*

<!-- Put image of Google Authenticator here. -->
<img src="/google_auth.png" width="100" height="100" > <img src="/zerodha2fa.png" width="100" height="100" >
<!-- Example of TOTP  by using Zerodha -->



## Algorithm 

T<sub>0</sub> = Unix time from which to start counting steps \
T<sub>X</sub> = Interval used to calculate counter (default is 30 seconds) \
C<sub>T</sub> = Number of durations T~X~ between T~0~ and T(current time) \
K = Secret key shared with both authenticator and authenticatee

C<sub>T</sub> = (T - T<sub>0</sub> )/T<sub>X</sub>

TOTP(K) = HOTP(K,C<sub>T</sub>)

HOTP(K,C<sub>T</sub>) : 
1. Step 1: Generate an HMAC-SHA-512 value. Let HS = HMAC-SHA-512(K,C)  // HSis a 20-byte string

  2.  Step 2: Generate a 4-byte string (Dynamic Truncation) \
   Let Sbits = DT(HS)   //  DT, defined below, returns a 31-bit string

  3.  Step 3: Compute an HOTP value
   Let Snum  = StToNum(Sbits)   // Convert S to a number in 0...2^{31}-1
   Return D = Snum mod 10^Digit //  D is a number in the range 0...10^{Digit}-1 \
Usually we have 6 digits OTP. So, we set D=6 in the above steps. We use HMAC-SHA-512 instead of HMAC-SHA-1 for added security. 
 

## References 
1. RFC6238 TOTP - https://datatracker.ietf.org/doc/html/rfc6238 
2. RFC4226 HOTP - https://datatracker.ietf.org/doc/html/rfc4226
3. Wikipedia - https://en.wikipedia.org/wiki/Time-based_one-time_password
