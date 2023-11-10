#計算留言的平均長度

data = []
tot = 0
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip)
		count += 1
		tot = tot + len(line)
print ('總共有', len(data),'筆留言')
print ('每則留言平均長度為', tot / len(data), '個字')