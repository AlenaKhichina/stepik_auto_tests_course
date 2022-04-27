from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    # cчитываем значение для переменной х под картинкой с сундуком
    x_element = browser.find_element_by_css_selector("div.form-group img")
    x = x_element.get_attribute("valuex")
    
    # вычисляем значение функции ln(abs(12*sin(x)))
    y = calc(x)

    # Ввести ответ в текстовое поле.
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    
    # Отметить checkbox "I'm the robot"
    option1 = browser.find_element_by_css_selector("[type='checkbox']")
    option1.click()
    
    # Выбрать radiobutton "Robots rule!"
    option2 = browser.find_element_by_css_selector("[value='robots']")
    option2.click()
    
    # Нажать на кнопку Submit
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
