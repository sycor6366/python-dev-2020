


test = {"name":"zhangsan", "tel":1234567890123}


# L = []
L = [{'name': 'zhangsan', 'tel': 123456, 'age': 18}, {'name': 'lisi', 'tel': 3213213, 'age': 28}, {'name': 'wangwu', 'tel': 3333333, 'age': 48},
     {'name': 'zhangsan', 'tel': 1223456, 'age': 38}]


def get_data_first():
    name = input("请输入姓名")
    tel = input("请输入电话")
    age = input("请输入年龄")
    get_data(name, tel, age)

def get_data(name, tel, age):
    data = {}
    data["name"] = name
    data["tel"] = tel
    data["age"] = age
    return data


def add_new(D):
    if D in L:
        print("姓名:{}, 电话：{}, 年龄：{} 已存在通讯录中，无法添加成功".format(D["name"], D["tel"], D["age"]))
    else:
        L.append(D)
        print("添加成功,姓名为{}, 电话为{}, 年龄为{}".format(D["name"], D["tel"], D["age"]))


def find_data(name):
    find_data_list = []
    for i in L:
        if i["name"] == name:
            find_data_list.append(i)
    if len(find_data_list) == 0:
        print("没有找到姓名为{}的数据".format(name))
    else:
        print("共计找到{}位姓名为{}的用户,详情为：".format(len(find_data_list), name))
        for i in find_data_list:
            print("姓名{}, 电话{}, 年龄为{}".format(i["name"], i["tel"], i["age"]))


def del_data(D):
    if D in L and len:
        L.remove(D)
    else:
        print("通讯录中不存在需要删除的人物")


def update_data(D, new_D):
    if D in L:
        index = L.index(D)
        L[index] = new_D
        print("更改成功,已将该用户的姓名{},电话{},年龄{}，更改为姓名{},电话{},年龄{}".format(
            D["name"], D["tel"], D["age"], new_D["name"], new_D["tel"], new_D["age"]))
    else:
        print("没有找到需要更改的数据")


def menu():
    menu = {1: "新增内容",
            2: "查询内容",
            3: "更改内容",
            4: "查询内容",
            5: "查询所有内容",
            6: "退出"}
    for i in menu:
        print("--------------------输入{}， 为{}--------------------".format(i, menu[i]))


def main(data):
    if data == 1:
        print("请依次按提示输入您要新增的姓名、电话、年龄")
        name = input("请输入您要新增的姓名")



if __name__ == "__main__":
    # # add_new("zhangsan", 123456, 18)
    #     # # print(L)
    #     # # find_data("zhangsan")
    #     # D = get_data("zhangsan", 1223456, 38)
    #     # new_D = get_data("zhangsan11111", 123456, 18)
    #     # add_new(new_D)
    #     # #update_data(D, new_D)
    #     # print(L)
    def main(a):
        if True:
            pass
    print("--------------------欢迎使用通讯录功能--------------------")
    menu()
    input("请输入您要使用的功能：")