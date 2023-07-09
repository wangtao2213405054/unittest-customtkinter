# _author: Coke
# _date: 2023/7/9 18:28

from view.login import Login

import customtkinter
import logging
import utils

customtkinter.set_appearance_mode("Dark")  # 设置主题颜色: "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # 设置组件风格: "blue" (standard), "green", "dark-blue"


class APP(customtkinter.CTk):
    """ 应用程序主要入口 """

    WIDTH = 600
    HEIGHT = 450
    APPNAME = '自动化测试工具'

    def __init__(self):
        super(APP, self).__init__()
        utils.logger(utils.DEBUG)
        self.set_windows()
        self.login = Login(self)

    def set_windows(self):
        """ 设置窗口信息 """
        self.title(self.APPNAME)
        self.geometry(f'{self.WIDTH}x{self.HEIGHT}')
        self.minsize(self.WIDTH, self.HEIGHT)
        logging.debug(
            f'设置窗口 Title 为 {self.APPNAME}'
            f'初始化窗口宽高: {self.WIDTH} x {self.HEIGHT}'
            f'窗口最低宽高为: {self.WIDTH} x {self.HEIGHT}'
        )


if __name__ == '__main__':
    app = APP()
    app.mainloop()
