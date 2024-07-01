import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

def categorize_task(description):
    # Simple categorization based on keywords
    tokens = word_tokenize(description)
    tokens = [word for word in tokens if word.isalnum()]
    tokens = [word for word in tokens if word.lower() not in stopwords.words('english')]

    if any(word in tokens for word in ['work', 'office', 'project']):
        return 'Work'
    elif any(word in tokens for word in ['home', 'cleaning', 'chores']):
        return 'Home'
    else:
        return 'Other'
