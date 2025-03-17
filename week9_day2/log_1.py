def test_logging():
    # 实例化driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    # 打开百度首页
    driver.get("https://www.baidu.com")
    logging.info("打开百度首页")
    # 输入霍格沃兹测试学院
    driver.find_element(By.CSS_SELECTOR, "#kw").send_keys("霍格沃兹测试学院")
    logging.info("输入霍格沃兹测试学院")
    # 点击搜索
    driver.find_element(By.CSS_SELECTOR, "#su").click()
    logging.info("点击搜索")
    time.sleep(3)
    driver.quit()


# 步骤截图
def test_screenshot():
    # 实例化driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    # 打开百度首页
    driver.get("https://www.baidu.com")
    driver.get_screenshot_as_file(f"./screenshot/打开百度首页.png")
    # 输入霍格沃兹测试学院
    driver.find_element(By.CSS_SELECTOR, "#kw").send_keys("霍格沃兹测试学院")
    driver.get_screenshot_as_file(f"./screenshot/输入霍格沃兹测试学院.png")
    # 点击搜索
    driver.find_element(By.CSS_SELECTOR, "#su").click()
    driver.get_screenshot_as_file(f"./screenshot/点击搜索.png")
    time.sleep(3)
    driver.quit()

   # page_source记录
def test_page_source():
    # 实例化driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    # 打开百度首页
    driver.get("https://www.baidu.com")
    # 打印页面信息
    print(driver.page_source)
    # 输入霍格沃兹测试学院
    driver.find_element(By.CSS_SELECTOR, "#kw").send_keys("霍格沃兹测试学院")
    # 点击搜索
    driver.find_element(By.CSS_SELECTOR, "#su").click()
    time.sleep(3)
    driver.quit()