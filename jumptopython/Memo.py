import sys


option = sys.argv[1]
memo = sys.argv[2]

if option == 'a':
    f = open('memo.txt','a')    #두번쨰 파라미터는 파일모드로 ,a는 파일에 추가 w는 처음부터 다스쓰기 r은 읽기다.
    f.write(memo)
    f.write('\n')
    f.close
elif option == 'r':
    f = open('memo.txt','r')
    print(f.readline(),end='')
    print(f.readline(),end='')
    print(f.readline(),end='')
else :
    print('옵션이 잘못되었습니다.')


