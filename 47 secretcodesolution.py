uinp= input("Enter your message: ")
words = uinp.split(" ")
coding = int(input("1 for coding and 0 for decoding "))
coding == True if (coding ==1)else False   #bracket after ifimportant
if (coding):
 fword = []
 for word in words :
    if (len(word)>=3): 
        r1 = "dka"
        r2 =   "fjt"
        nword = r1 +  word[1:] + word[0]   + r2
        fword.append(nword)
    else :
       fword.append(word[::-1])     
 print(" ".join(fword)) # to join a lsit in a string
else:
   fword = []
   for word in words :
    if (len(word)>=3): 
        nword= word[3:-3]
        nword= nword[-1]+nword[:-1]         
        fword.append(nword)
    else :
       fword.append(word[::-1])     
print(" ".join(fword)) 
