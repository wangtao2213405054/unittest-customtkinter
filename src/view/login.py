# _author: Coke
# _date: 2023/7/9 18:46

import customtkinter
import tkinter.messagebox


class Login(customtkinter.CTkFrame):
    """ 登录页面 """

    def __init__(self, master: any):
        """
        创建一个新的登录页面对象
        :param master: 主窗口对象
        """
        super(Login, self).__init__(master)
        self.pack(pady=40, padx=120, fill="both", expand=True)

        # Title
        self.title = customtkinter.CTkLabel(
            master=self,
            width=120,
            height=32,
            text="登  录",
            font=customtkinter.CTkFont(size=24)
        )
        self.title.pack(pady=12, padx=10)

        # Username
        self.username = customtkinter.CTkEntry(master=self, width=240, height=32, placeholder_text="用户名")
        self.username.pack(pady=12, padx=10)

        # Password
        self.password = customtkinter.CTkEntry(master=self, width=240, height=32, placeholder_text="密码", show="*")
        self.password.pack(pady=12, padx=10)

        # Login Button
        self.login = customtkinter.CTkButton(
            master=self,
            width=240,
            height=32,
            text="登 录",
            command=self.login_callback
        )
        self.login.pack(pady=12, padx=10)

        # Remember the Password
        self.remember_password = customtkinter.CTkCheckBox(master=self, text="记住密码")
        self.remember_password.pack(pady=12, padx=10)

    def login_callback(self):
        """
        登录按钮回调事件
        :return:
        """
        username = self.username.get()
        password = self.password.get()

        # da = customtkinter.CTkInputDialog()
        # da.mainloop()
        self.options = {'parent': self, 'icon': 'question', 'type': 'okcancel', 'title': '温馨提示', 'message': '请输入用户名和密码'}
        self.tk.call('tk_messageBox', *self._options(self.options))
        # if not all([username, password]):
        #     tkinter.messagebox.askokcancel('温馨提示', '请输入用户名和密码', parent=self)

    def _canned_remember_data(self):
        """
        将用户名和密码数据存储入库
        :return:
        """
        if self.remember_password.get():
            pass
