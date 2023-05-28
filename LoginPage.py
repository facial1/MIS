import tkinter as tk
from tkinter import messagebox
from db import db
from MinaPage import MianPage

"""
这是用tkinter编写的图形界面程序，实现了学生信息的录入、查询、删除和修改等功能。
程序的结构是使用了多个Frame类来封装不同的页面，然后在主窗口中切换显示。
程序的逻辑是使用了db模块来操作students.json文件，存储和读取学生信息。
程序的界面是使用了tkinter和ttk模块提供的组件，如Label, Entry, Button, Treeview等，来展示和输入数据。
"""

    #初始页面参数
class LoginPage:

    def __init__(self,master):
        self.root = master
        self.root.geometry('300x200')
        self.root.title('登录页')

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        self.page = tk.Frame(root)
        self.page.pack()

        tk.Label(self.page).grid(row=0, column = 0)

        tk.Label(self.page,text='账户').grid(row= 1, column =1)
        tk.Entry(self.page,textvariable=self.username).grid(row = 1, column = 2)

        tk.Label(self.page,text='密码').grid(row = 2, column = 1)
        tk.Entry(self.page,textvariable=self.password).grid(row = 2,column = 2)

        tk.Button(self.page, text='登录',command=self.login).grid(row = 3, column = 1,pady=20)
        tk.Button(self.page, text='退出',command=self.page.quit).grid(row = 3, column =2, pady=20)


    def login(self):
            name = self.username.get()
            pwd = self.password.get()
            flag, message = db.check_login(name, pwd)
            if flag:
                self.page.destroy()
                MianPage(self.root)
            else:
                messagebox.showwarning(title='警告', message='登陆失败，检查账号密码')




if __name__ =='__main__':
    root = tk.Tk()
    LoginPage(master=root)
    root.mainloop()
