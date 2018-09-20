from urllib.request import urlopen, Request
import json,random
from urllib.parse import urlencode
#join的作用
possible_company_name=['yunda', 'zhongtong']
possible_company_name2=['yunda=shunfeng']
print('Possible company:', '，'.join(possible_company_name))
print('Possible company:', '，'.join(possible_company_name2))#这个只是把唯一的一个数据传入了字符串当中



guess_url='http://m.kuaidi100.com/autonumber/auto?num=3953390300077'

#获取数据
res = json.loads(urlopen(guess_url).read().decode('utf-8'))#json是为了把获得的数据变成列表类型
print(type(res))
print(res)

#如果是多个公司，可能是这样的：
# res=[{'comCode': 'yunda,zhongtong', 'id': '', 'noCount': 198, 'noPre': '395339', 'startTime': ''}]
possible_company_name = [company['comCode'] for company in res]  #使company成为一个字典 之后再查询字典
# print(possible_company_name)
print('Possible company:', '，'.join(possible_company_name))



QUERY = 'http://m.kuaidi100.com/query?{0}'
params = urlencode({
    'type': 'yunda',
    'postid': 3953390300077,
    'id': 1,
    'valicode': '',
    'temp': random.random()
})
#所以说urlencode并不是没用，当字典文件多的时候便体现出来了作用，用&连在一起
print(params)
req = Request(QUERY.format(params), headers={'Referer': guess_url})
res = json.loads(urlopen(req).read().decode('utf-8')) #获取所有信息
print(type(res))