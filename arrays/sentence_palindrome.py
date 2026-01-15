def is_palindrome(s):
    l=0
    r = len(s)-1
    while l<r:
        if not s[l].isalnum():
            l+=1
        elif not s[r].isalnum():
            r-=1
        else:
            if s[l].lower()==s[r].lower():
                l+=1
                r-=1
            else:
            
                return False
    return True
a= "Too hot to hoot" 
if is_palindrome(a):
    print("Is a palindrome")
else:
    print("Not a palindrome")                       