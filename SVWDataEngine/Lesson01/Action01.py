'''
Action1：求2+4+6+8+...+100的求和，用Python该如何写
'''
class SumClass:
    def getSumByFor(self):
        sum = 0
        for i in range(2, 102, 2):
            sum += i
        print('result of for method is:', sum)

    def getSumByWhile(self):
        i = 2
        sum = 0
        while i <= 100:
            sum += i
            i += 2
        print('result of while method is:', sum)

if __name__ == "__main__":
    result = SumClass()
    result.getSumByFor()
    result.getSumByWhile()
