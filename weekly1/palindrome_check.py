def is_palindrome(s):
    kept1=[]
    kept2=[]
    num=0
    count=0
    for i in s:
        num+=1
    for i in s:
        if num%2==0 and count<num/2:
            kept1.append(i)
            count+=1
        elif num%2==0 and count>=num/2:
            kept2.append(i)
            count+=1
        elif num%2==1 and count<=(num-1)/2:
            kept1.append(i)
            count+=1
        elif num%2==1 and count>=(num-1)/2:
            kept2.append(i)
            count+=1
    return ''.join(kept1) == ''.join(kept2)
word1 = "level"
word2 = "python"
word3 = "radar"

print(is_palindrome(word1))  # Expected output: True
print(is_palindrome(word2))  # Expected output: False
print(is_palindrome(word3))  # Expected output: True
