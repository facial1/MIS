import tkinter as tk
from tkinter import ttk
from db import  db


#录入页 封装详情
class InsertFrame(tk.Frame):
    """一个允许用户将学生信息插入数据库的框架"""
    def __init__(self,root):
        """用输入小部件和一个按钮初始化框架"""
        super().__init__(root)
        self.name = tk.StringVar()
        self.gender = tk.StringVar()
        self.birth = tk.StringVar()
        self.student_number = tk.StringVar()
        self.grade = tk.StringVar()
        self.collage = tk.StringVar()
        self.phone= tk.StringVar()
        self.status = tk.StringVar()
        self.create_page()
    def create_page(self):
        """在框架上创建输入小部件和按钮"""
        tk.Label(self).grid(row=0,pady=10)

        tk.Label(self,text='姓 名:').grid(row=0,column=1,pady=10)
        tk.Entry(self,textvariable=self.name).grid(row=0,column=2,pady=10)

        tk.Label(self,text='性  别:').grid(row=1,column=1,pady=10)
        tk.Entry(self,textvariable=self.gender).grid(row=1,column=2,pady=10)

        tk.Label(self,text='出生日期:').grid(row=2,column=1,pady=10)
        tk.Entry(self,textvariable=self.birth).grid(row=2,column=2,pady=10)

        tk.Label(self,text='学  号:').grid(row=3,column=1,pady=10)
        tk.Entry(self,textvariable=self.student_number).grid(row=3,column=2,pady=10)

        tk.Label(self,text='班  级:').grid(row=4,column=1,pady=10)
        tk.Entry(self,textvariable=self.grade).grid(row=4,column=2,pady=10)

        tk.Label(self,text='学  院:').grid(row=5,column=1,pady=10)
        tk.Entry(self,textvariable=self.collage).grid(row=5,column=2,pady=10)

        tk.Label(self,text='电  话:').grid(row=6,column=1,pady=10)
        tk.Entry(self,textvariable=self.phone).grid(row=6,column=2,pady=10)

        tk.Button(self, text="录入",command=self.recode_info).grid(row=7, column=2, pady=10)
        tk.Label(self, textvariable=self.status).grid(row=8, column=2, pady=10,stick=tk.E)

    def recode_info(self):
        """将用户输入记录到数据库并清空输入小部件。"""
        stu = {"name": self.name.get(), "gender":self.gender.get(), "birth": self.birth.get(),
               "student_number": self.student_number.get(), "grade": self.grade.get(),
          "collage": self.collage.get(), "phone": self.phone.get()}
        #清空窗口
        self.name.set('')
        self.gender.set('')
        self.birth.set('')
        self.student_number.set('')
        self.grade.set('')
        self.collage.set('')
        self.phone.set('')
        db.insert(stu)
        self.status.set('获取数据成功')

#查询页 封装详情
class SearchFrame(tk.Frame):
    def __init__(self,root):

        super().__init__(root)

        self.table_view = tk.Frame()

        self.table_view.pack()

        self.create_page()

    def create_page(self):
            columns = ("name","gender","birth","student_number","grade","collage","phone")
            columns_values = ("姓名", "性别", "出生日期", "学号", "班级","学院 ","电话")

            self.tree_view = ttk.Treeview(self,show='headings',columns=columns)

            #创建树形图视图小部件
            self.tree_view.column('name'  ,width=80,anchor='center')
            self.tree_view.column('gender',width=80, anchor='center')
            self.tree_view.column('birth' ,width=80, anchor='center')
            self.tree_view.column('student_number', width=80, anchor='center')
            self.tree_view.column('grade', width=150, anchor='center')
            self.tree_view.column('collage', width=80, anchor='center')
            self.tree_view.column('phone', width=80, anchor='center')

            self.tree_view.heading('name',    text='姓名')
            self.tree_view.heading('gender',  text='性别')
            self.tree_view.heading('birth',   text='出生日期')
            self.tree_view.heading('student_number',  text='学号')
            self.tree_view.heading('grade',   text='班级')
            self.tree_view.heading('collage', text='学院')
            self.tree_view.heading('phone',   text='电话')

            self.tree_view.pack(fill=tk.BOTH,expand=True)

            self.show_data_frame()

            tk.Button(self,text='刷新数据',command=self.show_data_frame).pack(anchor=tk.E,pady=5)
    def show_data_frame(self):
           #删除旧阶段  用以刷新数据
            for _ in map(self.tree_view.delete,self.tree_view.get_children('')):
                pass
            students = db.all()
            index =0
            for stu in students:
                self.tree_view.insert('',index+1,values=(
                    stu['name'],stu['gender'],stu['birth'],stu['student_number'],stu['grade'],stu['collage'],stu['phone']
                ))

