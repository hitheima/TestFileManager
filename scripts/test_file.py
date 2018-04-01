import os, sys

import time

sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.file_page import FilePage

class TestFile:

    def setup(self):
        self.driver = init_driver()
        self.file_page = FilePage(self.driver)


    def test_first(self):

        # # 新建文件夹zzz
        # self.file_page.create_dir_with_name("zzz")
        #
        # # 新建文件夹aaa
        # self.file_page.create_dir_with_name("aaa")

        # 进入zzz
        self.file_page.entry_dir_with_name("zzz")

        # 创建1-20.txt文件
        for i in range(20):
            self.file_page.creat_file_with_name(str(i + 1) + ".txt")
            time.sleep(1)

        # 选中当前目录的所有文件

        # 回到首页

        # 移动到aaa目录中


