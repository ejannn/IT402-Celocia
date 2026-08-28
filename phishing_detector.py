sender = "support@school-security.example"

subject = "URGENT: Account Verification Required"

email_body = """ Dear Student,

Your school account requires verification.
Please click the link below and enter your password immediately.
Your account may be suspended if you do not verify it.

Thank you,
School Security Team """

suspicious_words = [
    "urgent",
    "verify", 
    "password",
    "click",
    "suspend",
    "immediately",
]

print("PHISHING EMAIL DETECTOR")
print()
print("sender:")
print(sender) 
print()
print("subject:")
print()
print("Message:")
print(email_body)

print("SUSPICIOS INDICATORS")
print()

email_text = email_body.lower()

score = 0

for word in suspicious_words:
    if word in email_text:
        print("[!]"  + word)
        score += 1

if score <= 1:
    risk_level = "LOW"
elif score <=3:
    risk_level = "MEDIUM"
else:
    risk_level = "HIGH"

print("RISK SCORE" , score)
print("RISK LEVEL" , risk_level)




