from selenium import webdriver

driver = webdriver.Firefox(executable_path=r'./driver/geckodriver.exe')
driver.get("https://www.worldometers.info/coronavirus/")

# Last Update
el = driver.find_element('xpath', '/html/body/div[2]/div[2]/div[1]/div/div[2]')
print(el.get_property("innerHTML"))

#Corona Virus Case, Deaths , Recovered
label = driver.find_elements_by_xpath('//div[@class="maincounter-number"]/span')
label_list1 = []
for s in range(len(label)):
    label_list1.append(label[s].text)
print(label_list1)    


#Currently Infected Patients , Cases which had an outcome:
label2 = driver.find_elements_by_xpath('//div[@class="number-table-main"]')
label_list2 = []
for s in range(len(label2)):
    label_list2.append(label2[s].get_property("innerHTML"))
print(label_list2)    



# in Mild Condition , Serious or Critical , Recovered / Discharged, Deaths
label3 = driver.find_elements_by_xpath('//span[@class="number-table"]')
label_list3 = []
for s in range(len(label3)):
    label_list3.append(label3[s].get_property("innerHTML"))
print(label_list3)    




driver.close()