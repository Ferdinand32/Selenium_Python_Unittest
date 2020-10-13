from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 


page = webdriver.Chrome() # Создаем страницу браузера через драйвер
page.set_window_size(1900, 1200)  # Задаем размер окна
page = page
print('Заходим на страницу Яндекс')
try:
    page.get("https://yandex.ru/") #заходим на страницу Яндекс
except:
    print('Ошибка при заходе в Яндекс')
    assert False
    page.close()
print('Начинаем поиск по искомой посиковой фразе')
try:
    page.find_element_by_id('text12321').send_keys('расчет расстояний между городами') #Ищем поисковую строку и вводим туда поисковую фразу. Ищем по id. Лучше искать по xpath, но тут есть уникальный и постоянный id
except:
    print('Отсутвует поисковая строка') 
    assert False
    page.close()
try:
    page.find_element_by_class_name('button_theme_websearch').click() #Жмем на кнопку поиска
except:
    print('Отсутвует кнопка поиска')
    assert False
    page.close()  
print('Ждем загрузки страницы поиска')
wait  = WebDriverWait(page, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@id='search-result']/li[2]/div"))) #Ждем пока появятся результаты поиска
try:
    serch_result = page.find_elements_by_class_name('link_theme_outer') #Сохраняем все названия страниц результатов поиска в переменную
except:
    print('Ошибка поисквой выдачи. Яндекс не вернул результаты')
    assert False
    page.close() 
i = 0
error = 1
print('Поиск искомога результата в поисковой выдаче') 
while i < len(serch_result): #Ищем среди результатов искомый и кликаем на него. При масштабном тестировании такое заносится в функцию в отдельном файле
    if 'avtodispetcher.ru' in serch_result[i].text:
        serch_result[i].click()
        time.sleep(2)
        error = 0
        print('Переход на искомый сайт') 
        break
    i += 1
if error == 1:
    print('На первой странице Яндекс нет искомого сайта') 
page.switch_to_window(page.window_handles[1]) #Переключаемся на новую вкладка браузера, т.к. Яндекс открывает новую при переходе из поиска
print('Проверка URL страницы')
try:
    assert 'avtodispetcher.ru/distance/' in page.current_url #Проверяем, что мы на нужной странице
except:
    print('URL страницы не соответсвует эталонному')
     
page.execute_script("window.scrollTo(0, 500)") #Скроллим вниз на 500 пикселей
print('Вводим данные в поля калькулятора')
try:
    page.find_element_by_xpath("//*[@id='from_field_parent']/input").send_keys('Тула') 
except:
    print('Отсутствует поле Откуда')
    assert False
    page.close() 
try:
    page.find_element_by_xpath("//*[@id='to_field_parent']/input").send_keys('Санкт-Петербург')
except:
    print('Отсутствует поле Куда')
    assert False
    page.close()  
try:
    page.find_element_by_xpath("//*[@id='CalculatorForm']/div[2]/div[1]/label/input").clear()
    page.find_element_by_xpath("//*[@id='CalculatorForm']/div[2]/div[1]/label/input").send_keys('9')
except:
    print('Отсутствует поле Расход топива')
    assert False
    page.close() 
try:
    page.find_element_by_xpath("//*[@id='CalculatorForm']/div[2]/div[2]/label/input").clear()
    page.find_element_by_xpath("//*[@id='CalculatorForm']/div[2]/div[2]/label/input").send_keys('46')
except:
    print('Отсутствует поле Стоимость топива')
    assert False
    page.close() 
print('Ожидание - 1 минута')
time.sleep(60) #Ждем минуту
print('Жмем на кнопку рассчитать')
try:
    page.find_element_by_xpath("//*[@id='CalculatorForm']/div[3]/input").click() 
except:
    print('Кнопка рассчитать не найдена')
    assert False
    page.close() 
wait  = WebDriverWait(page, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@id='summaryContainer']/p"))) #Ждем пока появятся результаты 
print('Проверяем результат вычислений')
try:
    assert 'Расстояние: 897 км' in page.find_element_by_xpath("//*[@id='summaryContainer']/p").text #Финальная проверка результата 
except:
    print('Ошибка при расчете расстояния') 
page.close()




