#write a script to enter any sentence and print those word which is palindrome also print total number of palindrome word.
def paliwordcount(s):
    p=s.split(" ")
    q=0
    r=[]
    for i in p:
        if (i==i[::-1]):
            q=q+1
            r.append(i)
    if q>0:
        print(" Palindrome Word In Sentence Is {q} And Palindrome Words Are:{r}.")              
    else:
        print(" No Palindrome Word in Sentence!!!")    
s=input("enter a sentece:")
paliwordcount(s)
