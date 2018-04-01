import os, sys, time, pytest
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
        self.file_page.entry_dir_with_name("zzz")

        # 创建1-20.txt文件
        for i in range(20):
            self.file_page.create_file_with_name(str(i + 1) + ".txt")
            time.sleep(1)

        # 选中当前目录的所有文件
        self.file_page.select_all_file()

        # 进入sdcard
        self.file_page.entry_sdcard()

        # 进入aaa
        self.file_page.entry_dir_with_name("aaa")

        # 移动文件到当前目录
        self.file_page.move_all_select()

        # 检查当前目录是否有某个文件
        for i in range(2):
            if self.file_page.is_file_exits_with_name(str(i + 1) + ".txt"):
                print("创建成功")
                break
            else:
                print("创建失败")
                continue
        else:
            assert 1
            return
    
        assert 0
