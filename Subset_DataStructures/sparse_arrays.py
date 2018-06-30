def main():
    pass

def matchingStrings(strings, queries):
    d = {}
    res = []
    for s in strings:
        if s in d.keys():
            d[s] += 1
        else:
            d[s] = 1

    for query in queries:
        if query not in d.keys():
            res.append(0)
        else:
            res.append(d[query])

    for r in res:
        print (r)

    return res

if __name__ == "__main__":
    main()