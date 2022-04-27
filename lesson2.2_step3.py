from selenium import webdriver
import time 
import math
from selenium.webdriver.support.ui import Select

def sum(x, y):
  return str(int(x) + int(y))

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    # cчитываем значение для переменной х
    x_element = browser.find_element_by_css_selector(".container .nowrap:nth-child(2)")
    x = x_element.text
    
    # cчитываем значение для переменной y
    y_element = browser.find_element_by_css_selector(".container .nowrap:nth-child(4)")
    y = y_element.text
    
    # вычисляем значение функции сумму
    sum1 = (int(x) + int(y))

    # Выбрать в выпадающем списке значение равное расчитанной сумме
    input1 = Select(browser.find_element_by_tag_name("select"))
    input1.select_by_value(str(sum1)) # ищем элемент с суммой
        
    # Нажать на кнопку Submit
    browser.find_element_by_tag_name("button").click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
