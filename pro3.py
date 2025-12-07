# QR code miking using py
import qrcode 
upi_id = input("emter your upi_id =")
#url formet
#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENTCY&tn=MESSAGE
# pa = receiver id ,pn= sender id ,am= amount , cu = inr etc , tn= message u want to print

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20NAME&mc=1234' 
pytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20NAME&mc=1234' 
goggle_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20NAME&mc=1234' 

phonepe_qr = qrcode.make(phonepe_url)
goggle_pay_qr = qrcode.make(goggle_pay_url)
pytm_qr = qrcode.make(pytm_url)

# save in image
phonepe_qr.save('phonepe_qr.png')
pytm_qr.save('pytm_qr.png')
goggle_pay_qr.save('goggle_pay_qr.png')

# display
phonepe_qr.show()
pytm_qr.show()
goggle_pay_qr.show()

