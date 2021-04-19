import linecache,re,time,sys


data = open('access.log')
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
cache_name = './cache/' + now + 'cache.txt'

def stri(keyword):
    i = 0
    for e in data:
        i = i + 1
        search0 = re.search('Mozilla',e)#跳过
        search1 = re.compile(keyword, re.I)


        if search0 == None:


            with open(cache_name, "a") as f:
                #print('这是第', i, '行，正在搜索关键字')
                try:
                    if type(search1.search(e).group()) == str:
                        f.write(linecache.getline('1.txt', i))
                    else:
                        print('n')

                except Exception as error:
                    pass




        else:
            pass
            #print('这是第',i,'行，存在忽略字符串，已忽略该行')
            #print('-' * 40)

    with open(cache_name) as file_obj:
        content = file_obj.read()
        print(content)




def numbsech():
    #ascii--先删除第一个等号前部分
    #cache_name = './cache/' + now + 'cache.txt'
    cachefile = open(cache_name)
    str = cachefile.readline()
    #print(str[:str.index('=')+1])
    cut = str[:str.index('=')+1]

    #cache2_name = './cache/' + now + 'cache.txt'
    with open(cache_name, "w") as f1:
        f1.write(str.replace(cut,''))

    #再删除第二个等号前部分
    cache2 = open(cache_name)
    str2 = cache2.readline()
    cut2 = str2[:str2.index('=')]

    #cache3_name = './cache/' + now + 'cache.txt'
    with open(cache_name, "w") as f2:
        f2.write(str2.replace(cut2,''))

    #读取
    cache3 = open(cache_name)
    str3 = cache3.readline()
    print(str3)
    cut3 = str3[:str3.index(',')+1]
    print(cut3)





if __name__ == '__main__':
    check1 = sys.argv[1]
    if check1 == 'stri':
        keyword = sys.argv[2]
        stri(keyword)
    elif check1 == 'number':
        keynumb = sys.argv[2]
        stri(keynumb)
    else:
        print('请输入正确参数，如：stri，number')

