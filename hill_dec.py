# Import Numpy for Matrix Vector Multiplication

import numpy as np

# Define a function to get the key from the alphabet dictionary using values

def get_key(val):
    for key, value in alphabet.items():
         if val == value:
             return key
 
    return "key doesn't exist"

# Define the Alphabet

alphabet = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9," ": 10,"A": 11,"B": 12,"C": 13,"D": 14,"E": 15,"F": 16,"G": 17,"H": 18,"I": 19,"J": 20,"K": 21,"L": 22,"M": 23,"N": 24,"O": 25,"P": 26,"Q": 27,"R": 28,"S": 29,"T": 30,"U": 31,"V": 32,"W": 33,"X": 34,"Y": 35,"Z": 36,",":37,r"'": 38,"." : 39,"!" : 40,"?" : 41,"*":42,r'"':43,"a":44,"b":45,"c":46,"d":47,"e":48,"f":49,"g":50,"h":51,"i":52,"j":53,"k":54,"l":55,"m":56,"n":57,"o":58,"p":59,"q":60,"r":61,"s":62,"t":63,"u":64,"v":65,"w":66,"x":67,"y":68,"z":69,"-":70,";":71,"\n":72}

# Define the Decryption Key as the Inverse of Encryption Key in mod 73

decryption_key = np.array([[29,58,13,61],
                                            [20,36,67,71],
                                            [58,0,28,32],
                                            [39,38,26,40]])

# Open the Encrypted File

f = open(r"C:\Users\Abhay Jha\Desktop\Decryption\file.txt", "r")

# Create a new File called Decrypted File

decrypted_file = open(r"C:\Users\Abhay Jha\Desktop\Decryption\decrypted_file.txt", "w")

# Read the whole encrypted file as a string

file_string = f.read()

# Create Vectors of Length 4x1, decrypt and write into a new file

for i in range(0,len(file_string), 4):

    # Make 4x1 vectors

    vector = np.array([alphabet[file_string[i]],
                alphabet[file_string[i+1]],
                alphabet[file_string[i+2]],
                alphabet[file_string[i+3]]])

    # Multiply the 4x1 vectors with the decryption key and write in the new file

    decrypted_file.write(get_key((decryption_key.dot(vector)%73)[0]) + get_key((decryption_key.dot(vector)%73)[1]) + get_key((decryption_key.dot(vector)%73)[2]) + get_key((decryption_key.dot(vector)%73)[3]))