def recursion (k):
    if(k>0):
        result=k+recursion(k-1)
        print(result)
    else:
        return 0
    return result
print("Recursion Example Result")
recursion ( 3 )
