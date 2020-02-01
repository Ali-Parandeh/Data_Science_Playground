# Import the Spanish language class
from spacy.lang.en import English
from spacy.lang.de import German
from spacy.lang.es import Spanish

# Create the nlp object
nlp = Spanish() # or English() or German()

# Process a text (this is Spanish for: "How are you?")
doc = nlp("¿Cómo estás?")

# Print the document text
print(doc.text)
#  '¿Cómo estás?'