def login(driver, login_url):
    driver.get(login_url)
    driver.find_element_by_name('log').send_keys('admin')
    driver.find_element_by_name('pwd').send_keys('123456')
    driver.find_element_by_name('wp-submit').click()