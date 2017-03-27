import sys
file = open("text.txt",'r')
input_text = sys.argv[1]
count = 0
while True:
	line = file.readline()
	count += line.count(input_text)
	if not line: break

print(count)
