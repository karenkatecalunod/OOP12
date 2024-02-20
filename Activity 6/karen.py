record={}

def add_record():
    key = input("Enter key: ")
    value = input("Enter value:")
    record[key] = value

def delete_record(key):
    key = input("Enter the key:")
    if key in record:
        del record [key]
        print("Record")
        print(record)
        print("Deleted")
        return True

def display_record():
    while True: key = input("")
       "choice" =\
         input( "enter,add,data,D")
    if "choice" == "add data":
          add_record()
   elif "choice" =="deleete"
          delete_record()
   elif "choice" == "delete record"
         delete_record()
   elif "choice" == "end":
        print("THANK YOU")
   elif:
     print("Invalid entyry")

   if__ name __ == "__main__":



