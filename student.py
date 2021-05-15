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