# Calculate the proportion of txt.entities that
# contains 'Márquez' or 'Gabo': prop_ggm
count =0
for ent in txt.entities:
    if ('Márquez' in ent or 'Gabo' in ent):
        count += 1
        
prop_ggm = count / len(txt.entities)