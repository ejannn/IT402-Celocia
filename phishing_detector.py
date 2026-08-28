import re


legit_domain = "university-example.edu"
 
email = {
    "sender": "maria.santos@university-example.edu",
    "subject": "ITE 403 \u2014 Missing Activity",
    "body": """
Hi Alvin,
 
I'm checking the submissions for our ITE 403 class.
 
Your Week 5 activity appears to be missing from the submission list.
 
Please review your submission here:
 
https://ite403-submission-portal.net/upload
 
I need to finalize the grades today.
 
Thank you,
Dr. Maria Santos
"""
}
 
victim_name = "Alvin"
course = "ITE 403"
 
suspicious_words = [
    "urgent",
    "verify",
    "password",
    "click",
    "suspended",
    "immediately"
]
 
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
indicators = []
 

 
for word in suspicious_words:
    if word in email_text:
        indicators.append("Suspicious word detected: " + word)
        score += 1
 
if victim_name.lower() in email_text:
    indicators.append("Personalization: victim's name detected")
    score += 1
 
if course.lower() in email_text:
    indicators.append("Academic targeting: specific course detected")
    score += 1
 
credential_detected = False
for word in credential_words:
    if word in email_text:
        credential_detected = True
        break
 
if credential_detected:
    indicators.append("Credential request detected")
    score += 2
 
reward_detected = False
for word in reward_words:
    if word in email_text:
        reward_detected = True
        break
 
if reward_detected:
    indicators.append("Reward/prize language detected")
    score += 2
 
link_detected = False
links_found = re.findall(r"https?://[^\s]+", email["body"])
if "[link]" in email_text or len(links_found) > 0:
    link_detected = True
    indicators.append("Suspicious link detected")
    score += 2

domain_mismatch = False
for link in links_found:
    match = re.search(r"https?://([^/]+)", link)
    if match:
        link_domain = match.group(1)
        if legit_domain not in link_domain:
            domain_mismatch = True
            indicators.append(
                "Link domain does not match sender's official domain ("
                + link_domain + " vs " + legit_domain + ")"
            )
            score += 2
 
urgency_detected = False
for word in urgency_words:
    if word in email_text:
        urgency_detected = True
        break
 
if urgency_detected:
    indicators.append("Urgency/deadline pressure detected")
    score += 1
 

 
if score <= 2:
    risk_level = "LOW"
elif score <= 5:
    risk_level = "MEDIUM"
else:
    risk_level = "HIGH"
 

 
personalized = (victim_name.lower() in email_text) and (course.lower() in email_text)
 
if personalized:
    attack_type = "Spear Phishing"
elif link_detected or credential_detected:
    attack_type = "Phishing"
else:
    attack_type = "Other"
 

 
if risk_level == "HIGH":
    recommendation = (
        "Do not click the link or submit any files or credentials. "
        "Verify directly with the instructor through a separate, "
        "trusted channel (official LMS, known office, or phone number) "
        "before taking any action."
    )
elif risk_level == "MEDIUM":
    recommendation = "Be cautious. Verify the sender and message before taking action."
else:
    recommendation = "No major warning signs detected, but continue to verify unexpected messages."
 

 
print("====================================")
print("       PHISHING EMAIL DETECTOR")
print("====================================")
print()
print("Sender:", email["sender"])
print("Subject:", email["subject"])
print()
print("INDICATORS FOUND")
print("------------------------------------")
for item in indicators:
    print("[!]", item)
print()
print("RISK SCORE:", score)
print()
print("RISK LEVEL:", risk_level)
print()
print("POSSIBLE ATTACK:")
print(attack_type)
print()
print("RECOMMENDATION:")
print(recommendation)