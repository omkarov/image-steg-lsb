from stegapy import create_image
from stegapy import decode_image
import tkinter
from tkinter import filedialog
from tkfilebrowser import askopendirname, askopenfilename, asksaveasfilename
msg=''


def encode_enc(msg):

    s2=tkinter.Tk()
    name=askopenfilename()
    print(name)
    global newimg
    if len(msg)==0:
        s9 = tkinter.Tk()
        label9 = tkinter.Label(s9, text='Data is empty', padx=200, pady=10,bg='black', fg='white')
        label9.grid(row=1, column=0)

        def restart():
            s9.destroy()
            s = tkinter.Tk()

            label2 = tkinter.Label(s, text='STEGANOGRAPHY Using LSB', padx=200, pady=5)
            label2.grid(row=0, column=0)

            button2 = tkinter.Button(s, text='Encode', command=encode2, padx=200, pady=5, bg='black', fg='white')
            button2.grid(row=1, column=0, padx=25, pady=25)

            button2 = tkinter.Button(s, text='Decode', command=decode2, padx=200, pady=5, bg='black', fg='white')
            button2.grid(row=2, column=0, padx=25, pady=25)
        button10 = tkinter.Button(s9, text='Retry', command=restart, padx=200, pady=5, bg='black', fg='white')
        button10.grid(row=3, column=0, padx=25, pady=25)
        raise ValueError('Data is empty')
    def call2():
        location=filedialog.askdirectory()
        print(location)
        location+='/'
        create_image(msg, name,location + 'secret-image.png')

        # decoded = decode_image('secret-image.png')
        # print(decoded)
        s2.destroy()
        s3=tkinter.Tk()
        label5=tkinter.Label(s3,text='Data Encoded',padx=10,pady=10)
        label5.grid(row=0,column=1)
        button8 = tkinter.Button(s3, text='Decode', pady=10, command=decode2, padx=10,bg='black', fg='white')
        button8.grid(row=3, column=1, pady=10, padx=10)
        button4=tkinter.Button(s3,text='Quit',pady=10,padx=10,command=s3.destroy,bg='black', fg='white')
        button4.grid(row=2,column=1,pady=10,padx=10)
        s3.mainloop()

    s2 = tkinter.Tk()
    button3=tkinter.Button(s2,text='Save as new file',pady=10,command=call2,padx=10,bg='black', fg='white')
    button3.grid(row=0,column=1,padx=200,pady=200)

    s2.mainloop()


def encode():#To encode the data
    s.destroy()
    s1=tkinter.Tk()

    label2=tkinter.Label(s1,text='Steganography',padx=200,pady=15)
    label2.grid(row=0,column=0)
    global entry1
    entry1=tkinter.Entry(s1)
    entry1.grid(row=1,column=0,padx=10,pady=15)

    def call():#To call encode_enc
        msg=entry1.get()
        s1.destroy()
        encode_enc(msg)
    button1=tkinter.Button(s1,text='Enter data',padx=25,pady=5,command=call,bg='black', fg='white')
    button1.grid(row=2,column=0)
    s1.mainloop()

def encode2():#To encode the data
    s1=tkinter.Tk()

    label2=tkinter.Label(s1,text='Steganography',padx=200,pady=15)
    label2.grid(row=0,column=0)
    global entry1
    entry1=tkinter.Entry(s1)
    entry1.grid(row=1,column=0,padx=10,pady=15)

    def call():#To call encode_enc
        msg=entry1.get()
        s1.destroy()
        encode_enc(msg)
    button1=tkinter.Button(s1,text='Enter data',padx=25,pady=5,command=call,bg='black', fg='white')
    button1.grid(row=2,column=0)
    s1.mainloop()


def decode():#To decode the data in the image.
    s.destroy()
    s1=tkinter.Tk()
    sloc=str(askopenfilename())
    print('sloc' + sloc)
    decoded= decode_image(sloc)
    print(decoded)
    label2=tkinter.Label(s1,text='Secret Code:\n'+str(decoded),padx=200,pady=200,bg='black', fg='white')
    label2.grid(row=0,column=1)
    s1.mainloop()

def decode2():#To decode the data in the image.
    s1=tkinter.Tk()
    sloc=str(askopenfilename())
    print('sloc' + sloc)
    decoded= decode_image(sloc)
    print(decoded)
    label2=tkinter.Label(s1,text='Secret Code:\n'+str(decoded),padx=200,pady=200,bg='black', fg='white')
    label2.grid(row=0,column=1)
    s1.mainloop()


s=tkinter.Tk()

label2=tkinter.Label(s,text='STEGANOGRAPHY Using LSB',padx=200, pady=5)
label2.grid(row=0,column=0)

button2=tkinter.Button(s,text='Encode',command=encode,padx=200,pady=5,bg='black', fg='white')
button2.grid(row=1,column=0,padx=25,pady=25)

button2=tkinter.Button(s,text='Decode',command=decode,padx=200,pady=5,bg='black', fg='white')
button2.grid(row=2,column=0,padx=25,pady=25)
s.mainloop()

