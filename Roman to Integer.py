class Solution:
    def romanToInt(self, s: str) -> int:
        start=-1
        out=0
        end=len(s)-1
        while end>=0:
            if s[end]=='I':
                out=out+1
                end=end-1
            elif s[end]=='V':
                if s[end-1]=='I' and end>=1:
                    out=out+4
                    end=end-2
                else:
                    out=out+5
                    if end==0:
                        return out
                    end=end-1
            elif s[end]=='X':
                if s[end-1]=='I' and end>=1:
                    out=out+9
                    end=end-2
                else:
                    out=out+10
                    if end==0:
                        return out
                    end=end-1
            elif s[end]=='L':
                if s[end-1]=='X' and end>=1:
                    out=out+40
                    if end==0:
                        return out
                    end=end-2
                else:
                    out=out+50
                    if end==0:
                        return out
                    end=end-1
            elif s[end]=='C':
                if s[end-1]=='X' and end>=1:
                    out=out+90
                    if end==0:
                        return out
                    end=end-2
                else:
                    out=out+100
                    if end==0:
                        return out
                    end=end-1
            elif s[end]=='D':
                if s[end-1]=='C' and end>=1:
                    out=out+400
                    end=end-2
                else:
                    out=out+500
                    end=end-1
            elif s[end]=='M':
                if s[end-1]=='C' and end>=1:
                    out=out+900
                    if end==0:
                        return out
                    end=end-2

                else:
                    out=out+1000
                    if end==0:
                        return out
                    end=end-1
        return out
