Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n=int(input("Enter size : "))
ar=[1,2,3,4,5,6]
evensum=0
oddsum=0
for i in range(n):
    if(ar[i]%2==0):
        evensum=evensum+ar[i]
    else:
        oddsum=oddsum+ar[i]
print(oddsum,evensum)
        