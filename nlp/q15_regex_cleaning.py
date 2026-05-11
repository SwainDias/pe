# Q15. Regex-based Text Cleaning

import re

text = "Hello, World! This is NLP Lab-2025. Remove: punctuation, numbers (123), & special chars!!!"

print(f"Original text:\n  {text}\n")

# Step 1: Remove punctuation
step1 = re.sub(r'[^\w\s]', '', text)
print(f"After removing punctuation:\n  {step1}\n")

# Step 2: Remove numbers
step2 = re.sub(r'\d+', '', step1)
print(f"After removing numbers:\n  {step2}\n")

# Step 3: Convert to lowercase
step3 = step2.lower()
print(f"After converting to lowercase:\n  {step3}\n")

# Step 4: Remove extra whitespace
cleaned = re.sub(r'\s+', ' ', step3).strip()
print(f"Final cleaned text:\n  {cleaned}")
