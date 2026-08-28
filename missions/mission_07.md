MISSION 7 — IMPROVE YOUR DETECTOR
===================================

Your current detector is too simple.

Improve it.

ADD AT LEAST THREE NEW DETECTION RULES.

Do not use the examples below as your only answer. Think of your own
indicators first.

Possible areas to investigate:
- suspicious domains
- credential requests
- threatening language
- reward/prize language
- suspicious links
- personal information requests
- excessive urgency
- authority/impersonation

REQUIREMENTS
------------
Your improved program must:
1. Detect your original indicators.
2. Detect at least three new indicators.
3. Calculate a risk score.
4. Display a risk level.
5. Give a short recommendation.

Document the three new rules you added and explain why each matters.

OUTPUT:
Write your new document rules in:
missions/mission_07.md

Save a screenshot of your code and programming running at
evidence/mission_07.png

After completing Mission 7. Commit your changes with a message of Improve phishing detector.


Mission 7 — Improve Your Detector

Objective

The original phishing detector relied mainly on a fixed list of suspicious words. This version improves the detector by adding additional rules that look for common phishing characteristics.

The detector now checks the original indicators, spear-phishing indicators, and four new phishing indicators.

New Detection Rules

1. Credential Request

The detector checks for words and phrases such as:

- password
- login
- credentials
- account information
- username

This matters because phishing emails commonly attempt to trick users into giving away account or login information. Detecting these requests can identify messages that may be trying to steal credentials.

2. Reward or Prize Language

The detector checks for phrases such as:

- you won
- winner
- prize
- reward
- cash
- congratulations

This matters because phishing messages may use fake prizes, rewards, or money to persuade users to interact with a message or provide information.

3. Suspicious Links

The detector checks for:

- `[LINK]`
- `http://`
- `https://`

This matters because phishing emails may direct victims to websites designed to collect information or impersonate legitimate services. A link alone does not prove that an email is malicious, but it is an indicator that deserves additional attention.

4. Urgency or Deadline Pressure

The detector checks for words and phrases such as:

- today
- immediately
- urgent
- act now
- deadline
- expires

This matters because attackers may create a sense of urgency so that the recipient acts before carefully checking the message.

Original Indicators Retained

The improved detector continues to check the original suspicious indicators:

- urgent
- verify
- password
- click
- suspended
- immediately

It also keeps the two spear-phishing indicators:

- Victim's name
- Specific course information

Risk Scoring

Each detected indicator increases the risk score.

Some stronger indicators, such as credential requests, reward/prize language, and suspicious links, receive two points because they can be particularly relevant to phishing detection.

The risk levels are:

- **LOW** — score of 0–2
- **MEDIUM** — score of 3–5
- **HIGH** — score of 6 or higher

Recommendation

The detector also provides a short recommendation based on the calculated risk level.

For a high-risk email, the recommendation is to avoid clicking links or providing information and to verify the sender through a trusted channel.

For a medium-risk email, the user is advised to be cautious and verify the message before taking action.

For a low-risk email, the detector reports that no major warning signs were detected, while still recommending normal caution.

Why the Improved Detector Is Better

The original detector mainly searched for individual suspicious words. This could cause it to miss phishing emails that use different wording.

The improved detector looks for several types of suspicious behavior, including credential requests, prize claims, links, urgency, personalization, and academic targeting.

This makes the detector more useful because phishing detection does not depend on one specific word. Multiple indicators can be combined to produce a risk score and a more meaningful risk level.