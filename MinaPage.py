import tkinter as tk
from views import InsertFrame,SearchFrame,DeleteFrame, AboutFrame,ChangeFrame

    #跳转页面参数
class MianPage:
    def __init__(self,master:tk.Tk):
        self.root = master
        self.root.title('学生信息管理系统 v 0.1')
        self.root.geometry('700x400')
        self.create_page()

    def create_page(self):
        self.about_frame = AboutFrame(self.root)
        self.change_frame = ChangeFrame(self.root)
        self.insert_frame = InsertFrame(self.root)
        self.search_frame = SearchFrame(self.root)
        self.delete_frame = DeleteFrame(self.root)

        menubar = tk.Menu(self.root)
        menubar.add_command(label='录入',command=self.show_insert)
        menubar.add_command(label='查询',command=self.show_search)
        menubar.add_command(label='删除',command=self.show_delete)
        menubar.add_command(label='修改',command=self.show_change)
        menubar.add_command(label='关于',command=self.show_about)
        self.root ['menu'] = menubar

    def show_insert(self):
        self.about_frame.pack_forget()
        self.change_frame.pack_forget()
        self.insert_frame.pack()
        self.search_frame.pack_forget()
        self.delete_frame.pack_forget()

    def show_search(self):
        self.about_frame.pack_forget()
        self.change_frame.pack_forget()
        self.insert_frame.pack_forget()
        self.search_frame.pack()
        self.delete_frame.pack_forget()

    def show_delete(self):
        self.about_frame.pack_forget()
        self.change_frame.pack_forget()
        self.insert_frame.pack_forget()
        self.search_frame.pack_forget()
        self.delete_frame.pack()

    def show_change(self):
        self.about_frame.pack_forget()
        self.change_frame.pack()
        self.insert_frame.pack_forget()
        self.search_frame.pack_forget()
        self.delete_frame.pack_forget()

    def show_about(self):
        self.about_frame.pack()
        self.change_frame.pack_forget()
        self.insert_frame.pack_forget()
        self.search_frame.pack_forget()
        self.delete_frame.pack_forget()

if __name__ == '__main__':
    root = tk.Tk()
    MianPage(root)
    root.mainloop()
