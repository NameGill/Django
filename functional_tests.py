from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        """
        测试方法之前；若setUp异常，tearDown方法不会执行
        """
        self.browser = webdriver.Firefox()

    def tearDown(self):
        """
        测试方法之后；就算测试中出错，也会运行tearDown。即Firefox窗口不会一直停留在桌面上
        """
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """
        以test开头的均为测试方法
        """
        self.browser.get('http://localhost:8000')
        self.assertIn('successfully', self.browser.title)  # unittest的辅助函数（断言）
        self.fail('Finish the test!')  # 生成指定错误消息，提示测试结束


if __name__ == '__main__':
    unittest.main(warnings='ignore')  # 禁止抛出ResourceWarning异常
