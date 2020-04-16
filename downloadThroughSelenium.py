from selenium import webdriver

driver = webdriver.Chrome(executable_path = r'C:\Program Files\chromedriver.exe')

# LOADING THE PAGE
driver.get('https://www.pagalworld.mobi/')
driver.maximize_window()
# SEARCHING QUERY FOR SONGS
search_Bar = driver.find_element_by_xpath('//*[@id="gsc-i-id1"]').send_keys(Song_name)

search_Button = driver.find_element_by_xpath('//*[@id="___gcse_0"]/div/div/form/table/tbody/tr/td[2]/button')
driver.implicitly_wait(10)
search_Button.click()

# SELECTING SONG PAGE
song_Link = driver.find_element_by_xpath(
    '//*[@id="___gcse_0"]/div/div/div/div[5]/div[2]/div/div/div[1]/div[1]/div[1]/div[1]/div/a')
# GETTING LINK OF THE TOP MOST SONG
downlod_page_link = song_Link.get_attribute('href')

# SEARCHING FOR THE SONG DOWNLOAD PAGE
driver.get(downlod_page_link)

# DOWNLOADING THE SONG
dowload_song = driver.find_element_by_xpath('/html/body/main/div/div[2]/div/a/span')
driver.implicitly_wait(10)
dowload_song.click()
