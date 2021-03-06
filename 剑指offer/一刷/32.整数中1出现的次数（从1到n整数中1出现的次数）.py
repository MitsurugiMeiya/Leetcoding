

class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        print(self.helper(n))
        return self.helper(n)

    def helper(self,n):
        res = 0
        bit = 1
        while bit <= n:
            high = n / bit #31155 / 100 = 311
            low = n % bit #31155 % 100 = 55
            # (311 + 8)/10 * 100 。311个100里，每个100里带有10个带1的数（10-19），/10是为了查看
            # 有没有进一位
            res += (high + 8) / 10 * bit + (high % 10 == 1) * (low+1)
            bit *= 10
        return res


if __name__ == "__main__":
    solution = Solution()
    solution.NumberOf1Between1AndN_Solution(2573)




"""
自己思路：隐约之间感觉到是和进制有关的，转换了几个之后，似乎又找不到什么要点

0000001 1
0001010 10
1100100 100

后面发现自己的思路完全是错误的：

正确思路：
https://cuijiahua.com/blog/2017/12/basis_31.html
1、思路
三种情况，i位>=2, i位 == 1，i位 == 0，所以用+8来决定是否进位，这样的话，2+8 / 10进位，0+8/10不进位

根据设定的整数位置，对n进行分割，分为两部分，高位n/i，低位n%i
    当i表示百位，且百位对应的数>=2,如n=31456,i=100，则a=314,b=56，此时百位为1的次数有a/10+1=32（最高两位0~31），每一次都包含100个连续的点，即共有(a/10+1)*100个点的百位为1
    当i表示百位，且百位对应的数为1，如n=31156,i=100，则a=311,b=56，此时百位对应的就是1，则共有a/10(最高两位0-30)次是包含100个连续点，当最高两位为31（即a=311），本次只对应局部点00~56，共b+1次，所有点加起来共有（a/10*100）+(b+1)，这些点百位对应为1
    当i表示百位，且百位对应的数为0,如n=31056,i=100，则a=310,b=56，此时百位为1的次数有a/10=31（最高两位0~30）

综合以上三种情况，当百位对应0或>=2时，有(a+8)/10次包含所有100个点，还有当百位为1(a%10==1)，需要增加局部点b+1
之所以补8，是因为当百位为0，则a/10==(a+8)/10，当百位>=2，补8会产生进位位，效果等同于(a/10+1)
"""