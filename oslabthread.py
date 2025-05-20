import threading
import time

Process_1_operations = [
    ("ADD",5,3),
    ("SUB",10,4)
]
Process_2_operations = [
    ("MUL",6,7),
    ("DIV",20,5),
    ("MOD",9,4)
]


def execute_operation(operation,arg1,arg2):
        if operation == "ADD":
            result = arg1 + arg2
            print(f"AddResult :{result}")
        elif operation == "SUB":
            result = arg1 - arg2
            print(f"SubResult: {result}")
        elif operation == "MUL" :
            result = arg1 * arg2
            print(f"MulResult: {result}")
        elif operation == "DIV" :
            if arg2!= 0:
                result = arg1/arg2
                print(f"DivResult: {result}")
            else:
                print("error: Division by Zero")

        elif operation == "MOD":
            result = arg1 % arg2
            print(f"ModResult: {result}")
def process_operation(operations,process_id):
    for operation in operations:
        op_name,arg1,arg2 = operation
        print(f"Process{process_id}: Performing{op_name} with arguments{arg1} and {arg2}")
        execute_operation(op_name,arg1,arg2)
        time.sleep(1)

thread1 = threading.Thread(target = process_operation,args = (Process_1_operations,"1"))
thread2 = threading.Thread(target = process_operation,args = (Process_2_operations,"2"))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
