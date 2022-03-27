from beach_manager.models import Beach
from django.db import IntegrityError

import csv

def import_beaches_csv(lines):
    reader = csv.reader(lines, delimiter=",")
    line_count = 0

    print("\033[94mImporting beaches from csv file...\033[0m")
    for row in reader:              
        line_count += 1
        if line_count == 1:
            continue
        else:
            name = row[0].strip()
            municipality = row[1].strip()          

            try:
                Beach.objects.create(
                    name=name,
                    municipality=municipality,
                )

            except IntegrityError:
                print("\033[93mERROR: The beach (%s) was duplicated!\033[0m" % (name))
            
    print("\033[94mImported %s beaches\033[0m" % (line_count-1))