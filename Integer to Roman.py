class Solution:
    def intToRoman(self, num: int) -> str:
        out=''
        if num>999:
            for i in range(num//1000):
                out=out+'M'
            num=num%1000
        if num>899:
            out=out+'CM'
            num=num%900
        if num>499:
            out=out+'D'
            num=num%500
        if num>399:
            out=out+'CD'
            num=num%400
        if num>99:
            for i in range(num//100):
                out=out+'C'
            num=num%100
        if num>89:
            out=out+'XC'
            num=num%90
        if num>49:
            out=out+'L'
            num=num%50
        if num>39:
            out=out+'XL'
            num=num%40
        if num>9:
            for i in range(num//10):
                out=out+'X'
            num=num%10
        if num>8:
            out=out+'IX'
            num=num%9
        if num>4:
            out=out+'V'
            num=num%5
        if num>3:
            out=out+'IV'
            num=num%4
        if num>0:
            for i in range(num//1):
                out=out+'I'
            num=num%1
        return out
