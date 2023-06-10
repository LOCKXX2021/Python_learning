def func(days):
    days_list = ['一','二','三','四','五','六','七']
    match days:
        case days:
            print('今天是周{}'.format(days_list[days-1]))
days = int(input('请输入1-7之间的整数'))
func(days)