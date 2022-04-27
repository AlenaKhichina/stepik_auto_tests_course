from selenium import webdriver
import time 



try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/wait1.html")
    
    time.sleep(1)
    button = browser.find_element_by_id("verify")
    button.click()
    message = browser.find_element_by_id("verify_message")
    assert message.text == "Verification was successful!"
   #assert "successful" in message.text
    
finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
