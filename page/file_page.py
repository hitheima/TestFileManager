import os, sys

from selenium.common.exceptions import TimeoutException

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

    # first_edit_text
    first_deit_text = By.CLASS_NAME, "android.widget.EditText"

    # 名称已经存在
    name_already_exist = By.XPATH, "text,已存在,1"

    # xpath 确实
    ok_button = By.XPATH, "text,确定"

    # xpath 取消
    cancel_button = By.XPATH, "text,取消"

    # 侧边栏按钮
    side_menu_button = By.ID, "android:id/home"

    # 内部存储设备
    sdcard_button = By.XPATH, "text,内部存储设备"

    # 移动选择项
    move_all_select_button = By.XPATH, "text,移动选择项"

    # 当前目录名字的item
    current_dir_items = By.ID, "com.cyanogenmod.filemanager:id/breadcrumb_item"

    # 当前目录名字的item
    current_property_dir_name = By.ID, "com.cyanogenmod.filemanager:id/fso_properties_name"

    # 点击操作
    def click_operation(self):
        self.click(self.operation_button)

    # 点击属性
    def click_property(self):
        self.click(self.property_button)

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

    # 清空文本框内容，并输入文字
    def input_first_edit_text(self, text):
        self.clear_text(self.first_deit_text)
        self.input_text(self.first_deit_text, text)

    # 根据文件名新建文件
    def create_dir_with_name(self, dir_name):
        self.click_operation()
        self.click_new_dir()
        self.input_first_edit_text(dir_name)
        try:
            self.find_element(self.name_already_exist)
        except TimeoutException:
            self.click(self.ok_button)
            return True
        self.click(self.cancel_button)
        self.click(self.cancel_button)
        return False

    def create_file_with_name(self, file_name):
        self.click_operation()
        self.click_new_file()
        self.input_first_edit_text(file_name)
        try:
            self.find_element(self.name_already_exist)
        except TimeoutException:
            self.click(self.ok_button)
            return True
        self.click(self.cancel_button)
        self.click(self.cancel_button)
        return False

    def entry_dir_with_name(self, dir_name):
        loc = By.XPATH, "text," + dir_name
        self.scroll_page_until_loc(loc)
        self.click(loc)

    def select_all_file(self):
        self.click_operation()
        self.click_all_select()

    def entry_sdcard(self):
        self.click(self.side_menu_button)
        self.click(self.sdcard_button)

    def move_all_select(self):
        self.click_operation()
        self.click(self.move_all_select_button)

    def is_file_exits_with_name(self, file_name):
        return self.create_file_with_name(file_name)

    def get_current_dir_name(self):
        items = self.find_elements(self.current_dir_items)
        last_index = len(items) - 1
        return items[last_index].get_attribute("text")

    def get_current_property_dir_name(self):
        # 点击菜单
        self.click_operation()
        # 点击属性
        self.click_property()
        return self.find_element(self.current_property_dir_name).get_attribute("text")


