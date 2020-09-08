class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        li=[]
        for i in range(1,n+1):
            if i%3!=0 and i%5!=0:
                item=str(i)
            if i%3==0:
                item='Fizz'
            if i%5==0:
                item='Buzz'
            if i%3==0 and i%5==0:
                item='FizzBuzz'
            li.append(item)
        return li
            
        