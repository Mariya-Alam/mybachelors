class Process:
    def __init__(self,operations,process_id):
        self.operations = operations
        self.process_id = process_id

    def execute(self):
        for operation in self.operations:
            op_name,arg1,arg2 = operation
            print(f"Process{self.process_id}:performing{op_name} with arguments{arg1} and{arg2}")
            self.execute_operation(op_name,arg1,arg2)

    def execute_operation(self,operation,arg1,arg2):
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

Process_1_operatons = [
    ("ADD",5,3),
    ("SUB",10,4)
]
Process_2_operatons = [
    ("MUL",6,7),
    ("DIV",20,5),
    ("MOD",9,4)
]
process_1 = Process(Process_1_operatons,"1")
process_2 = Process(Process_2_operatons,"2")

process_1.execute()
process_2.execute()