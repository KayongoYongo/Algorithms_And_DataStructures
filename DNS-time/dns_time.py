def getMinTime(cache_size, cache_time, server_time, urls):
    current_cache = []
    time_taken = []

    for url in urls:
        if len(current_cache) < cache_size:
            current_cache.append(url)
            if url in current_cache:
                time_taken.append(cache_time)
            else:
                time_taken.append(server_time)
            print(current_cache)
            print(time_taken)
        else:
            current_cache.pop(0)
            current_cache.append(url)
            print(current_cache)
    
    return time_taken

cache_size = 3
cache_time = 2
server_time = 5
urls = [
    "http://www.hackerrank.com",
    "http://www.google.com",
    "http://www.yahoo.com",
    "http://www.gmail.com",
    "http://www.yahoo.com",
    "http://www.hackerrank.com",
    "http://www.gmail.com"
]

print(f'The time taken is {getMinTime(cache_size, cache_time, server_time, urls)}')