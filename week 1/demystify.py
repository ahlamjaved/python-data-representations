def demystify(l1_string): 
    l1_string=l1_string.replace('l','a')
    l1_string=l1_string.replace('1','b')
    return l1_string
   
print(demystify("lll111l1l1l1111lll"))
print(demystify("111l1l11l11lll1lll1lll11111ll11l1ll1l111"))
