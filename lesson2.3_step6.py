from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    #Нажать на кнопку
    browser.find_element_by_css_selector("button.btn").click()
    
    #Создать новую вкладку
    new_window = browser.window_handles[1]
    #Переключиться на новую вкладку
    browser.switch_to.window(new_window)
    
    # cчитываем значение для переменной х
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    
    # вычисляем значение функции ln(abs(12*sin(x)))
    y = calc(x)
    
    # Ввести ответ в текстовое поле.
    browser.find_element_by_id("answer").send_keys(y)
  
     
    #Нажать кнопку "Submit"
    browser.find_element_by_css_selector("button.btn").click()
    
finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
