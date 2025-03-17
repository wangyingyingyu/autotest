python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 设置 ChromeDriver 路径
service = Service(executable_path='D:/chrome/chrome-driver/chromedriver-win64/chromedriver.exe')
options = Options()
driver = webdriver.Chrome(options=options, service=service)
driver.implicitly_wait(10)

driver.get("https://example.com")  # 替换为目标网站

# 1. 向下滚动 1000 像素
driver.execute_script("window.scrollBy(0, 1000);")

# 2. 滚动到特定元素
element = driver.find_element(By.XPATH, '元素的 XPATH')
driver.execute_script("arguments[0].scrollIntoView();", element)

# 3. 等待某个元素加载并滚动到该元素
WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, '元素的 XPATH'))
)
driver.execute_script("arguments[0].scrollIntoView();", element)

# 关闭浏览器
driver.quit()