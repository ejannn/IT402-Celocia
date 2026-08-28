sender = "support@school-security.example"

subject = "URGENT: Account Verification Required"

email_body = """ Dear Student,

Your school account requires verification.
Please verify your account to avoid interruption of access.

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

for word in suspicious_words:
    if word in email_text:
        print("[!]"  + word)