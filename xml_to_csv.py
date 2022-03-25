import xmltodict, csv, os, itertools
import pandas as pd

def xml_to_csv(filename: str, yr: int):
    # PARSE XML FILE
    with open(str(yr) + '\\xml\\' + filename + '.xml') as xmlfile:
        xml = xmltodict.parse(xmlfile.read())

    # CREATE CSV FILE
    csvfile = open(str(yr) + '\\csv\\' + filename + '.csv','w',encoding='utf-8')
    csvfile_writer = csv.writer(csvfile)

    # ADD HEADER
    cols = ["event_id","company_id","stock_symbol","company_name","stock_exchange", "isin",
            "earnings_date", "quarter", "fiscal_year", "earnings_date_status", "time_of_day",
            "quarter_end_date", "audit_source", "disclaimer"]
    csvfile_writer.writerow(cols)

    #FOR EACH EMPLOYEE
    for earning in xml["WallStreetHorizon"]["Source"]["earnings"]:

        # EXTRACT EMPLOYEE DETAILS
        csv_line = []
        for c in cols:
            try:
                csv_line.append([earning[c]])
            except:
                csv_line.append(' ')
            
        # ADD A NEW ROW TO CSV FILE
        csv_line = list(itertools.chain.from_iterable(csv_line))
        csvfile_writer.writerow(csv_line)
    
    csvfile.close()

    df = pd.read_csv(str(yr) + '\\csv\\' + filename + '.csv')
    df.to_csv(str(yr) + '\\csv\\' + filename + '.csv', index = False)

for yr in [
    2022, 2021, 2020, 2019, 2018, 2017
]:
    directory = str(yr) + '/xml'
 
    # iterate over files in
    # that directory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            try:
                xml_to_csv(f.lstrip(str(yr) + '/xml\\').rstrip('.XML').rstrip('.xml'), yr)
            except:
                pass
