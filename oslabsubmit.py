# Step 1: Create input files
def create_input_files():
    files_content = {
        'file1.txt': "ADD a b AddResult\nSUR c d SubResult",
        'file2.txt': "XUL e f NullResult\nDIV g h DivResult\nXOD i j NoResult",
        'file3.txt': "DIV c d DivResult\nXUL e f NullResult\nSUR g h SubResult",
        'file4.txt': "ADD i j SumResult\nSUR b a SubResult\nXUL c d NullResult\nDIV e f DivResult",
        'file5.txt': "ADD AddResult 1000 %uResult"
    }

    for filename, content in files_content.items():
        with open(filename, 'w') as f:
            f.write(content)


create_input_files()


# Step 2: Process arithmetic operations
def process_operation(op, var1, var2, result_var, context):
    if var1 not in context:
        context[var1] = int(var1) if var1.isdigit() or (var1[0] == '-' and var1[1:].isdigit()) else 0

    if var2 not in context:
        context[var2] = int(var2) if var2.isdigit() or (var2[0] == '-' and var2[1:].isdigit()) else 0

    # Perform the operation
    if op == 'ADD':
        context[result_var] = context[var1] + context[var2]
    elif op == 'SUR':
        context[result_var] = context[var1] - context[var2]
    elif op == 'DIV':
        try:
            context[result_var] = context[var1] / context[var2]
        except ZeroDivisionError:
            context[result_var] = float('inf')
    elif op == 'XUL':
        context[result_var] = None
    elif op == 'XOD':
        context[result_var] = "No operation"
    else:
        context[result_var] = f"Unknown operation: {op}"


# Step 3: Process files sequentially (no threading)
import time
from collections import defaultdict


def without_threading():
    print("\nwithout threading:")
    context = defaultdict(int)
    start_time = time.time()

    for i in range(1, 6):
        filename = f'file{i}.txt'
        with open(filename, 'r') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) >= 4:
                    op, var1, var2, result_var = parts[:4]
                    process_operation(op, var1, var2, result_var, context)
                    print(f"Processed {op} in {filename}: {var1}, {var2} → {result_var} = {context[result_var]}")
                time.sleep(0.1)

    end_time = time.time()
    print(f"\nFinal context: {dict(context)}")
    print(f"Total time without threading: {end_time - start_time:.4f} seconds")


without_threading()

# Step 4: Process files with threading
import threading


def threaded_process_file(filename, context, lock):
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 4:
                op, var1, var2, result_var = parts[:4]
                with lock:
                    process_operation(op, var1, var2, result_var, context)
                    print(
                        f"Thread {threading.current_thread().name} processed {op} in {filename}: {var1}, {var2} → {result_var} = {context[result_var]}")
            time.sleep(0.1)


def with_threading():
    print("\nRunning with threading:")
    context = defaultdict(int)
    lock = threading.Lock()
    threads = []
    start_time = time.time()

    for i in range(1, 6):
        filename = f'file{i}.txt'
        thread = threading.Thread(
            target=threaded_process_file,
            args=(filename, context, lock),
            name=f"Thread-{i}"
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"\nFinal context: {dict(context)}")
    print(f"Total time with threading: {end_time - start_time:.4f} seconds")
with_threading()

