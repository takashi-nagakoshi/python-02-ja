def mystery_function(lst):
    result = lst
    for i in range(len(lst)):
        # インデックスではなくリストの要素の偶奇をチェックする
        if lst[i] % 2 == 0:
            result[i] = lst[i] ** 2
    return result
    
lst= [1, 2, 3, 4, 5]
lst= [4, 1, 6, 2, 10]

def main():
    results = mystery_function(lst)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()