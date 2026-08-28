email = {
    "sender": "maria.santos@university-example.edu",
    "subject": "ITE 403 — Missing Activity",
    "body": """
Hi Alvin,

I'm checking the submissions for our ITE 403 class.

Your Week 5 activity appears to be missing from the submission list.

Please review your submission here:

[LINK]

I need to finalize the grades today.

Thank you,
Dr. Maria Santos
"""
}

suspicious_words = [
    "urgent",
    "verify",
    "password",
    "click",
    "suspended",
    "immediately"
]


victim_name = "Alvin"
course = "ITE 403"

email_text = (
    email["sender"] + " " +
    email["subject"] + " " +
    email["body"]
).lower()

score = 0

print("PHISHING EMAIL DETECTOR")
print()
print("Sender:", email["sender"])
print("Subject:", email["subject"])
print("Message:")
print(email["body"])

print("SUSPICIOUS INDICATORS")
print()


for word in suspicious_words:
    if word in email_text:
        print("[!] Suspicious word:", word)
        score += 1

if victim_name.lower() in email_text:
    print("[!] Personalization: victim's name detected")
    score += 1


if course.lower() in email_text:
    print("[!] Academic targeting: specific course detected")
    score += 1


if score <= 1:
    risk_level = "LOW"
elif score <= 3:
    risk_level = "MEDIUM"
else:
    risk_level = "HIGH"

print()
print("RISK SCORE:", score)
print("RISK LEVEL:", risk_level)