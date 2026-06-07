class solution:
    def finalValueOperatins(self,operations):
        x=0
        for op in operations:
            if "++"in op:
                x=x+1
            else:
                x=x-1
        return x
operations=["--x","x++",]
obj=solution()
print(obj.finalValueOperatins(operations))