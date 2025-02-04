import re
import string
import nltk
from nltk.corpus import words

nltk.download('words')
common_words = set(words.words())

def check_password_strength(password):
    """Check password strength and provide feedback."""
    
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_char_criteria = any(char in string.punctuation for char in password)
    dictionary_check = password.lower() not in common_words  # Avoid common words

    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria, dictionary_check])

    if score == 6:
        strength = "Strong "
    elif 4 <= score < 6:
        strength = "Medium "
    else:
        strength = "Weak "

    feedback = []
    if not length_criteria:
        feedback.append("Increase password length (at least 8 characters).")
    if not uppercase_criteria:
        feedback.append("Add at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Add at least one lowercase letter.")
    if not digit_criteria:
        feedback.append("Include at least one digit (0-9).")
    if not special_char_criteria:
        feedback.append("Use at least one special character (!@#$%^&*).")
    if not dictionary_check:
        feedback.append("Avoid using common words or dictionary-based passwords.")

    return strength, feedback

