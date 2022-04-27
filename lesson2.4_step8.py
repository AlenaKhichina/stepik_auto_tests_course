from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
   browser = webdriver.Chrome()
   browser.get("http://suninjuly.github.io/explicit_wait2.html")

   # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд) 
   button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
  
   #Нажать кнопку "Book"
   browser.find_element_by_id("book").click()
   browser.execute_script("window.scrollBy(0, 50);") #проскролить страницу
   
   # cчитываем значение для переменной х
   x = browser.find_element_by_id("input_value").text
    
   # вычисляем значение функции ln(abs(12*sin(x)))
   y = calc(x)
    
   # Ввести ответ в текстовое поле.
   browser.find_element_by_id("answer").send_keys(y)
  
   #Нажать кнопку "Submit"
   browser.find_element_by_id("solve").click()
 
finally:
   # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
