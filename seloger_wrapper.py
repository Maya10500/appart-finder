from seloger import seloger

wrapper = seloger.Seloger()
wrapper.get_url("https://www.seloger.com/")
#wrapper.do_research()
wrapper.enter_value('//*[@id="agatha_autocomplete_autocompleteUI__input"]','Lyon')
wrapper.enter_value('//*[@id="agatha_budget"]/input', 900000)
wrapper.click('//*[@id="agatha_actionbuttons"]/div/div[2]/label/a')
wrapper.get_all()
#wrapper.click('//*[@id="agatha_actionbuttons"]/div/div[2]/label/a')