#Generate Authentication TOTP

import hmac
import hashlib
import time
import struct



sharedsecret="amit@puttingbugsincode"
DIGIT=10
X=30 # Time Step given by question
T0=0

def dynamic_truncation(HS):
  # offsetBits = last 4 bits of HS.
  # HS is passed in hex. So convert accordingly
  offsetBits=HS[-1:]
  offset = int(offsetBits,16)
  # P = HS[offset]...HS[offset+3]
  P=HS[offset*2:offset*2+8]
  # Last 31 digits of P
  binary_P=int(P,16) & 0x7FFFFFFF
  #return last 31 digits of P
  #return P[-31:]
  return str(binary_P)

def truncate(HS):
  Sbits= dynamic_truncation(HS) # DT returns a 31 bit string
  #Snum=int(Sbits,2) #convert bit to an integer in the range 0 to 2^{31}-1
  #D= int(Sbits) % (10**DIGIT) # D will be Digit-digits number
  #return D
  return Sbits[-DIGIT:]

def HOTP(K,T):
  #HS=HMAC-SHA-512(K,T)
  t_byte=struct.pack(">Q", T)
  h=hmac.new(K.encode(),t_byte,hashlib.sha512).hexdigest()
  HOTP=truncate(h)
  return HOTP

def TOTP():
  K=sharedsecret
  currentTime=int(time.time())
  T=(currentTime-T0) // X
  print("The TOTP is {}".format(HOTP(K,T)))

if __name__=='__main__':
  TOTP()
