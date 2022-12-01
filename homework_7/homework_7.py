# In[26]:


# # 1 Sequential_map

# Sequential_map - функция должна принимать в качестве аргументов любое количество функций (позиционными аргументами, НЕ списком), а также контейнер с какими-то значениями. Функция должна возвращать список результатов последовательного применения переданных функций к значениям в контейнере. Например, sequential_map(np.square, np.sqrt, lambda x: x**3, [1, 2, 3, 4, 5]) -> [1, 8, 27, 64, 125]

# In[78]:


def sequential_map (*args):
    funcs = list(args)
    vals = funcs.pop(-1)
    for fun in funcs:
        vals = list(map(fun, vals)) 
    return vals


# # 2 Consensus_filter

# consensus_filter - функция должна принимать в качестве аргументов любое количество функций (
# позиционными  аргументами, НЕ списком), возвращающих True или False, а также контейнер с какими-то значениями. Функция должна возвращать список значений, которые при передаче их во все функции дают True. Например: consensus_filter(lambda x: x > 0, lambda x: x > 5, lambda x: x < 10, [-2, 0, 4, 6, 11]) -> [6]

# In[53]:


def consensus_filter (*args):
    funcs = list(args)
    vals = funcs.pop(-1)
    for fun in funcs:
        vals = list(filter(fun, vals))
        if vals == []:
            return vals
    return vals


# # 3 Conditional_reduce 

# функция должна принимать 2 функции, а также контейнер с значениями. Первая функция должна принимать 1 аргумент и возвращать True или False, вторая также принимает 2 аргумента и возвращает значение (как в обычной функции reduce). conditional_reduce должна возвращать одно значение - результат reduce, пропуская значения с которыми первая функция выдала False. Например, conditional_reduce(lambda x: x < 5, lambda x, y: x + y, [1, 3, 5, 10]) -> 4

# In[78]:


def conditional_reduce(filter_fun, reduce_fun, vals):
    filter_vals = list(filter(filter_fun, vals))
    for idx in range(1, len(filter_vals)):
        filter_vals[idx] = reduce_fun(filter_vals[idx-1], filter_vals[idx])
    return filter_vals[-1]


# # 4 func_chain 

# функция должна принимать в качестве аргументов любое количество функций (
# позиционными  аргументами, НЕ списком). Функция должна возвращать функцию, объединяющую все переданные последовательным выполнением. Например, my_chain = func_chain(lambda x: x + 2, lambda x: (x/4, x//4)). my_chain(37) -> (9.75, 9).

# In[80]:


def func_chain(*args):
    def custom_chain(*vals):
        funcs = args
        for fun in funcs:
            vals = list(map(fun, vals)) 
        return vals
    return custom_chain


#