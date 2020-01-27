# Create a new text object using Polyglot's Text class: txt
txt = Text(article)

# Print each of the entities found
for ent in txt.entities:
    print(ent)
    
""" <script.py> output:
    ['Charles', 'Cuvelliez']
    ['Charles', 'Cuvelliez']
    ['Bruxelles']
    ['l’IA']
    ['Julien', 'Maldonato']
    ['Deloitte']
    ['Ethiquement']
    ['l’IA']
    ['.'] """
    
# Print the type of ent
print(type(ent))

""" <script.py> output:
    <class 'polyglot.text.Chunk'> """