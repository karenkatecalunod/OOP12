dict = []
print("please select the following")

for i in iter(int,1):
   dict.append(i)
   c = input("Enter your choice")
   if (c == "a") :
     key = input("Enter")
     value = input("Enter")


   print("Record Deleted successfully.'")
else:
  print("invalid choice")

record_keeper= input()
dict = {}
while True:
  print("a. Add Data")
  print("b. Delete Data")
  print("c. End")

a, b, c = record_keeper

if a== a:
  key =input("Enter the key:")
  value = input("Enter the value")
  record_keeper = input("")
  record_keeper = view_Data(key)

elif b == b:
  key = input("Enter the")
  value = input("Enter the key")
  record_keeper = input("")
  record_keeper = view_Data()

elif c == c:
  print("THANK YOU")
else:
  print("invalid choice")

