#python script to check string is palindrome or not
s=input("Enter any String :")
y=s[::-1]
if(s==y):
    print("String is Palindrome.")
else:
    print("String is Not Palindrome.")
