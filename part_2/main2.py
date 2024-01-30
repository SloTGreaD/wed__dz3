import time
from multiprocessing import Pool, cpu_count

def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def factorize_list_parallel(numbers, processes=None):
    if processes is None:
        processes = cpu_count()

    with Pool(processes) as pool:
        start_time = time.time()
        result = pool.map(factorize, numbers)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Parallel factorization took {elapsed_time:.4f} seconds using {processes} processes")
    return result

# Test:
if __name__ == '__main__':
    test_numbers = [128, 255, 99999, 10651060]
    expected_results = [
        [1, 2, 4, 8, 16, 32, 64, 128],
        [1, 3, 5, 15, 17, 51, 85, 255],
        [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999],
        [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    ]

    result_parallel = factorize_list_parallel(test_numbers)

    # Check the test:
    for i in range(len(test_numbers)):
        assert result_parallel[i] == expected_results[i]

    print("Test successful!")

