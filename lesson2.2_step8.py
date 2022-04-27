from selenium import webdriver
import time 
import os # импортируем модуль

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    # заполняем текстовые поля: имя, фамилия, email    
    browser.find_element_by_name("firstname").send_keys("Ivan")
    browser.find_element_by_name("lastname").send_keys("Petrov")
    browser.find_element_by_css_selector("[placeholder='Enter email']").send_keys("Ivan@pochta.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
  
    #Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    browser.find_element_by_css_selector("[type='file']").send_keys(file_path)
  
     
    #Нажать кнопку "Submit"
    browser.find_element_by_css_selector("button.btn").click()
    
finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
