def main():

    n = 2
    arr = [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]

    dynamicArray(n, arr)


def dynamicArray(n, queries):
    #
    # Write your code here.
    #
    final_arr = []
    for i in range(n):
        final_arr.append([])

    last_answer = 0

    for query in queries:
        query_type = query[0]
        x = query[1]
        y = query[2]
        index = (x^last_answer)%n
        if query_type == 1:
            final_arr[index].append(y)
        elif query_type == 2:
            inside_index = y%len(final_arr[index])
            last_answer = final_arr[index][inside_index]
            print (last_answer)



if __name__ == "__main__":
    main()