#删除页 封装详情
class DeleteFrame(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        self.username = tk.StringVar()
        self.status = tk.StringVar()
        tk.Label(self, text='根据名字删除数据').pack()
        tk.Entry(self, textvariable=self.username).pack()
        tk.Button(self, text='删除',command=self.delete).pack()
        tk.Label(self, textvariable=self.status).pack()

    def delete(self):
        username = self.username.get()
        flag,message = db.delete_by_username(username)
        self.status.set(message)

#修改页 封装详情
class ChangeFrame(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        self.name = tk.StringVar()
        self.gender = tk.StringVar()
        self.birth = tk.StringVar()
        self.student_number = tk.StringVar()
        self.grade = tk.StringVar()
        self.collage = tk.StringVar()
        self.phone= tk.StringVar()
        self.status = tk.StringVar()
        self.create_page()

    def create_page(self):
        """在框架上创建输入小部件和按钮"""
        tk.Label(self).grid(row=0, pady=10)

        tk.Label(self, text='姓 名:').grid(row=0, column=1, pady=10)
        tk.Entry(self, textvariable=self.name).grid(row=0, column=2, pady=10)

        tk.Label(self, text='性  别:').grid(row=1, column=1, pady=10)
        tk.Entry(self, textvariable=self.gender).grid(row=1, column=2, pady=10)

        tk.Label(self, text='出生日期:').grid(row=2, column=1, pady=10)
        tk.Entry(self, textvariable=self.birth).grid(row=2, column=2, pady=10)

        tk.Label(self, text='学  号:').grid(row=3, column=1, pady=10)
        tk.Entry(self, textvariable=self.student_number).grid(row=3, column=2, pady=10)

        tk.Label(self, text='班  级:').grid(row=4, column=1, pady=10)
        tk.Entry(self, textvariable=self.grade).grid(row=4, column=2, pady=10)

        tk.Label(self, text='学  院:').grid(row=5, column=1, pady=10)
        tk.Entry(self, textvariable=self.collage).grid(row=5, column=2, pady=10)

        tk.Label(self, text='电  话:').grid(row=6, column=1, pady=10)
        tk.Entry(self, textvariable=self.phone).grid(row=6, column=2, pady=10)

        tk.Button(self, text="查询", command=self.search_user).grid(row=7, column=1, pady=10)
        tk.Button(self, text="修改", command=self.change_user).grid(row=7, column=2, pady=10)
        tk.Label(self, textvariable=self.status).grid(row=8, column=2, pady=10, stick=tk.E)
    def search_user(self):
        flag,info = db.search_by_username(self.name.get())
        if flag:
            self.name.set(info['name'])
            self.gender.set(info['gender'])
            self.birth.set(info['birth'])
            self.student_number.set(info['student_number'])
            self.grade.set(info['grade'])
            self.collage.set(info['collage'])
            self.phone.set(info['phone'])
            self.status.set(info['数据查询成功'])
        else:
            self.status.set(info)

        self.name.set('')
        self.gender.set('')
        self.birth.set('')
        self.student_number.set('')
        self.grade.set('')
        self.collage.set('')
        self.phone.set('')
    def change_user(self):
        stu = {"name": self.name.get(), "gender": self.gender.get(), "birth": self.birth.get(),
               "student_number": self.student_number.get(), "grade": self.grade.get(),
               "collage": self.collage.get(), "phone": self.phone.get()}
        # 清空窗口
        self.name.set('')
        self.gender.set('')
        self.birth.set('')
        self.student_number.set('')
        self.grade.set('')
        self.collage.set('')
        self.phone.set('')
        db.update(stu)
        self.status.set('修改数据成功')

class AboutFrame(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        tk.Label(self,text='关于作品：本作品由tkinter制作').pack()
        tk.Label(self,text='作者邮箱号：1907781431@qq.com').pack()

