import webbrowser 
chromePath = r'C://Program Files//Google//Chrome//Application//chrome.exe'   # 例如我的：D:\Google\Chrome\Application\chrome.exe 
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath)) #這裡的'chrome'可以用其它任意名字，如chrome111，這裡將想開啟的瀏覽器儲存到'chrome' 

web = 'https://www.youtube.com/'
webbrowser.get('chrome').open(web,new=3) 