import pickle
import time


class Student:
    def __init__(self,sid,name,sexual,grade,a_class,majory):
        self.sid = sid
        self.name = name
        self.sexual = sexual
        self.grade = grade
        self.a_class = a_class
        self.majory = majory

    def get_info(self):
        print('学号：%s,姓名：%s，性别，%s，年级：%s，班级：%s,专业：%s'
              %(self.sid,self.name,self.sexual,self.grade,self.a_class,self.majory))


def Ceate_index(path):
    i = 0
    size = 300
    Student_dict = {}
    f = open(path, 'rb')
    while True:
        try:
            f.seek(i * size)
            st = pickle.load(f)
            Student_dict[st.sid] = i
            i += 1
        except EOFError:
            break
    f.close()
    return Student_dict

def output(i, path):
    size = 300
    f = open(path, "rb")
    f.seek(i * size)
    st = pickle.load(f)
    st.get_info()
    f.close()

def main():
    path = r"student.db"
    student_dict = Ceate_index(path)
    print("输入0为退出")
    while True:
        sid = input("查询的学号为：")
        if sid == "0":
            print("查询结束")
            break
        else:
            try:
                start = time.perf_counter()
                i = student_dict[sid]
                output(i, path)
                end = time.perf_counter()
                usetime = end - start
                print("查询成功,查询时间为%f" % usetime)
            except KeyError:
                print("没有学号为{}的学生".format(sid))

if __name__ == '__main__':
    main()