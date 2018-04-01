import os, sys
sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.file_page import FilePage

class TestFile:

    def setup(self):
        self.driver = init_driver()
        self.file_page = FilePage(self.driver)


    def test_first(self):

        # 新建文件夹zzz
        self.file_page.create_dir_with_name("zzz")

        # 新建文件夹aaa
        self.file_page.create_dir_with_name("aaa")
        
        # 进入zzz
        # 创建1-20.txt文件
        # 移动到aaa目录中


