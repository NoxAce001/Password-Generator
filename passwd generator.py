#Password generator

import random

while True:
    try:
        length=int(input("Enter the length of paasword:"))
        num=list("0124567893012456789306457893456789")
        spcl_chr=list("@#₹!&*€$@#₹!&*€#₹!&*€$@#₹!&*$π∆π∆")
        alphabets= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c','d', 'e','f','g', 'h', 'j','k', 'l', 'm', 'n', 'o', 'p', 'a', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        mix=100*(alphabets+num+spcl_chr+alphabets)	
        random.shuffle(mix)
        print("List form:",mix[0:length])
        print("You can try this:",''.join(mix[0:length]))
        print()
    except:
        print("Please enter a numeric value , e.g: 1,2,3,4.....etc")
        print()
