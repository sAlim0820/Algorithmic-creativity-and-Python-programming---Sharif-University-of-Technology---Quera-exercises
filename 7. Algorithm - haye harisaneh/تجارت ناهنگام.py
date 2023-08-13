try:
    n = list(input().split())
    working = 0
    now_num = 0
    copy_n = n.copy()
    
    index_number = []
    
    for working in copy_n:
        working = int(working)
        if working >= now_num + 3 :
            now_num = working
            index_number.append((n.index(str(working)))+1)
    
    for i in index_number:
        print(i,end=" ")

     
    
        
except:
    pass
    