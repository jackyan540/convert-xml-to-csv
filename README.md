# convert-xml-to-csv
HBS Research Associate project to convert XML formatted files to CSV formats. Project completed for Professor Jonathan Wallen.

Received data covering Jan. 1, 2017 through Mar. 14, 2022. Data is at the daily frequency level, amounting to 1,900 individual XML files. The objective is to convert these XML files into easier to use CSV files without any data loss.

*The data is proprietary and cannot be shared in this repository. Details about the data are described below.*

## Data Specifications

XML file names are formatted as: `WSH_DAILY_SNAPSHOT_ED_V03_YYMMDD.xml` (i.e. for Jan. 1, 2022: `WSH_DAILY_SNAPSHOT_ED_V03_20220101.xml`). Some XML filename extensions are capitalized (i.e. using `.XML` rather than `.xml`).  CSV file names will have the same format: `WSH_DAILY_SNAPSHOT_ED_V03_YYMMDD.csv`.

Data is organized by year and file format. (i.e. for an XML file dated Jan. 1, 2022, the file path is: `2022\xml\WSH_DAILY_SNAPSHOT_ED_V03_20220101.xml` and for the file path for the corresponding csv file is: `2022\csv\WSH_DAILY_SNAPSHOT_ED_V03_20220101.csv`).

XML files are formatted as:  
`<WallStreetHorizon>`  
    `<earnings>`  
        `<event_id> </event_id>`  
        `<company_id> </company_id>`  
        `<stock_symbol> </stock_symbol>`  
        `<company_name> </company_name>`  
        `<stock_exchange> </stock_exchange>`  
        `<isin> </isin>`  
        `<earnings_date> </earnings_date>`  
        `<quarter> </quarter>`  
    `</earnings>`  
`</WallStreetHorizon>`
