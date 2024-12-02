# a = ("1231","啊啊啊啊","1assd")
# print(type(a),a)
# #圆括号是元组
# b = ["1231","啊啊啊啊","1assd"]
# print(type(b),b)
#
# c = "123112312112"
# print(type(c))
#
# d = {"1":1,"2":2}
# print(type(d),d["1"])

# name = "pengyuyyan"
# age = 40
# height = 182.0
# print(name)
# print(age)
# print(height)

#给变量largest_city赋值字符串"Beijing"，并打印变量largest_city
# largest_city = "Beijing"
# print(largest_city)

# 给变量city赋值"Beijing"，然后打印变量city，再给变量city赋值"Shanghai"，然后打印变量city
# city = "Beijing"
# print(city)
# city = "Shanghai"
# print(city)

# 我们写两行代码，第一行：用代码来计算1+1，并赋值给变量answer；第二行：打印变量answer
# answer = 1+1
# print(answer)

# 我们同样可以只写一行代码，来完成上面的功能，直接打印1 + 1
# print(1+1)

# 第一行代码，计算8 - 2，并赋值给answer1，第二行代码打印变量answer1
# 第三行代码，计算8/ 2，并赋值给answer2，第四行代码打印变量answer2
# answer1 = 8-2
# print(answer1)
# answer2 = 8/2
# print(answer2)

# 第一行代码，计算1.5 + 1.5，直接打印结果
# 第二行代码，计算1.5 * 1.5，直接打印结果
# print(1.5+1.5)
# print(1.5*1.5)

# 计算双十一购买的商品需要付多少钱
# 单个商品价格分别保存在变量price1，price2，price3中，折扣存储在变量discount中
# 1.将单个商品价格相加计算出商品总价
# 2.将商品总价*折扣计算出应付总金额，并将应付总金额赋值给变量total
# 2.使用print输出结果tota
# price1 = 286
# price2 = 399
# price3 = 899
# discount = 0.7
# total = (price1+price2+price3)*discount
# print(total)

# 用取整数商//的方法，计算111在百位上的数值，并输出。
# print(111//100)

# 计算520除以2的余数，将结果赋值给变量result，使用print()输出result
# result = 520%2
# print(result)

# 给变量account赋值5000，然后使用格式化输出打印print(f"您的账户余额{account}")
# account = 5000
# print(f"您的账户余额{account}")



# 今天是星期天，所以我们可以给变量today_is_sunday赋值True，同时给变量today_is_friday赋值False
# 然后我们分别打印输出这两个变量
# today_is_sunday = True
# today_is_friday = False
# print(today_is_sunday)
# print(today_is_friday)

# 我们分别打印一下这四个比较运算的结果，2 > 1，5 < 4，1 >= 1，20 <= 10
# print(2 > 1)
# print(5 < 4)
# print(1 >= 1)
# print(20 <= 10)

# 我们先给一个变量number_a赋值一个数10，然后再比较这个变量是否大于9，并打印这个比较的结果
# number_a = 10
# print(number_a > 9)

# 我们给三个变量result_1，result_2，result_3，分别赋值三个逻辑运算的结果：
# True and False，True or False，not True，并且打印这三个变量，看看运算的结果是什么~
# result_1 = True and False
# result_2 = True or False
# result_3 = not True
# print(result_1)
# print(result_2)
# print(result_3)

# 今天是周天，我们给变量today_is_sunday赋值True，然后进行一次判断，
# 如果今天是周天的话，我们就打印输出“今天不用工作！”
# today_is_sunday = True
# if True:
#     print("今天不用工作！")


# 我们来写一个if判断，如果lilei报考的志愿lilei_application是“清华大学”，并且它的高考分数exam_score大于了670，
# 他就会被录取，输出“你被清华大学录取了”。而lilei报考的就是清华大学，并且高考成绩是676
# lilei_application = "清华大学"
# exam_score = 676
# if (lilei_application == "清华大学") and (exam_score > 670):
#     print("你被清华大学录取了")

# 给一个变量number_a赋值None，然后判断它，如果number_a是空值，就输出"这是一个空值"
# number_a = None
# if number_a == None:
#     print("这是一个空值")

# 给一个变量number_a赋值10，判断number_a是否等于10；如果等于10的话：1，给number_a赋值1；2，并且打印输出number_a的值；3，然后再赋值0；4，并且打印输出number_a的值；我们就会得到一个竖排的10
# *注意if内的这四行代码属于同一个缩进里面的代码块
# number_a = 10
# if number_a == 10:
#     number_a = 1
#     print(number_a)
#     number_a = 0
#     print(number_a)


# 如果今天下雨，就输出“今天就不跑步了”，否则的话就输出“今天要跑步”。而今天是下雨的，today_weather = "下雨"，尝试用if-else结构写一个双向判断
# today_weather = "下雨"
# if today_weather == "下雨" :
#     print("今天就不跑步了")
# else :
#     print("今天要跑步")

# 我们需要根据余额来判断要不要买一个包包，如果余额大于10000的时候，输出“立刻买”；如果余额大于1000但是小于等于10000的时候，输出“等等再买”；其余情况，输出“暂时不买了”，给余额变量money_left赋值20000
# money_left = 20000
# if money_left > 10000:
#     print("立刻买")
# elif (money_left > 1000) and (money_left <= 10000):
#     print("等等再买")
# else:
#     print("暂时不买了")