__date__ ='20180920'

print('12345678901234567890')
tDict={'headers':'001','host':'192.168.0.1'}
res='headers:{headers:#<5}host:{host}\n'.format(**tDict) #从被引入的数据第一个开始算加几个#
res+='#'*65+'3\n'  #覆盖之前的
res+='{0:^10}|{1:^10}zt'.format('time','info')#^居中对齐
print(res)
# res = 'code: {nu: <20} company: {com: <15} ' \
#       'is checked: {ischeck}\n'.format(**data)
# res += '=' * 65 + '\n'
# res += '{0: ^21}|{1: ^44}\n'.format('time', 'content')
# for item in data['data']:
#     res += '-' * 65 + '\n'
#     res += '{time: ^21}| {context}\n'.format(**item)
# res += '=' * 65 + '\n'
# return res

