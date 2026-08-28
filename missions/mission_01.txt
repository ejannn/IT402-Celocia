MISSION 1 — ANALYZE THE EMAIL
================================

Do NOT write Python yet.

Read this fictional email:

From: IT Support <support@school-security.example>
Subject: URGENT: Account Verification Required

Hi Alvin,

We noticed unusual activity on your student account.

Your account will be suspended today unless you verify your account
immediately.

Please click the link below:

http://school-account-verification.example/login

Enter your username and password to continue.

IT Support Team

YOUR TASK
---------
Identify:

1. Who is the target?
    => Alvin Araneta
2. Who is the supposed sender?
    => support@school-security.example
3. What is the attacker asking for?
    => Username and Password for verification.
4. What creates urgency?
    => the subject of the mail
5. What information makes the message convincing?
    => "Your account will be suspended today unless you verify your account
        immediately."
6. What could the attacker gain?
    => Username and Password
7. Identify at least five red flags.
    => 1 the sender specifically said that account will be suspended today.
       2 the link is kinda suspicious
       3 entering bare username and password to continue
       4 no reason why the account is in risk or proof of unusual activuty to see.
       5 immediately sound so desperate
OUTPUT:
Write your answers in:
missions/mission_01.md

After completing Mission 1. Commit your changes with a message of Complete Mission 1 analysis.