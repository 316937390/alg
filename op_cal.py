#coding=utf-8
import sys 

def isOperand(i):
    if i in ['0','1','2','3','4','5','6','7','8','9']:
        return True
    else:
        return False
def isOperator(i):
    if i in ['+','-','*','/']:
        return True
    else:
        return False
def lstPop(l):
    assert len(l) != 0
    return l.pop()

def calFunc(l,r,op):
    if op == '+':
        return l+r
    if op == '-':
        return l-r
    if op == '*':
        return l*r
    if op == '/':
        return l//r

def opPri(i,j):
    p = {'*':0,'/':0,'+':1,'-':1}
    if p[i] < p[j]:
        return 0 #  i比j高
    elif p[i] == p[j]:
        return 1 #  i和j一样
    elif p[i] > p[j]:
        return -1 # i比j低

str_line = '6/2+1*2+3'
operand = []
operator = []
result = None
for i in str_line:
    if isOperand(i):
        operand.append(i)
    elif isOperator(i):
        if len(operator) != 0:
            while len(operator) != 0:
                prev = operator[-1]
                if opPri(i,prev) == 1 or opPri(i,prev) == 0:
                    break
                else: # 比前一个操作符优先级低，要先计算前一个操作符
                    r = lstPop(operand)
                    l = lstPop(operand)
                    op = lstPop(operator)
                    tmp = calFunc(int(l), int(r), op)
                    operand.append(tmp)
            operator.append(i)
        else:
            operator.append(i)

print('\n{}\n{}'.format(operand,operator))

while len(operand) != 0 or len(operator) != 0:
    Flago = False
    Flagl = False
    Flagr = False
    r = None
    l = None
    op = None
    if len(operator) != 0:
        op = lstPop(operator)
    else:
        Flago = True
    if len(operand) != 0:
        r = int(lstPop(operand))
    else:
        Flagr = True
    if len(operand) != 0:
        l = int(lstPop(operand))
    else:
        Flagl = True
    if (not Flago) and (not Flagr) and (not Flagl):
        t = calFunc(l, r, op)
        operand.append(t)
    else:
        result = r
        break

print('{} = {}'.format(str_line,result))

