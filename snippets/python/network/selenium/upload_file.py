el = driver.find_element_by_xpath("//*[contains(text(), '???')]")
el.send_keys('/path/to/file')
driver.find_element_by_xpath("//*[contains(text(), '???')]").click()
