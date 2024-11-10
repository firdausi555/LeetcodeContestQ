class Solution:
    def smallestNumber(self, n, t):
        
        def product(n):
            product = 1
            while n > 0:
                product *= n % 10  
                n //= 10  
            return product

        
        
        while True:
            if product(n) % t == 0:
                return n
            n += 1
