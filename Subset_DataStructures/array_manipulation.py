def main():
    arrayManipulation(5, [[1,2,100], [2,5,100], [3,4,100]])

def arrayManipulation(n, queries):
    arr = [0] * n

    for query in queries:
        i = query[0]-1
        j = query[1]

        add_sum = query[2]

        arr[i] += add_sum
        if (j <len(arr)):
            arr[j] -= add_sum

    print (arr)
    max = res = 0
    for num in arr:
        res = res+num
        if (max<res): max=res

    print (max)
    return max


if __name__ == "__main__":
    main()

