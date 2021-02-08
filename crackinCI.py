# determine isf string has all unique characters 

# def char_frequency(str1):
#     dict = {}
#     for n in str1:
#         keys = dict.keys()
#         if n in keys:
#             dict[n] += 1
#         else:
#             dict[n] = 1
#     return dict
# print(char_frequency('google'))

# given two strings write method to check i 1 is permutation of another 

#if they are inpermutation with each other then their sum will be same others sam and their multiplication will also be sam,e 

def permutation (arr1,arr2):
    sum1=sum2=0
    mul1=mul2=1
    for i in range(len(arr1)):
        sum1+= arr1[i]
        mul1*=arr1[i]

    for i in range(len(arr2)):
        sum2+=arr2[i]
        mul2*=arr2[i]

    if sum1==sum2 and mul1==mul2:
        return True 
    else:
        return False
print(permutation([2,3,4,5],[5,4,3,1]))
