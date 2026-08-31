Your final program should analyze a fictional email and produce a
clear security report.

TARGET STRUCTURE
----------------

====================================
       PHISHING EMAIL DETECTOR
====================================

Sender:
Subject:

INDICATORS FOUND
------------------------------------
[!] ...
[!] ...
[!] ...

RISK SCORE: ...

RISK LEVEL: ...

POSSIBLE ATTACK:
Phishing / Spear Phishing / Other

RECOMMENDATION:
...

====================================

FINAL ANALYSIS
--------------
Write a short Security Analyst Report answering:

1. What makes the email suspicious?
2. What information does the attacker know about the target?
3. What human behavior is being exploited?
4. What vulnerability is being exploited?
5. What could happen if the victim follows the instructions?
6. What should the victim do instead?
7. What are the limitations of your Python detector?

SUBMISSION
----------
Submit:
- phishing_detector.py
- Security Analyst Report
- Screenshots of your program working on at least 3 emails

OUTPUT:
Write your analysis in:
missions/ginal_mission.md

Save a screenshot of your code and programming running at
evidence/final_mission.png

After completing Last Mission. Commit your changes with a message of FLAG{THINK_LIKE_A_SECURITY_ANALYST}.

1. What makes the email suspicious?
   On the surface it looks like a normal professor email: correct
   name, correct course code, believable reason. The giveaway is the
   link. It's supposed to lead to a class submission page, but it
   points to "ite403-submission-portal.net" instead of the school's
   real domain, "university-example.edu." The "finalize the grades
   today" line also adds same-day pressure that discourages a student
   from stopping to double-check.
 
2. What information does the attacker know about the target?
   The attacker knows Alvin's first name, that he's enrolled in ITE
   403, and that the course has a Week 5 activity currently being
   graded. That's specific enough that it was probably pulled from a
   class roster, an LMS enrollment list, or a compromised faculty/
   student account rather than guessed at random.
 
3. What human behavior is being exploited?
   Trust in an authority figure (a professor), fear of losing credit
   for missing work, and time pressure from the "today" deadline that
   pushes Alvin to react quickly instead of verifying first.
 
4. What vulnerability is being exploited?
   A process/habit gap: students are used to clicking "review your
   submission" links in class emails and rarely check the destination
   domain before entering their school login on whatever page loads.
 
5. What could happen if the victim follows the instructions?
   The link likely leads to a fake login page styled like the
   school's LMS. If Alvin enters his username and password there, the
   attacker captures real credentials and can log into his actual
   school account, see personal/academic records, and use the account
   to send the same scam to classmates or other courses.
 
6. What should the victim do instead?
   Not click the link. Log into the official LMS directly through a
   bookmarked or manually typed URL and check the assignment status
   there, or contact the instructor through a known, separate channel
   (school email thread, office hours, class group chat) to confirm
   the request is real.
 
7. What are the limitations of your Python detector?
   This email is actually a good demonstration of the detector's
   blind spots: it contains none of the "loud" words in
   suspicious_words or credential_words (no "verify," "password," or
   "urgent"), so those checks return nothing. The tool only caught
   this case because of the personalization/course-targeting checks
   and the domain-mismatch check on the link not because of
   keyword matching. That means a well-written social-engineering
   email with no obvious trigger words, or one with no link at all
   (e.g., asking the victim to reply with information instead), could
   slip past this script entirely. It also has no real link-safety
   check (no DNS, WHOIS, or reputation lookup), no email header/SPF/
   DKIM analysis, and no machine learning it is a simple keyword
   and pattern matcher meant for learning, not production use.