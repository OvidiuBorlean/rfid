import time
import sys

card = '0019171125'        # Stored good card number consider using a list or a file.
def main():                # define a main function.
  while True:                # loop until the program encounters an error.
    sys.stdin = open('/dev/hidraw0', 'r')
    RFID_input = input()            
    if RFID_input == card:      # coppare the stored number to the input and if True execute code.
         print "Access Granted" 
         print "Read code from RFID reader:{0}".format(RFID_input)
    else:                    # and if the condition is false excecute this code.
         print "Access Denied"
         tty.close()
main()                 
