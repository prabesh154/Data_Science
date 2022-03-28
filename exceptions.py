
x=input("Enter a number ")
y=input("Enter the another number ")
try:
  z=int(x)/int(y)
except ZeroDivisionError as e:
     print("Exception Occured :",e)
     z=None
# except Exception as e:
#      print("Exception Type:",type(e).__name__)
#      z=None

except TypeError as e:
     print("Exception Occured :",e)
     z=None

print("Division is :",z)