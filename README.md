# MIS
用Tkinter制作学生信息管理系统

## LoginPage.py

用Python的tkinter模块编写的图形界面程序，实现了学生信息管理系统的登录页。代码的结构和逻辑如下：

  - 首先，导入tkinter模块，messagebox模块，db模块和MianPage模块。tkinter模块提供了GUI组件，messagebox模块提供了弹出窗口，db模块提供了操作students.json文件的函数，MianPage模块提供了主页面的类。
  - 然后，定义一个LoginPage类，继承自tk.Frame类。这个类封装了登录页面的组件和逻辑。
  - 在__init__方法中，初始化一些属性和组件：
  - self.root是主窗口对象，传入作为参数。
  - self.username和self.password是两个tk.StringVar对象，用来存储用户输入的账户和密码。
  - self.page是一个tk.Frame对象，用来容纳其他组件，并添加到主窗口中。
  - 使用tk.Label, tk.Entry和tk.Button创建一些标签，文本框和按钮，并使用grid方法将它们放置在合适的位置。其中，登录按钮绑定了self.login方法，退出按钮绑定了self.page.quit方法。
  - 在login方法中，实现登录逻辑：
  - 获取用户输入的账户和密码，并调用db.check_login函数检查是否合法。这个函数返回一个布尔值和一个消息。
  - 如果布尔值为真，说明登录成功，则销毁当前页面，并创建一个MianPage对象。这个对象是主页面的类，定义在MianPage模块中。
  - 如果布尔值为假，说明登录失败，则弹出一个警告窗口，显示消息。
- 最后，在主程序中，创建一个tk.Tk对象作为主窗口，并创建一个LoginPage对象作为初始页面。然后调用root.mainloop方法启动事件循环。

## MinaPage.py

用Python的tkinter模块编写的图形界面程序，实现了学生信息管理系统的主页面。代码的结构和逻辑如下：

  - 首先，导入tkinter模块和views模块。views模块提供了五个Frame类，分别是InsertFrame, SearchFrame, DeleteFrame, AboutFrame和ChangeFrame，用来封装不同的功能页面。
  - 然后，定义一个MianPage类，继承自tk.Tk类。这个类封装了主页面的组件和逻辑。
  - 在__init__方法中，初始化一些属性和组件：
  - self.root是主窗口对象，继承自tk.Tk类。
  - 调用self.root.title方法设置窗口标题为'学生信息管理系统 v 0.1'。
  - 调用self.root.geometry方法设置窗口大小为700x400。
  - 调用self.create_page方法创建页面组件。
  - 在create_page方法中，创建页面组件：
  - 使用views模块中的五个Frame类创建五个对象，分别是self.about_frame, self.change_frame, self.insert_frame, self.search_frame和self.delete_frame，并添加到主窗口中。这些对象分别对应关于、修改、录入、查询和删除功能的页面。
  - 创建一个tk.Menu对象作为菜单栏，并添加五个命令按钮，分别是'录入'、'查询'、'删除'、'修改'和'关于'。这些按钮分别绑定了self.show_insert, self.show_search, self.show_delete, self.show_change和self.show_about方法，用来切换显示不同的页面。
  - 将菜单栏对象赋值给主窗口的'menu'属性。
  - 在show_insert, show_search, show_delete, show_change和show_about方法中，实现页面切换逻辑：
  - 使用pack_forget方法隐藏不需要显示的页面，使用pack方法显示需要显示的页面。例如，在show_insert方法中，隐藏除了self.insert_frame之外的其他四个页面，只显示self.insert_frame页面。
  - 最后，在主程序中，创建一个MianPage对象作为主页面，并调用root.mainloop方法启动事件循环。

## views.py

这段代码是用Python的tkinter模块编写的图形界面程序，实现了学生信息管理系统的五个功能页面。代码的结构和逻辑如下：

- 首先，导入tkinter模块，ttk模块和db模块。ttk模块提供了风格化的GUI组件，db模块提供了操作students.json文件的函数。
- 然后，定义五个Frame类，分别是InsertFrame, SearchFrame, DeleteFrame, ChangeFrame和AboutFrame，用来封装不同的功能页面。
- 在每个Frame类中，定义__init__方法和create_page方法。__init__方法用来初始化一些属性和组件，create_page方法用来创建页面上的组件，并绑定相应的逻辑函数。
- 在每个逻辑函数中，实现相应的功能，如录入、查询、删除、修改和显示学生信息。调用db模块中的函数来操作数据库，并给出提示信息。
- 最后，在主程序中，导入views模块，该模块提供了MianPage类，用来封装主页面的组件和逻辑。创建一个MianPage对象作为主页面，并调用root.mainloop方法启动事件循环。

## db.py

用Python的json模块编写的，实现了一个模拟的MySQL数据库类。代码的结构和逻辑如下：

- 首先，导入json模块。json模块提供了将Python对象和JSON字符串相互转换的功能¹²³⁴⁵。
- 然后，定义一个MysqlDatabases类，模拟一个MySQL数据库。这个类有两个属性，分别是self.users和self.students，分别存储了users.json和students.json文件中的数据。这两个文件是用JSON格式存储了用户信息和学生信息的文本文件。
- 在__init__方法中，初始化两个属性：
  - 使用open函数以只读模式打开users.json和students.json文件，并读取它们的内容。
  - 使用json.loads函数将文件内容转换为Python对象，即列表或字典，并赋值给self.users和self.students。
- 在类中定义了六个方法，分别实现了不同的数据库操作：
  - check_login方法用来检查用户登录是否合法。接受用户名和密码作为参数，遍历self.users列表，如果找到匹配的用户名和密码，返回True和'登录成功'；如果找不到匹配的用户名或密码，返回False和'登录失败'。
  - all方法用来返回所有学生信息。直接返回self.students列表。
  - insert方法用来插入一条学生信息。接受一个字典作为参数，表示一条学生信息，将其追加到self.students列表中。
  - delete_by_username方法用来根据姓名删除一条学生信息。接受一个字符串作为参数，表示姓名，遍历self.students列表，如果找到匹配的姓名，从列表中移除该元素，并返回True和'删除成功'；如果找不到匹配的姓名，返回False和'用户不存在'。
  - search_by_username方法用来根据姓名查询一条学生信息。接受一个字符串作为参数，表示姓名，遍历self.students列表，如果找到匹配的姓名，返回True和该元素；如果找不到匹配的姓名，返回False和'用户不存在'。
  - update方法用来修改一条学生信息。接受一个字典作为参数，表示一条学生信息，遍历self.students列表，如果找到匹配的姓名，使用update方法更新该元素，并返回True和'修改成功'；如果找不到匹配的姓名，返回False和'用户不存在'。
- 最后，在主程序中，创建一个MysqlDatabases对象，并赋值给db变量。然后调用db.search_by_username方法查询姓名为'李某'的学生信息，并打印结果。





## users.json

登录页的测试用户及密码



## students.json

测试增删查改功能的一些数据



## 补充

重启进程之后，之前所保存的或者删除的数据会恢复默认状态，不会在json文件中显示出来



