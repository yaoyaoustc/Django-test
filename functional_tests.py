from selenium import webdriver

brower = webdriver.Chrome()
brower.get('http://localhost:8020')

assert 'Django' in brower.title