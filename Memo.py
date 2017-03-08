import sys


option = sys.argv[1]
memo = sys.argv[2]

if option == 'a':
    f = open('memo.txt','a')
    f.write(memo)
    f.write('\n')
    f.close
elif option == 'r':
    f = open('memo.txt')
    f.read()
else :
    print('옵션이 잘못되었습니다.')


