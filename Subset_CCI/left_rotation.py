def main():
    left_rotation(3, [1,2,3,4,5])

def left_rotation(d, arr):
    size = len(arr)
    n = d%size
    back = arr[n:]
    front = arr[:n]

    arr[:n] = back
    arr[(size-n):] = front

    print (" ".join(str(x) for x in arr))
    return arr

if __name__ == "__main__":
    main()