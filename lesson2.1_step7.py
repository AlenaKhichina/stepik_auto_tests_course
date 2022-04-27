from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    # cчитываем значение для переменной х
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    # вычисляем значение функции ln(abs(12*sin(x)))
    y = calc(x)

    # Ввести ответ в текстовое поле.
    input1 = browser.find_element_by_css_selector(".form-group .form-control")
    input1.send_keys(y)
    
    # Отметить checkbox "I'm the robot"
    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
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
