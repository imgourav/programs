            # Palindrome Program for Numbers as Input
    
num=int(input("Enter a number: "))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")
    
            # Palindrome Program for String as Input
        
string=input("Enter the String: ")
reverse=string[::-1]
if string==reverse:
    print("String is Palindrome")
else:
    print("String is not Palindrome")
