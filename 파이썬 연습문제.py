
# coding: utf-8

# # 파이썬 연습문제 

#  - **1번: 다음 식의 결과값을 쓰시오**

# In[1]:


def iterable_test(x):
    try:
        iter(x)
        return ('iterable object')
    except TypeError:
        return ('non-iterable object')


Object = [['list'],{'set'},1,range(1,10), set(),frozenset({1,2}),'string',{'dict_key':'dict_value'}, True, dict(a=1)]
for x in Object:
    print('"{}" is a {}'.format(x,iterable_test(x)))


# Your Answer: x

# - **2번**

# In[3]:


People = ['주경', '형민', '채린', '지연']
iterator = iter(People)
for _ in range(0,len(People)+1):
    try:
        print(next(iterator))
    except:
        print('Raised StopIteration Error')


# - **3번**

# In[5]:


test = [['list'],'string', ('tuple'), dict(dict_key='dict_value'), frozenset({1,2,3}), (1,2), range(1,10), 34, set()]
se1 = set()
for Object in test:
    try:
        se1.add(Object)
    except:
        pass
print(se1)


# In[8]:


a = set()
b = 'abc'
a.add(b)
a


# - **4번**

# In[9]:


import numpy as np
matrix = np.array(range(1,11)).reshape(2,5)
for row in zip(['a','b'], matrix):
    print(row)


# - **5번**

# In[10]:


test = [['list'],'string', ('tuple'), dict(dict_key='dict_value'), frozenset({1,2,3}), (1,2), range(1,10), 34, set()]
for i in test:
    try:
        print("{}'s hash type is {}".format(i,hash(i)))
    except:
        print('{} is not hashable'.format(i))


# - **6번**

# In[11]:


def Filter(func, iterable):
    return ([x for x in filter(func,iterable)])

func = lambda x: x%3 == 0
fun = lambda x:x == 's'
test = [range(1,10), {1,2,3}, 'string']
for i in test:
    try:
        print(Filter(func,i))
    except:
        print(Filter(fun,i))


# - **7번**

# In[12]:


lyrics = '''
서명은다넘가
수풍 슬부데새
달 지는소 니나
정 로다서낙에떨지 는내
침면다 건는황길 마 게한번가  누
''' 
def addition(original,new_lyrics):
    return original + new_lyrics

new = '''
산월  어고벽비은슬 는 벽종이우지 리아 던심이절난
산조 어는해 일아이 시돋마
천은얼나멀  
면못오나
'''

result = map (addition, lyrics, new)
print(''.join(list(result)))

