import pywhatkit as kt
import getpass as gp

print("We the lazy people are even automating the whatsapp now :)")

try : 

    # Here getpass module will provide a security to "phone numbers"
    # getpass() will 'encrypt' the phone number and hides it in the command line
    
    phone_num = gp.getpass(prompt= "Enter your phone number :", stream = None)

    # This string will hold the text which needs to be send to recipent
    msg = "Hey ! I'm sending you this message using Python !"

    # Here comes the main part of code :
    # sendwhatmsg() will hold the ph number , messages, 'hour' part of time , 'minutes' part of time
    kt.sendwhatmsg(phone_num, msg, 7, 4)

except :
    print("An unexpected error occured")
