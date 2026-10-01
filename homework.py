class Daily_Message:
    def __init__(self):
        self.message=""
    def get_message(self):
        self.message=input("What's today's daily message?")
    def print_message(self):
        print("Message in upper",self.message.upper)
daily_text=Daily_Message()
daily_text.get_message()
daily_text.print_message()
class Helper_Session:
    def __init__(self):
        print("Daily Data helper session started")
    def __del__(self):
        print("Daily Data helper session ended")
def create_session():
    print("Creating Helper session")
    session=Helper_Session()
    print("Session is ready")
    return session
print("Calling create_session function")
session_object=create_session()
print("Program is running")
class Pair_Finder:
    def find_pairs(self,numbers,target):
     look={}


     for index, number in enumerate(numbers):
        needed_num=target-number

        if needed_num in look:
         return(look[needed_num],index)
         look[number]=index
     return None
numbers=(10,15,16,20,12)
target_value=(int(input("Enter target sum to search")))
result=Pair_Finder().find_pairs(numbers,target_value)
if result is not None:
   print("index1=%d,index2=%d" %result)
else:
   print("No matching pair found.")
del session_object
print("The session has concluded")