ppl = {'person1': { 'name': 'John Cena','size': {'height': 175,'weight': 100}},'person2': {'name': 'Chuck Norris','size': {'height': 180,'weight': 90}}, 'person3': { 'name': 'Jon Skeet','size': {'height': 185,'weight': 110 } } }
#print(dict(sorted(ppl['person1']['size'].items()),key=lambda x:x[1]))
for i in ppl.keys():
  pp=ppl[i]['size']
  for i in pp:
    print(sorted(pp.items(),key=lambda x:x[i][0],reverse=True))
  #print(dict(sorted(pp.items()),key=lambda x:x['weight']))
