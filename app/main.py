def cache(func):
    # Write your code here
    cache_dict = {}  # Словник для зберігання результатів

    def wrapper(*args):
        if args in cache_dict:
            print("Getting from cache")
            return cache_dict[args]
        else:
            result = func(*args)
            cache_dict[args] = result
            print("Calculating new result")
            return result

    return wrapper
