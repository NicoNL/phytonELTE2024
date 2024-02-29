word = input("Enter the correct word: ")
while( word != "chupacabra"):
    word = input("Enter the correct word or you wont leave: ")
    if(word == "chupacabra"):
       print("You've succesfully scaped from the loop")
       break
    