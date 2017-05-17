import base64
import os
import sendgrid
import sys
from sendgrid.helpers.mail import *

if (len(sys.argv) < 3):
  print ("Usage :")
  print ("python %s mail@adress attachment" %  sys.argv[0])
  sys.exit()

mailto = sys.argv[1]
cert = sys.argv[2]

sg = sendgrid.SendGridAPIClient(apikey='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')

from_email = Email("errong.leng@gmail.com")
subject = "Your certificate"
to_email = Email(mailto)
print (to_email)

content = Content("text/html", "Your certificate")

with open(cert,'rb') as f:
    data = f.read()
    f.close()

certdata = base64.b64encode(data)
attachment = Attachment()
attachment.content = certdata
attachment.type = "application/x-pkcs12"
s = os.path.split(cert)
attachment.filename = s[len(s)-1]
attachment.disposition = "attachment"
attachment.content_id = "contentid"

mail = Mail(from_email, subject, to_email, content)
mail.add_attachment(attachment)

response = sg.client.mail.send.post(request_body=mail.get())

print(response.status_code)
print(response.body)
print(response.headers)
