import email.message as email

# 設定基本郵件資訊
msg = email.EmailMessage()
msg["fromEmail"]="emailAddress"
msg["toEmail"]="emailAddress"
msg["Subject"]="你好,66"
# 寄送純文字內容
msg.set_content("test")
# # 寄送多樣式內容
# msg.add_alternative("<h3>優惠券<h3>滿五百送一百", subtype="html")
# 連線 SMTP server 驗證寄件人身分後發送郵件
import smtplib as smtp

server=smtp.SMTP_SSL("smtp.gmail.com", 465)
server.login("account","password")
server.send_message(msg)
server.close()