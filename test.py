suspects = ['A','B','C','D']
for x in suspects:
    if(x!='A')+(x=='C')+(x=='D')+(x!='D')==3:
        print('The theif is: ',x)
        break