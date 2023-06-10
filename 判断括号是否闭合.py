s = input("请输入测试字符串：")

# 创建一个特殊列表
stack = []

for c in s:
    # 如果是左括号，那么添加到特殊列表中
    if c == '(' or c == '[' or c == '{':
        stack.append(c)
    # 如果是右括号的情况
    else:
        # 如果碰到右括号，但特殊列表中没有左括号，那么肯定是非法的
        if len(stack) == 0:
            print("非法T_T")
            break

        # 逐个给出 c 对应的右括号 d
        if c == ')':
            d = '('
        elif c == ']':
            d = '['
        elif c == '}':
            d = '{'

        # 对比 d 和从特殊列表尾部弹出的元素
        if d != stack.pop():
            print("非法T_T")
            break
else:
    # 如果循环走完，特殊列表不为空，那么肯定是左括号比右括号多的情况
    # 那肯定有同学会问：右括号比左括号多的情况在哪里判断？
    # 小甲鱼答：在上面 d != stack.pop() 的判断中已经可以排除了~
    if len(stack) == 0:
        print("合法^o^")
    else:
        print("非法T_T")