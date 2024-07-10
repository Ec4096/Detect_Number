# # -*- coding: utf-8 -*-
# print("hello Ec4096")

# m = 'test'

# a = 5
# b = 6

# # print("a + b = ",a+b)
# # print(a/b)
# # print(a%b)
# # print(a//b)

# s = 'Hello world!'
# s = s.replace('o','o'.upper())

# a = 5;
# b = 10;

# print('a upper b') if a>b else print('a lower-equal b')

# print("a    b")
# print("a\nb")
# print(len("a\tb"))

# res = input()
# print("end:" + res)

# for i in range(3):
#     print(i)











# dictA = {"name":"Tome"}
# dictB = dictA.copy()
# print(dictA)
# print(dictB)

# delete_item = "name"
# dictA.pop(delete_item)
# print(dictA)
# print(dictB)

# del dictB['name']
# print(dictA)
# print(dictB)


# sum = lambda a:a+10
# print(sum(5))

# def my_function(a):
#     print(a)

# data = [1,2,3,4]

# data2 = list(map(my_function,data))
# #print(data2)




# data = list(x**2 for x in range(10))
# print(data)

# data2 = list(map(lambda x:x**2,range(10)))
# print(data2)


# data = list(2**x for x in range(32) )
# print(data)

# if 1 in data:
#     print("True")


# def climbStairs(n: int) -> int:
#         a,b,ans = 0,1,1
#         for i in range(1,n+1):
#             a,b,ans = b+ans,a,a+b
#         return ans


# num = climbStairs(3)
# print(num)

# def toHex(num: int) -> str:
#         ans = ""
#         assit = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
#         if num<0:
#               num = 2**32+num
#         while num!=0:
#             num0 = (int)(num%16)
#             ans+=assit[num0]
#             num //=16
#         return ans[::-1]

# ans = toHex(-1)
# print(ans)

# def bitwiseComplement( n: int) -> int:
#         ans = []
#         while n!=0:
#             n0 = n%2
#             ans+=str(n0)
#             n = n//2
#         # ans = ans[::-1]
#         cout = 0
#         for i in range(len(ans)):
#             if ans[i] =='0':
#                 cout+=2**i
#             else:
#                 pass
#         return cout

# print(bitwiseComplement(5))

# c = "A"
# num = ord(c)
# print(num)

# def longestCommonPrefix(strs: list[str]) -> str:
#         flag = []
#         min_num = 200
#         for i in range(len(strs)):
#             min_num = min(min_num,len(strs[i]))

#         for i in range(min_num):
#             flag.append(True)

#         for i in range(min_num):
#             c = strs[0][i]
#             for j in range(1,len(strs)):
#                 if c in strs[j][i:]:
#                     if not flag[j]:
#                         continue
#                 else:
#                     flag[i] = False
#         ans = ""

#         for i in range(len(flag)):
#             if flag[i]:
#                 ans+=strs[0][i]
#             else:
#                 break
#         print(flag)
#         return ans

# s1 = ["aa","ab"]
# ans = longestCommonPrefix(s1)

# print(s1)

# def divide(dividend: int, divisor: int) -> int:
#         ans = 0
#         d0 = abs(dividend)
#         d1 = abs(divisor)
#         flag = False
#         while d0>=d1:
#             ans+=1
#             d0-=d1
#             flag = True

#         if (dividend>0 and divisor<0)or(dividend<0 and divisor>0):
#             ans = -ans
#         print(flag)

#         return ans

# ans = divide(-1,1)
# print(ans)

# def generateParenthesis(n: int) -> list[str]:
#         ans = []
#         def backtrack(S, left, right):
#             if len(S) == 2 * n:
#                 ans.append(''.join(S))
#                 return
#             if left < n:
#                 S.append('(')
#                 backtrack(S, left+1, right)
#                 S.pop()
#             if right < left:
#                 S.append(')')
#                 backtrack(S, left, right+1)
#                 S.pop()

#         backtrack([], 0, 0)
#         return ans

# s = generateParenthesis(3)
# print(s)

# def countPrimes(n: int) -> int:
#         if n==0 or n==1 or n==2:
#             return 0
#         if n==2:
#             return 1
#         ans = []

#         def is_prime(x:int):
#             if x<4: return True
#             for i in range(2,int(x*0.5)+1):
#                 if(x%i==0):
#                     return False
#             return True

#         for i in range(2,n):
#             if(is_prime(i)):
#                 ans.append(i)
#         return len(ans)
            

# ans = countPrimes(499979)
# print(ans)
# n = 10
# is_prime = [True]*n
# print(is_prime)

# def countPrimes(n: int) -> int:
#         if n <= 2:
#             return 0
        
#         # 使用数组记录是否为质数，默认全为 True
#         is_prime = [True] * n
#         is_prime[0] = is_prime[1] = False  # 0 和 1 不是质数
        
#         # 埃氏筛法，从小到大标记质数的倍数为非质数
#         for i in range(2, int(n ** 0.5) + 1):
#             if is_prime[i]:
#                 for j in range(2*i, n, i):
#                     is_prime[j] = False
        
#         # 统计质数的数量
#         count = sum(is_prime)
#         return count

# ans = countPrimes(10)

# a = 10
# b = 20
# print(sum(a,b))

d = {
            'I':1,
            'IV':3,
            'V':5,
            'IX':8,
            'X':10,
            'XL':30,
            'L':50,
            'XC':80,
            'C':100,
            'CD':300,
            'D':500,
            'CM':800,
            'M':1000,
        }

print(d.get('CD'))