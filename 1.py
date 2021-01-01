from selenium import webdriver
i=5747

while i < 6000:
    j = str(i)
    driver = webdriver.Chrome()
    url = ('https://sppu.wheebox.com/WAC-3/allqusdownloadhtml.ils?testNo='+j+'&code=1052000&showTest=319&actForm=edit&set=2')
    driver.get(url)
    driver.refresh()
    try:
        name = driver.find_element_by_class_name('row')
        a = name.text

        b = a.splitlines()

        print(i, b[2])
    except:
        print(i,'IndexOutOfBound')
    i=i+1

    driver.__exit__()