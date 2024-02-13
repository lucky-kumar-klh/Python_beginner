def even_numbers(limit):
    for i in range(2, limit+1, 2):
        # return i
        yield i    # yield not only returns value, but keeps the previous data in memory
                   # Whereas, once return's task is over, it will remove the value from memory 
    
for i in even_numbers(10):
    print(i)