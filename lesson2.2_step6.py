from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # cчитываем значение для переменной х
    x_element = browser.find_element_by_css_selector(".container .nowrap:nth-child(2)")
    x = x_element.text
    
    # вычисляем значение функции ln(abs(12*sin(x)))
    y = calc(x)
    
    # Ввести ответ в текстовое поле.
    browser.find_element_by_id("answer").send_keys(y)
     
    # Отметить checkbox "I'm the robot"
    browser.find_element_by_css_selector("[type='checkbox']").click()
     
    #Проскроллить страницу вниз
    browser.execute_script("window.scrollBy(0, 100);")
    
    # Выбрать radiobutton "Robots rule!"
    browser.find_element_by_css_selector("[value='robots']").click()
    
    #Нажать на кнопку Submit
    browser.find_element_by_tag_name("button").click()   

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
