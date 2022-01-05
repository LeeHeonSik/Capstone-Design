
# 해당 코드세트가 나온것만 검색하기
wannacheck = 'Am_F'
a, b = wannacheck.split('_')
new_out = []
for chord in sortedC:
  if wannacheck == chord[0][:len(wannacheck)] and a not in chord[0][len(wannacheck):] and b not in chord[0][len(wannacheck):]:
    new_out.append(chord)

x = [i[0] for i in new_out]
y = [i[1] for i in new_out]



