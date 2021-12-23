n = input('Enter any word of your choice: ')

dct1 = {}


def most_frequent(n):
    
    lst = list(n)

    for i in lst:
        if i in dct1:
            dct1[i]=dct1[i]+1
        else:
            dct1[i] = 1
     
    dct2 = sorted(dct1.items(), key=lambda x:x[1])
    sortdict = dict(dct2)
    print(sortdict)
             
        
most_frequent(n)
