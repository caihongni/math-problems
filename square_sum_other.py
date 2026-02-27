def even_to_odd(num):  #判斷一個正整數是否為偶數，如果為偶數，化偶數為奇數
    while True:
        k=0
        if num%4==0:
            num=num//4
        elif num%4==2:
            num=num//2
            k=1
        else:
            break
    return num,k
def is_square(num):
    i=1
    while i*i<num:
        i+=1
    if num-i*i==0:
        return 1
    else:
        return 2

def two_square_sum(num):
    i=1
    m=2
    while i*i<num:
        var=num-i*i
        if is_square(var)==1:
             break
        else:
            i+=1
    if is_square(var)!=1:
        m+=1
    return m

def three_square_sum(odd_part,k):
    if k==0 and odd_part % 8==7:
        return 4
    else:
        return 3


def main():
    while True:
        try:
            num=int(input("請輸入一個正整數:"))
            if num<=0:
                raise Exception("輸入不能為負數或零")
        except ValueError as e:
            print("請輸入一個有效數字")
        except Exception as e:
            print(f'發生異常:{e}')
        else:
            break
    
    
   #根據四平方和定理，任何一個正整數都可以分解成四個平方整數之和
    n=1
    if is_square(num)!=1:
        odd_part,k =even_to_odd(num)
        n+=1
        if two_square_sum(num)!=2:
            n+=1
            if three_square_sum(odd_part,k)!=3:
                n+=1
    
    print(f'正整數{num}的最小平方整數數量為{n}')
if __name__=="__main__":
    main()
    


