#計算留言的平均長度

data = []
tot = 0
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		tot = tot + len(line)

print ('總共有', len(data),'筆留言')
print ('每則留言平均長度為', tot / len(data), '個字')

#篩選 字數少於100的資料筆數

short = []
for msg in data:
	if len(msg) < 100:  
		short.append(msg)

print ('其中有', len(short), '筆為短留言')
print('[舉例]第一則留言為:', short[0])


#篩選好的留言
good = [nice for nice in data if 'good' in nice]
print ('其中有', len(good), '筆為正面的留言')
print('[舉例]第一則留言為:', good[0])
