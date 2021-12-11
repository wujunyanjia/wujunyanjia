"""
Project: 86python
Author:柠檬班-Tricy
Time:2021/11/24 19:11
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
"""
'''
1. 下面哪些不能作为标识符？-- 标识符命名
1、find 2、 _num 3、7val 4、add. 5、def 6、pan 7、-print 8、open_file 9、FileName
10、print 11、INPUT 12、ls 13、user^name 14、list1 15、str_
答案：
1、find  --ok
2、_num  -- ok
3、7val --不可以的  不能数字开头
4、add.   -- 不可以 
5、def  -- 关键字
6、pan  --ok 
7、-print  -- 不可以
8、open_file -- ok
9、FileName --ok 大驼峰命名
10、print  -- 函数名字？？--可以的，但是不推荐使用,会影响本身使用
11、INPUT -- ok  input()
12、ls - ok
13、user^name   --不可以
14、list1  - ok
15、str_  --ok
'''
'''
python的运算符：
1、算术运算符： + - * /
+ :两个数字相加 ；两个字符串的拼接
内置函数：数据类型的强制转化 str()-转化为字符串
                         int() -- 整型   float() --浮点型
*：除了表示两个数字的乘之外，表示字符串的重复输出 * 次数
print(10.1 + 20)
print("hello"+"lemon")
print("abc"+str(123))
print(20 - 10)
print( 2 * 5 )
print("我错了" * 10)
print(10 / 2)

2、赋值运算符  = +=  -=
num = 10  # 10赋值给num
num += 10 #==== num = num + 10
num -= 5
print(num)

3、比较运算符：== 、 > 、< 、>=、<=、 !=   -------- 运算结果是 布尔值 -- 真 假  True  False
print(100 < 100)
print("测试通过" == "测试失败")  # 判断字符串是否相等，断言 --自动化项目

4、逻辑运算符： or:假假为假   and 真真为真  not 非  --- 运算结果是 布尔值 -- 真 假  True  False
print(not 5 > 4)

5、成员运算符： in    not in  --- 判断元素是否是这个字符串/数据类型的里面
str1 = "lemon86"
print("w" in str1)
'''
'''
列表：[] --列表  -- list()
1、里面的元素可以是任何数据类型 -- int  float bool  字符串  list ，之间用逗号隔开
2、获取元素个数  -- 列表的长度 == len
3、元素可以重复的，统计重复元素出现的次数  --count
4、取值： 通过索引取值 [索引]
   取多个值： 切片 
扩展：列表的嵌套取值  ==print(list1[4][2])
5、列表里的元素是可以被改变的 -- 增加 删除  修改
list1 = [20,3.14,True,"Gala",[1,2,3,4,5],"Gala"] # 空列表
print(list1)
# print(len(list1))
# print(list1.count("Gala"))
# print(list1[3:7:1])
# print(list1[4][2])
# 增加
list1.append("小梅") # 追加了一个元素 --到列表的末尾 --最常用方法
print(list1)
list1.insert(3,"小米") # 指定位置进行元素的添加 插入
print(list1)
list1.extend(["小太阳","一凡","小七","Z","甜甜","无我"])  # 添加多个元素  --  放在换一个列表里，列表合并
print(list1)
# 删除
list1.pop(1)  # 默认删除最后一个元素 / 可以元素的位置进行删除
print(list1)
list1.remove(20) # 指定元素本身进行删除
print(list1)
# list1.clear() # 清空列表
# print(list1)
# 修改
list1[3] = "sam"  # 取值 再重新赋值  
print(list1)

元组 ： tuple  （）  -- 了解
1、里面的元素可以是任何数据类型 -- int  float bool  字符串  list tuple，之间用逗号隔开
2、获取元素个数  -- 列表的长度 == len
3、元素可以重复的，统计重复元素出现的次数  --count
4、取值： 通过索引取值 [索引]
   取多个值： 切片 
扩展：列表的嵌套取值
5、元组里的元素是不可以被改变的 --没有增删改
tuple1 = (True, '小米', 'Gala', 'sam', 'Gala', '小梅', '小太阳', '一凡', '小七', 'Z', '甜甜', '无我')
test1 = list(tuple1) # 转化为列表
test1[0] = "小句号"
tuple2 = tuple(test1)
print(tuple2)

字典：dict {}
1、元素是一个键值对 ： key ：value 
2、使用场景：物件-- 属性 ：人-- 名字 性别  身高 体重  ==字典存储物件各种属性
3、获取元素格式 -- len（）
4、取值：字典没有顺序 ，没有索引-- 不能通过索引取值
   只能通过key 取值 value ！！
5、字典是否可以修改元素 ？ -- key不可以被修改， value可以被修改
value： 增删改
dict1 = {"name":"小圆","gender":"male","weight":"70","hight":"180"}
print(dict1["name"])  # 只能通过key 取值 value
print(dict1.get("hight")) # 只能通过key 取值 value
# 增加 和修改
dict1["city"] = "深圳"  # 如果key不存在，新增加键值对 -一个
print(dict1)
dict1["name"] = "少年"  # 如果key存在，修改
print(dict1)
dict1.update({"hobby":"麻雀","phone":"13455667788","age":18}) # 字典合并操作- 增加多个元素
print(dict1)
# 删除
dict1.pop("weight")  # 指定key进行删除键值对
print(dict1)
   
集合 -set == 了解  == {}  -=很少
1、集合元素的不可以重复的 == 去重   == 无序
使用场景： 会列表做元素的去重
set1 = {1,2,3,4,3,4,5,4}
print(set1)
list1 = [1,2,3,44,5,4,4,3,2,2,2]
print(list1)
test1 = set(list1)
print(test1)
list2 = list(test1)
print(list2)
'''

# name = input("请输入你的名字：")  # 控制台输入 获取输入的值
# print(name)
# age = input("请输入你的年龄：")  # 控制台输入 获取输入的值
# print(age)
dict1 = {"name":"小米","age":18}
dict2 = dict(name="小米",
             age=18)
print(dict2.keys())

# list1 = [20,3.14,True,"Gala",[1,2,3,4,5],"Gala"] # 空列表
# print(list1)
# print(len(list1))
# print(list1.count("Gala"))
# print(list1[3:7:1])
# print(list1[4][2])
# 增加
# print(list1.append("小梅")) # 追加了一个元素 --到列表的末尾 --最常用方法



