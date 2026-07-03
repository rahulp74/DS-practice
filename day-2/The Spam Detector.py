# H1) The Spam Detector (Search in Stream) — Linear Search
# A cybersecurity intern at a startup is building a basic spam filter.
# Incoming emails are checked against a blacklist of known spam sender IDs.
# The blacklist has no order.
blacklist=["nnicrosoft@gmail.com","lotus65@gmail.com","1x@gmail.com"]
mailid=input()
f=False
for i in  blacklist:
    if mailid in blacklist:
        f=True
        break

if f==True:
    print("this is a spam mail")
else:
    print("mail is not a spam")
