import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
 #chromedriver_location = "C:\Users\nsuni\OneDrive\Desktop\Selenium\webdrive\testing\Lib\site-packages\Browser\chromedriver.exe"


driver = webdriver.Chrome(r"C:\Users\nsuni\OneDrive\Desktop\Selenium\webdrive\testing\Lib\site-packages\Browser\chromedriver.exe")



# test inputs
site = "https://www.goibibo.com/"
span = "Round-trip"
source_city = "Bangalore"
destination_city = "Dubai"
departure_date = "2022-12-25" # YYYY-MM-DD
return_date = "2023-01-15"
Travellers = "2 Adults,2 Children"
travel_class = "Premium Economy"




# XPATH List of the UI elements
source_city_XPATH = '//*[@id="root"]/div[4]/div/div/div[1]/div[1]/div/div/p[1]'
dropdown_selection_XPATH = '//*[@id="root"]/div[4]/div/div/div[1]/div[3]/div/p[1]/span'
destination_XPATH = '//*[@id="root"]/div[4]/div/div/div[1]/div[2]/div/div/p[2]'
departure_date_XPATH =  '//*[@id="root"]/div[4]/div/div/div[1]/div[3]/div/p[2]'
return_date_XPATH = '//*[@id="root"]/div[4]/div/div/div[1]/div[4]/div/p[1]'
search_button_XPATH = '//*[@id="root"]/div[4]/div/div/div[3]/span'
calendar_date_XPATH = '//*[@id="root"]/div[4]/div/div/div[1]/div[3]/div[2]/div[2]/div/div/div[2]/div[1]/div[3]/div[5]/div[4]/p'
calendar_submit_button_XPATH = '//*[@id="root"]/div[4]/div/div/div[1]/div[3]/div[2]/div[3]/span[2]'
span_XPATH = '//*[@id="root"]/div[4]/div/div/ul/li[2]/span[2]'
span_radio_button_XPATH = '//*[@id="root"]/div[4]/div/div/ul/li[2]/span[1]'
travel_class_XPATH = '//*[@id="root"]/div[4]/div/div/div[1]/div[5]/div[2]/div[2]/div/div[2]/ul/li[2]'
Travellers_XPATH = '//*[@id="root"]/div[4]/div/div/div[1]/div[5]/div[2]/div[1]/div/p[1]'
travel_class_done_XPATH = '//*[@id="root"]/div[4]/div/div/div[1]/div[5]/div[2]/div[3]/a[2]'




driver = webdriver.Chrome(r"C:\Users\nsuni\OneDrive\Desktop\Selenium\webdrive\testing\Lib\site-packages\Browser\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.goibibo.com/")



# time span selection steps
round_trip = driver.find_element(By.CLASS_NAME, "fvaIwQ")
round_trip.click()
time.sleep(2)


# source_city selection steps
fly_from = driver.find_element(By.CLASS_NAME, "sc-ksdxgE dvdvQX fswF1d")
fly_from.click()
fly_from_text = driver.find_element(By.XPATH("//input[@class='Auu91c NMm5M']")).sendkeys(Keys.ENTER) #dropdown_selection_XPATH
fly_from_text.send_keys("Bengaluru")
#fly_from_text.send_keys(Keys.ENTER)

time.sleep(2)

# destination_city selection steps
fly_to = driver.find_element(By.XPATH, "//input[@class='II2One j0Ppje zmMKJ LbIaRd']").sendkeys("Dubai") #destination_XPATH)
fly_to.click()
fly_to_text = driver.find_element(By.XPATH("//input[@class='Auu91c NMm5M']")) #dropdown_selection_XPATH)
#fly_to_text.send_keys(destination_city)
#fly_to_text.send_keys(Keys.ENTER)



# departure_date selection steps
departure_date_element = driver.find_element(By.XPATH("//input[@class='RKk3r eoY5cb j0Ppje']")).sendkeys("Departure") #departure_date_XPATH)
departure_date_element.click()
time.sleep(2)
calendar_div = driver.find_element(By.XPATH("//input[@class='1kvzzbb KQqAEc']")) #calendar_date_XPATH.format(date=departure_date)
calendar_div.click()



# return_date selection steps
return_date_calendar_div = driver.find_element(By.CLASS_NAME, "fswF1d_title").sendkeys("Return") #calendar_date_XPATH.format(date=return_date))
return_date_calendar_div.click()
time.sleep(2)
calender_picker = driver.find_element(By.XPATH("//input[@class='sc-ksdxgE dvdvQX fswF1d']")) #calender
calender_picker.click()


# click on the Done button in calendar picker
submit_button = driver.find_element(By.XPATH("//input[@class='VfPpkd-vQzf8d']")).sendkeys("Done") #calendar_submit_button_XPATH
submit_button.click()



#travellers_Adults selection steps
travellers_Adults = driver.find_element(By.XPATH("//input[@class='sc-nVkyK gJWpJ']")).sendkeys("Adults") #travellers_Adults
travellers_Adults_increase_count = driver.find_element(By.XPATH("//input[@class='sc-hiwPVj eHOVna']")) #count increse
#travellers_Adults_decrease_count = driver.find_element(By.XPATH("//input[@class='sc-ehCJOs kuj1ZU']")) #count decrease
travellers_Adults_count.click()



#travellers_Children selection steps
travellers_Children = driver.find_element(By.XPATH("//input[@class='sc-nVkyK gJWpJ']")).sendkeys("Children") #travellers_Children
travellers_Children_count = driver.find_element(By.XPATH("//input[@class='sc-ehCJOs kuj1ZU']")) #count increse
#travellers_Children_decrease_count = driver.find_element(By.XPATH("//input[@class='sc-ehCJOs kuj1ZU']")) #count decrease
travellers_Children_count.click()




#Travel_class selection steps
travel_class = driver.find_element(By.XPATH("//input[@class='sc-iNGGcK gnLWKR']")).sendkeys("Premium-Economy") #class
Done_button = driver.find_element(By.XPATH("//input[@class='sc-eLwHnm hHxEGr']")).sendkeys("Done") # submit button
Done_button.click()