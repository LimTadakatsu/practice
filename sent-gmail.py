#寄email程式

import email.message
msg=email.message.EmailMessage()
msg["From"]="mar55667890@gmail.com"#"寄件人地址"
msg["To"]="mar55667890@yahoo.com.tw"#"收件人"
msg["Subject"]="你好"
#寄送純文字物件
msg.set_content("測試")
# #寄送多樣式內容(Html)
msg.add_alternative("<h3>優惠券<h/3>滿五百送一百",subtype="html")
#連線SMTP server ,驗證寄件人身分發信
#搜尋 smtp server (公開資訊)
import smtplib
server=smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("mar55667890@gmail.com","Aq020202")
server.send_message(msg)
server.close()