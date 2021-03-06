#  函数是一个编程语言中通用的术语，主要作用就是定义一些比较固定的逻辑


# 函数样例一
# 定义一个函数 用def说明这是函数  m1是函数的名字 ()表示的是函数调用需要传入的内容
def m1():
    print("我是函数第一个演示代码")
# 执行一个函数
m1()

# 函数样例二
# 在()随意定义一个名字，在函数内部可以直接使用它
def m2(par):
    print("Welcome", par)
# 执行这个函数必须给这个函数一个内容，否则无法使用
m2('二')

# 函数样例三
# 在()随意定义两个名字，在函数内部可以直接使用它
def m3(par1,par2):
    print("参数内容是:",par1,par2)
# 执行这个函数必须给这个函数两个内容，否则无法使用
m3(1,2)

# 函数样例四
# 在()随意定义两个名字，在函数内部可以直接使用它
def m4(par1,par2):
    # 函数执行后，会通过return这个关键字返回一个结果
    return par1+par2
# 调用m4这个函数并将返回的结果进行打印输出
print(m4(1,2))