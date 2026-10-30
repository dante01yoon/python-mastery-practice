import os
import json
def total(prices:list[int])->int:
    result=0
    for p in prices :
        result+=p
    return result
print( total([1000,2500 ,300]) )
