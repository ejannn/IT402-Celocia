

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


credential_words = [
    "password",
    "login",
    "credentials",
    "account information",
    "username"
]

reward_words = [
    "you won",
    "winner",
    "prize",
    "reward",
    "cash",
    "congratulations"
]

urgency_words = [
    "today",
    "immediately",
    "urgent",
    "act now",
    "deadline",
    "expires"
]

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




credential_detected = False

for word in credential_words:
    if word in email_text:
        credential_detected = True
        break

if credential_detected:
    print("[!] Credential request detected")
    score += 2




reward_detected = False

for word in reward_words:
    if word in email_text:
        reward_detected = True
        break

if reward_detected:
    print("[!] Reward/prize language detected")
    score += 2




if "[link]" in email_text or "http://" in email_text or "https://" in email_text:
    print("[!] Suspicious link detected")
    score += 2




urgency_detected = False

for word in urgency_words:
    if word in email_text:
        urgency_detected = True
        break

if urgency_detected:
    print("[!] Urgency/deadline pressure detected")
    score += 1



if score <= 2:
    risk_level = "LOW"
elif score <= 5:
    risk_level = "MEDIUM"
else:
    risk_level = "HIGH"



if risk_level == "HIGH":
    recommendation = "Do not click links or provide information. Verify the sender through a trusted channel."
elif risk_level == "MEDIUM":
    recommendation = "Be cautious. Verify the sender and message before taking action."
else:
    recommendation = "No major warning signs detected, but continue to verify unexpected messages."


print()
print("RISK SCORE:", score)
print("RISK LEVEL:", risk_level)
print("RECOMMENDATION:", recommendation)