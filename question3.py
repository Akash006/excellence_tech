def max_con_one(data: list) -> int:
    if sum(data) == 0:
        return 0
    else:
        count = 0
        res = 1
        for i in range(len(data)):
            if( data[i] == 0):
                count = 0
            else:
                count += 1
                res = max(res, count)
    return res

if __name__ == '__main__':

    data = [0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1]

    result = max_con_one(data)
    print("Max occurance of 1 is : ", str(result))

    