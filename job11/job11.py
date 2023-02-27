# Créer un programme job11.py qui parcourt le contenu du fichier “domains.xml” et qui
# compte le nombre de noms de domaine.

import xml.etree.ElementTree as ET

tree = ET.parse('domains.xml')
root = tree.getroot()
count = 0
for table in root.iter('table'):
    for column in table.iter('column'):
        if column.attrib['name'] == 'domain':
            count += 1

print('Le fichier contient', count, 'noms de domaine.')
