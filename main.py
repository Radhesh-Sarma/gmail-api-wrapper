from email_sender import send_mail

# Add your processing code here



# We are using a dict to store mail info
mail = {}

mail['sender'] = 'youremail' # Put Sender's Email here
mail['reciever'] = 'recipient email' # Put recipient Email here
mail['subject'] = 'demo-subject'
mail['body'] = 'demo-body'

# Provide the full path of attachment file to be attached below
mail['file'] = 'Put full path of attachemnt here ' # Put the integer zero in case there is no attachment

# call send_mail function and pass the dict
send_mail(mail)