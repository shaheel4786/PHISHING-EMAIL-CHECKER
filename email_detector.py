import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download once
nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

# Define phishing keywords
phishing_keywords = {
    'click', 'verify', 'password', 'account', 'bank',
    'urgent', 'login', 'reset', 'confirm', 'blocked',
    'suspend', 'immediately', 'payment', 'security',
    'limit', 'restricted', 'access', 'update', 'unauthorized'
}

def preprocess(text):
    tokens = word_tokenize(text)
    tokens = [word.lower() for word in tokens if word.isalpha()]
    return [w for w in tokens if w not in stop_words]

# Start checker
print("\n--- PHISHING EMAIL CHECKER ---")
subject = input("ENTER THE SUBJECT OF THE EMAIL YOU WANT TO CHECK:\n")

print("\nENTER EACH LINE OF THE EMAIL BODY ONE BY ONE.")
print("Type 'done' when you are finished entering the body.\n")

body_lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    body_lines.append(line)

# Combine subject and body
full_email = subject + " " + " ".join(body_lines)

# Preprocess and detect
tokens = preprocess(full_email)
hits = [word for word in tokens if word in phishing_keywords]

print("\nTokens:", tokens)
if len(hits) >= 2:
    print(f"🛑 Phishing Keywords Detected: {hits}")
    print("FINAL RESULT: DEAR USER YOU WANT TO BE CAREFUL - This email is a PHISHING attempt!")
else:
    print("✅ FINAL RESULT: DON'T WORRY YOU ARE SAFE - This email seems LEGIT.")
