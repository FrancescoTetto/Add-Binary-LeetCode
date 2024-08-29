class Solution(object):
    def addBinary(self, a, b):
        a_int = int(a,2)
        b_int = int(b,2)
        sum_a_b  = bin(a_int + b_int)
         
        return str(sum_a_b[2:])

solution=Solution()
print(solution.addBinary('11', '1'))
