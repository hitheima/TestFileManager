import os, sys
sys.path.append(os.getcwd())

from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class FilePage(BaseAction):

    # 操作按钮
    operation_button = By.XPATH, "content-desc,操作"

    # 属性
    property_button = By.XPATH, "text,属性"

    # 刷新
    refresh_button = By.XPATH, "text,刷新"

    # 新建文件夹
    new_dir_button = By.XPATH, "text,新建文件夹"

    # 新建文件
    new_file_button = By.XPATH, "text,新建文件"

    # 全部选择
    all_select_button = By.XPATH, "text,全部选择"

    # 取消全选
    all_deselect_button = By.XPATH, "text,取消全选"

    # 添加到书签
    add_mark_button = By.XPATH, "text,添加到书签"

    # 添加快捷方式
    add_shortcut_button = By.XPATH, "text,添加快捷方式"

    # set_as_home
    set_as_home_button = By.XPATH, "text,Set,1"

    # 点击操作
    def click_operation(self):
        self.click(self.operation_button)

    # 点击属性
    def click_property(self):
        self.click(self.operation_button)

    # 刷新
    def click_refresh(self):
        self.click(self.refresh_button)

    # 新建文件夹
    def click_new_dir(self):
        self.click(self.new_dir_button)

    # 新建文件
    def click_new_file(self):
        self.click(self.new_file_button)

    # 全部选择
    def click_all_select(self):
        self.click(self.all_select_button)

    # 取消全选
    def click_all_deselect(self):
        self.click(self.all_deselect_button)

    # 添加到书签
    def click_add_mark(self):
        self.click(self.add_mark_button)

    # 添加快捷方式
    def click_add_shortcut(self):
        self.click(self.add_shortcut_button)

    # set_as_home
    def click_set_as_home(self):
        self.click(self.set_as_home_button)