from tkinter import *
from itertools import cycle

pathToInputFile = "input\\input.txt"
pathToOutputFileEncrypt = "input\\outputEncrypt.txt"
pathToOutputFileDecrypt = "input\\outputDecrypt.txt"
processingText = "hello kdjfkjdkf"
alp = 'abcdefghijklmnopqrstuvwxyz'
key = 0


class Block:
    def __init__(self, master):
        self.e = Entry(master, width=20)
        self.bOne = Button(master, text="Encode")
        self.bTwo = Button(master, text="Decode")
        self.l = Label(master, bg='black', fg='white', width=20)
        self.e.pack()
        self.bOne.pack()
        self.bTwo.pack()
        self.l.pack()

    def setFuncOne(self, func):
        self.bOne['command'] = eval('self.' + func)

    def setFuncTwo(self, func):
        self.bTwo['command'] = eval('self.' + func)

    def encryptFileTxt(self):
        processingText = readTxtFile(pathToInputFile)
        key = self.e.get()

        key_encoded = encode_val(key)
        value_encoded = encode_val(processingText)

        shifre = full_encode(value_encoded, key_encoded)
        print('Шифр=', ''.join(decode_val(shifre)))
        writeToFile(pathToOutputFileEncrypt, ''.join(decode_val(shifre)))



    def decryptFileTxt(self):
        processingText = readTxtFile(pathToOutputFileEncrypt)
        key = self.e.get()

        key_encoded = encode_val(key)
        value_encoded = encode_val(processingText)

        decoded = full_decode(value_encoded, key_encoded)
        decode_word_list = decode_val(decoded)
        print('Word=', ''.join(decode_word_list))
        writeToFile(pathToOutputFileDecrypt, ''.join(decode_word_list))



def readTxtFile(pathToFile):
    fileTxt = open(pathToFile)
    textFromFile = fileTxt.read()
    fileTxt.close()
    return textFromFile


def writeToFile(pathToFile, text):
    fileTxt = open(pathToFile, "w+")
    fileTxt.write(text)
    fileTxt.close()

def form_dict():
    d = {}
    iter = 0
    for i in range(0,127):
        d[iter] = chr(i)
        iter = iter +1
    return d


def encode_val(word):
    list_code = []
    lent = len(word)
    d = form_dict()

    for w in range(lent):
        for value in d:
            if word[w] == d[value]:
               list_code.append(value)
    return list_code


def comparator(value, key):
    len_key = len(key)
    dic = {}
    iter = 0
    full = 0

    for i in value:
        dic[full] = [i,key[iter]]
        full = full + 1
        iter = iter +1
        if (iter >= len_key):
            iter = 0
    return dic

def full_encode(value, key):
    dic = comparator(value, key)
    print('Compare full encode', dic)
    lis = []
    d = form_dict()

    for v in dic:
        go = (dic[v][0]+dic[v][1]) % len(d)
        lis.append(go)
    return lis

def decode_val(list_in):
    list_code = []
    lent = len(list_in)
    d = form_dict()

    for i in range(lent):
        for value in d:
            if list_in[i] == value:
               list_code.append(d[value])
    return list_code

def full_decode(value, key):
    dic = comparator(value, key)
    print ('Deshifre=', dic)
    d = form_dict()
    lis =[]

    for v in dic:
        go = (dic[v][0]-dic[v][1]+len(d)) % len(d)
        lis.append(go)
    return lis


root = Tk()
root.geometry('400x250')
first_block = Block(root)
first_block.setFuncOne('encryptFileTxt')
first_block.setFuncTwo('decryptFileTxt')
root.mainloop()





