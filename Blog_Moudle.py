#coding=UTF-8
from selenium import webdriver
import time

def create_post(driver):
    subj_con = "Post testing" + str(time.time())
    driver.find_element_by_name('post_title').send_keys(subj_con)
    js = "document.getElementById('content_ifr').contentWindow.document.body.innerHTML='" +subj_con+"'"
    print js
    driver.execute_script(js)
    driver.find_element_by_name('publish').click()
    return subj_con

def del_blog(driver,post_list_url, subj_con):
    driver.get(post_list_url)
    webdriver.ActionChains(driver).move_to_element(driver.find_element_by_xpath("//a[text()='"+subj_con+"']")).perform()
    driver.find_element_by_xpath("//a[text()='"+subj_con+"']/ancestor::td[1]//a[text()='移至回收站']").click()
    #driver.find_element_by_xpath("//a[contains(.,'移至回收站')]").click()

def add_new_post(driver,post_list_url):
    driver.get(post_list_url)
    driver.find_element_by_class_name("add-new-h2").click()
    return create_post(driver)
    
def edit_post(driver,post_list_url, subj_con):
    driver.get(post_list_url)
    webdriver.ActionChains(driver).move_to_element(driver.find_element_by_xpath("//a[text()='"+subj_con+"']")).perform()
    driver.find_element_by_xpath("//a[text()='"+subj_con+"']/ancestor::td[1]//a[text()='编辑']").click()   
    #更新标题
    update_title = "Updating_" +str(time.time())
    driver.find_element_by_name('post_title').clear()
    driver.find_element_by_name('post_title').send_keys(update_title)
    driver.find_element_by_id('publish').click()
    return update_title