import os, sys, time, pytest
sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.file_page import FilePage


class TestFile:

    def setup(self):
        self.driver = init_driver()
        self.file_page = FilePage(self.driver)

    @pytest.mark.skipif(True, reason="done")
    def test_refresh(self):
        self.file_page.entry_sdcard()
        dir_name = self.file_page.get_current_dir_first_file_name()
        self.file_page.scroll_page_onetime()
        after_refresh_dir_name = self.file_page.get_current_dir_first_file_name()
        if after_refresh_dir_name == dir_name:
            assert 0, "没有滑动成功"
        self.file_page.click_operation()
        self.file_page.click_refresh()
        after_refresh_dir_name = self.file_page.get_current_dir_first_file_name()
        assert after_refresh_dir_name == dir_name

    @pytest.mark.skipif(True, reason="done")
    def test_property(self):
        self.file_page.entry_sdcard()
        # 获取当前目录名字
        current_dir_name = self.file_page.get_current_dir_name()
        current_property_dir_name = self.file_page.get_current_property_dir_name()
        assert current_dir_name == current_property_dir_name

    @pytest.mark.skipif(True, reason="done")
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
                break
            else:
                continue
        else:
            assert 1
            return

        assert 0, "没有重名的文件，说明没有检测到条件需要的文件"
