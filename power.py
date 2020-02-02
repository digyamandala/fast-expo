#return k^n
def powerRecursive(k, n):
   
   if(n == 0):
      return 1
   if(n == 1):
      return k
   if(n == -1):
      return 1/k

   if(n < 0):
      tempn = n * -1
   else:
      tempn = n

   subres = powerRecursive(k, tempn//2)
   if(tempn % 2 == 0):
      res = subres * subres
   else:
      res = subres * subres * k

   if(n < 0):
      return (1/res)

   return res

def powerIterative(k, n):
   
   res = 1
   while(n > 0):
      if(n % 2 != 0):
         n = n - 1
         res = res * k
      n = n // 2
      k = k * k

   return res
   
# print(powerIterative(2, 1))
# print(powerIterative(2, 2))
# print(powerIterative(2, 4))
# print(powerIterative(2, 13))
# print(powerIterative(2, -8))
# print(powerRecursive(3, -7))


# 2^8 = 2^4 * 2^4
# 2^4 = 2^2 * 2^2
# 2^2 = 2^1 * 2^1
# 2^1 = 2
# 2^0 = 1

# ===

# 2^12 = 2^6 * 2^6
# 2^6 = 2^3 * 2^3
# 2^3 = 2^2 * 2^1
# 2^2 = 2^1 * 2^1
# 2^1 = 2
# 2^0 = 1

# 2^6 = 2^1 * 2^1
# 2^3 = 2^2 * 2^1
# 2^2 = 2^3 * 2^3
# 2^1 = 2^6 * 2^6

#======
# 2^-2 = 2^-1 * 2^-1
# 2^-1 = 1/2

#====
# 2^-3 = 2^-2 * 2^-1
# 2^-2 = 2^-1 * 2^-1
# 2^-1 = 1/2