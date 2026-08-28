emails = [
    {
        "name": "EMAIL A",
        "subject": "Your account will expire today",
        "body": """
Your account is scheduled for suspension.
Click here to verify your account immediately.
"""
    },
    {
        "name": "EMAIL B",
        "subject": "ITE 403 Week 5 Submission",
        "body": """
Hi Alvin,

I'm checking the submissions for ITE 403.
Your Week 5 activity appears to be missing.
Please review your submission before 3 PM.

Thank you,
Dr. Santos
"""
    },
    {
        "name": "EMAIL C",
        "subject": "Congratulations! You Won!",
        "body": """
You have won ₱50,000.
Send your account information to claim your prize.
"""
    }
]

suspicious_words = [
    "urgent",
    "verify",
    "password",
    "click",
    "suspended",
    "immediately"
]



for email in emails:

    print("=" * 40)
    print(email["name"])
    print("=" * 40)

    print("Subject:")
    print(email["subject"])

    print("\nMessage:")
    print(email["body"])

    print("SUSPICIOUS INDICATORS")
    print()

    email_text = (
        email["subject"] + " " + email["body"]
    ).lower()

    score = 0

    for word in suspicious_words:
        if word in email_text:
            print("[!] " + word)
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
    print()