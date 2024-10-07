import numpy as np

def main():
    # Task 1
    numpy_array = np.array(range(1, 31))
    print(numpy_array, numpy_array.shape)
    print('index10: ', numpy_array[10])

    # Task 2
    numpy_array = numpy_array.reshape(6, 5)
    print(numpy_array)
    print('index[3, 4]: ', numpy_array[3, 4])

    # Task 3
    extracted_array = numpy_array[3]
    print(extracted_array)
    extracted_array = numpy_array[:2, 2:]
    print(extracted_array)

    # Task 4
    numpy_array = np.random.randint(10, 100, 15)
    print(numpy_array)
    print('max: ', np.max(numpy_array))
    print('min: ', np.min(numpy_array))

    # Task 5
    numpy_array = np.random.randint(0, 50, (4, 4))
    print(numpy_array)
    print('sum: ', np.sum(numpy_array))

    # Task 6
    numpy_array = np.random.randint(1, 20, (5, 5))
    print(numpy_array)
    numpy_array[1, :] = 0
    print(numpy_array)
    numpy_array[numpy_array>=10] = 99
    print(numpy_array)

    # Task 7
    numpy_array = np.random.randint(1, 10, 5)
    numpy_array_2 = np.random.randint(1, 10, 5)
    print(numpy_array, numpy_array_2)
    print('add: ', numpy_array + numpy_array_2)
    print('sub: ', numpy_array - numpy_array_2)
    print('mul: ', numpy_array * numpy_array_2)

    # Task 8
    numpy_array = np.array([2, 4, 6, 8])
    numpy_array_2 = np.random.randint(1, 5, (3, 4))
    print(numpy_array, '\n', numpy_array_2)
    print(numpy_array_2+numpy_array)

    # Task 9
    numpy_array = np.random.randint(1, 100, 20)
    print(numpy_array[numpy_array>=50])
    numpy_array[numpy_array<=30] = -1
    print(numpy_array)

    # Task 10
    numpy_array = np.random.randint(1, 50, 12)
    numpy_array = numpy_array.reshape(3, 4)
    print('Original array:\n', numpy_array)
    print('Transposed array:\n', numpy_array.T)

if __name__ == '__main__':
    main()