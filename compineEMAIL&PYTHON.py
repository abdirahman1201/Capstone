from pywinauto import Application 
import os
import smtplib
import time
while True:
    app = Application(backend='uia')
    app.connect(title_re=".*Chrome.*")
    element_name="Address and search bar"
    dlg = app.top_window()

    url = dlg.child_window(title=element_name, control_type="Edit").get_value() # get url from open tab
    print(url)  

    def url_strip(url): #this function strips URLs to get parent URL
        if "http://" in url or "https://" in url:

            url = url.replace("https://", '').replace("http://", '') .replace('\"', '')
        if "/" in url:
            url = url.split('/', 1)[0]
        return url

    x = (url_strip(url)) # assigning parent website to x
    #print(x)
    a = ["www.youtube.com", "www.facebook.com", "www.instagram", "www.twitter.com", "www.reddit.com", "www.tiktok.com", "www.quora.com"]
    if x in a:
        email = 'emaildemo32@gmail.com'
        password = 'dvxddhzikurwjymh'

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
    
            smtp.login(email, password)

            subject = 'Forbidden Websites Alert' 
            body = 'An employee is visiting the following forbidden website:'  + "  " + url

            msg = f'Subject: {subject}\n\n{body}'

            smtp.sendmail(email, email, msg) 
    else:
        pass 
    time.sleep(50)