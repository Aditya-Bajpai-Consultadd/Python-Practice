#Write a decorator to log the execution time of a function that
#processes large datasets.


import time

def log_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time is {end-start} seconds")
        return result
    return wrapper

@log_time
def process_data(data):
    for i in range(1000000):
        data.append(i)
    return data

if __name__ == "__main__":
    data = []
    data = process_data(data)
    
