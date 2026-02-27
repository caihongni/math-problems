"""給定一個正整數n,找出加總為n的最小平方整數數量。
舉例來説，給定n=13，回傳2，因爲13=3^2+2^2=9+4。
給定n=27,回傳3，因爲27=3^2+3^2+3^2=9+9+9。"""

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
def count_oddprime_factors(odd_part):
    factors = []
    d = 3  # 最小的奇素数
    while d * d <= odd_part:
        while odd_part % d == 0:
            factors.append(d)
            odd_part //= d
        d+=2
    
    # 如果最后的odd_part大于1，则odd_part本身也是一个质因子
    if odd_part > 1:
        factors.append(odd_part)
        
        #獲得一個正整數中4k+3型素數的個數
    lis=[x for x in factors if x%4==3]
    return len(lis)
#二平方和定理：如果一個正整數的素因數分解，如果4k+3型的素數的個數為奇數，則無法分解成兩個平方數之和
def two_square_sum(odd_part):  
    
    l=count_oddprime_factors(odd_part)
    if l % 2==0:
        return 2
    else:
        return 3

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
        if two_square_sum(odd_part)!=2:
            n+=1
            if three_square_sum(odd_part,k)!=3:
                n+=1
    
    print(f'正整數{num}的最小平方整數數量為{n}')
if __name__=="__main__":
    main()
    


