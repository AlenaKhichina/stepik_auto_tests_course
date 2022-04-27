from selenium import webdriver

browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element_by_tag_name("button")
button.click()
