import smtplib, ssl
import configparser
import os
import csv


from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage


#
# Take email list and his size from folder Data/email.csv
#
def get_email_list(email_list_path):

    data_email=[]
    size = 0
    
    # This folder not changed
    with open(email_list_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # print(row['email'])
            size = size + len(row['email'].split('\n'))
            data_email.append(row['email'].split('\n'))
            
        return size, data_email
    
        

#
# Take Image name from folder and his size
#
def take_image_name_and_size():
   
    files_list=os.listdir('img')
    size = len(files_list)
    return size, files_list



def send_email(sender_email, receiver_email, bcc, subject, smtp_server, port, attack_file):
    
    # Create the root message 

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = subject
    msgRoot['From'] =  sender_name + "<"+sender_email+">"
    msgRoot['To'] = receiver_email
    msgRoot['Bcc'] = bcc_address # Отчеть или скрытая копия

    msgRoot.preamble = 'Multi-part message in MIME format.'

    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    msgText = MIMEText('Alternative plain text message.')
    msgAlternative.attach(msgText)

    msgText = MIMEText('<img src="cid:image1">', 'html')
    msgAlternative.attach(msgText)

    #Attach Image 
    fp = open(attack_file, 'rb') #Read image 
    msgImage = MIMEImage(fp.read())
    fp.close()

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)


    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        # server.sendmail(sender_email, receiver_email, msgRoot.as_string())
        server.send_message(msgRoot)
        server.quit()



if __name__ == "__main__":

    # Read config file
    config = configparser.RawConfigParser()
    config.read('config.cfg')
    details_dict = dict(config.items('EMAIL_SETTINGS'))

    # Config Varibles
    port = details_dict['port']
    smtp_server = details_dict['smtp_server']
    sender_email = details_dict['email_address']  # Your address
    password = details_dict['email_password']
    sender_name = details_dict['sender_name']
    bcc_address = details_dict['bcc_address']
    subject = details_dict['subject']

    ### Data Varibles
    image_path = details_dict['image_path']
    email_list_path = details_dict['email_list_path']

    print(email_list_path)


    size, data_email = get_email_list(email_list_path)

    print(size)
    print(data_email)

   
    #while size > 0:

        #receiver_email = ",".join(map(str, data_email[size - 1]))

        # send_email// receiver_email// bcc// smtp// port
        # send_email(sender_email, receiver_email, bcc_address, subject, smtp_server, port, image_path)
        say, adlar = take_image_name_and_size()
        print(say, adlar)
        #print(receiver_email)
        #size-=1 
       
    
  
