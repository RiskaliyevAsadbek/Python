# Homework:

# Exercise 1: Threaded Prime Number Checker

# Write a Python program that checks whether a given range of numbers contains prime numbers.
# Divide the range among multiple threads to parallelize the prime checking process.
# Each thread should be responsible for checking a subset of the range, and 
# the main program should print the list of prime numbers found.
import threading

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_in_range(start, end, result):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    result.extend(primes)
    print(f"Thread {threading.current_thread().name} found primes: {primes}")

def main():
    start_range = int(input("Enter start of range: "))
    end_range = int(input("Enter end of range: "))
    num_threads = int(input("Enter number of threads: "))

    step = (end_range - start_range + 1) // num_threads
    threads = []
    primes = []

    for i in range(num_threads):
        start = start_range + i * step
        end = start_range + (i + 1) * step - 1 if i < num_threads - 1 else end_range

        thread = threading.Thread(target=find_primes_in_range, args=(start, end, primes), name=f"T{i+1}")
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    primes.sort()
    print("\nAll prime numbers found:", primes)

main()

# Exercise 2: Threaded File Processing

# Write a program that reads a large text file containing lines of text.
# Implement a threaded solution to count the occurrence of each word in the file. 
# Each thread should process a portion of the file, and the main program should display a summary of word occurrences across all threads.
import threading
from collections import Counter

def count_words_in_lines(lines, result_list, index):
    word_count = Counter()
    for line in lines:
        words = line.strip().split()
        word_count.update(words)
    result_list[index] = word_count


def threaded_word_count(file_path, num_threads=4):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    total_lines = len(lines)
    chunk_size = total_lines // num_threads

    threads = []
    results = [None] * num_threads 

    for i in range(num_threads):
        start = i * chunk_size
        end = total_lines if i == num_threads - 1 else (i + 1) * chunk_size
        t = threading.Thread(target=count_words_in_lines,
                             args=(lines[start:end], results, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    final_count = Counter()
    for r in results:
        final_count.update(r)

    return final_count


if __name__ == "__main__":
    file_path = "large_text.txt"  
    word_counts = threaded_word_count(file_path, num_threads=4)

    print("Top 10 words:")
    for word, count in word_counts.most_common(10):
        print(f"{word}: {count}")
