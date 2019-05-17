# pwnable.tw_AliveNote  

death_note와 유사한 alpha_numeric shellcode 문제!!  
하지만 특수문자 없이, 알파벳과 숫자, 띄어쓰기만 가능하다.  
따라서, death_note에서는 /bin/sh를 인자로 넣어줄 수 있었지만, 여기서는 /도 만들어주어야 한다.  

alpha_numeric shellcode에서 항상 문제는 int 0x80! 노가다...  
입력 주고 받고가 너무 많으면 서버에서 오류가 난다!!  

sol.py, sol2.py모두 로컬에서는 됐지만, 서버에서는 sol2.py만 됐다.  
sol2.py도 됐다가 안됐다가 하는데, 운이 좋았던걸로...!  
