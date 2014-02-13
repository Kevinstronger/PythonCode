#coding=UTF-8

import unittest
from selenium import webdriver
import time
from login import login
from Blog_Moudle import create_post
from Blog_Moudle import del_blog
from Blog_Moudle import add_new_post
from Blog_Moudle import edit_post


class WordPressTestCase(unittest.TestCase):
    driver = None
    login_url = 'http://localhost/wordpress/wp-login.php'
    post_list_url = 'http://localhost/wordpress/wp-admin/edit.php'
    create_post_url = 'http://localhost/wordpress/wp-admin/post-new.php'
    
    
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_1_login(self):
        login(self.driver, self.login_url)
        print self.driver.current_url
        self.assertTrue("wp-admin" in self.driver.current_url)
    
    def test_2_delete_blog(self): 
        login(self.driver, self.login_url)
        #添加文章        
        self.driver.get(self.create_post_url)
        self.subj_cont = create_post(self.driver)
        print self.subj_cont
        self.driver.get(self.post_list_url)
        table = self.driver.find_element_by_class_name("wp-list-table")
        #验证新添加的文章标题在表格内
        self.assertTrue(self.subj_cont in table.text) 
        
        #删除新增加的文章
        time.sleep(3)        
        del_blog(self.driver,self.post_list_url, self.subj_cont)
        
        #重新获取table的text
        table = self.driver.find_element_by_class_name("wp-list-table")
        self.assertFalse(self.subj_cont in table.text)

    def test_3_update_blog(self):
        login(self.driver, self.login_url)
        
            
        self.new_title = add_new_post(self.driver, self.post_list_url)
        self.driver.get(self.post_list_url)
        table = self.driver.find_element_by_class_name("wp-list-table")
        #验证新添加的文章标题在表格内
        self.assertTrue(self.new_title in table.text)
        
        #编辑文章        
        self.updated_title = edit_post(self.driver,self.post_list_url, self.new_title)
        self.driver.get(self.post_list_url)
        table = self.driver.find_element_by_class_name("wp-list-table")
        #验证新添加的文章标题在表格内
        self.assertTrue(self.updated_title in table.text)

       
        
    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()
