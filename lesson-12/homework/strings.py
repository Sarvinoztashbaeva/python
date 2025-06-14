import threading
from math import isqrt
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
def check_primes(start, end, result):
    local_primes = []
    for number in range(start, end):
        if is_prime(number):
            local_primes.append(number)
    result.extend(local_primes)
def find_primes_in_range(start, end, num_threads=4):
    threads = []
    result = []
    thread_results = [[] for _ in range(num_threads)]

    step = (end - start) // num_threads
    for i in range(num_threads):
        thread_start = start + i * step
        thread_end = end if i == num_threads - 1 else thread_start + step
        t = threading.Thread(target=check_primes, args=(thread_start, thread_end, thread_results[i]))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    for sublist in thread_results:
        result.extend(sublist)

    result.sort()
    return result
if __name__ == "__main__":
    start_range = 10
    end_range = 100
    num_threads = 4

    primes = find_primes_in_range(start_range, end_range, num_threads)
    print(f"Prime numbers between {start_range} and {end_range} are:\n{primes}")


import threading
from collections import Counter
import re
def count_words(lines, counter_list, index):
    word_counter = Counter()
    for line in lines:
        words = re.findall(r'\b\w+\b', line.lower())
        word_counter.update(words)
    counter_list[index] = word_counter
def threaded_word_count(filename, num_threads=4):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    total_lines = len(lines)
    step = total_lines // num_threads
    threads = []
    counters = [None] * num_threads
    for i in range(num_threads):
        start = i * step
        end = None if i == num_threads - 1 else (i + 1) * step
        t = threading.Thread(target=count_words, args=(lines[start:end], counters, i))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    total_counter = Counter()
    for c in counters:
        total_counter.update(c)

    return total_counter

if __name__ == "__main__":
    filename = "large_text.txt"# here will be actual file path
    word_counts = threaded_word_count(filename, num_threads=4)
