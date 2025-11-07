
# Data Product Canvas - Berlin Building Completions (source-aligned)

## Metadata

* owner: Open Data Product
* description: Source-aligned data product combining Berlin LOR health and social structure data
* updated: 2025-10-27

## Input Ports

### Baufertigstellungen, Bauüberhang und Bauabgang in Berlin 2020

* owner: Amt für Statistik Berlin-Brandenburg
* url: https://www.statistik-berlin-brandenburg.de/f-ii-2-j
* license: CC-BY-3.0-Namensnennung
* updated: 2021-06-09

**Files**

* [SB_F02-02-00_2020j01_BE.xlsx](https://download.statistik-berlin-brandenburg.de/629351f64cf37f48/60bed0ed87bb/SB_F02-02-00_2020j01_BE.xlsx)

### Baufertigstellungen, Bauüberhang und Bauabgang in Berlin 2021

* owner: Amt für Statistik Berlin-Brandenburg
* url: https://www.statistik-berlin-brandenburg.de/f-ii-2-j
* license: CC-BY-3.0-Namensnennung
* updated: 2022-06-09

**Files**

* [SB_F02-02-00_2021j01_BE.xlsx](https://download.statistik-berlin-brandenburg.de/d712acdbe5af5c59/885f96bb0c20/SB_F02-02-00_2021j01_BE.xlsx)

### Baufertigstellungen, Bauüberhang und Bauabgang in Berlin 2022

* owner: Amt für Statistik Berlin-Brandenburg
* url: https://www.statistik-berlin-brandenburg.de/f-ii-2-j
* license: CC-BY-3.0-Namensnennung
* updated: 2023-06-09

**Files**

* [SB_F02-02-00_2022j01_BE.xlsx](https://download.statistik-berlin-brandenburg.de/2bd07d614def86bb/6dba9f3eaa0a/SB_F02-02-00_2022j01_BE.xlsx)

### Baufertigstellungen, Bauüberhang und Bauabgang in Berlin 2023

* owner: Amt für Statistik Berlin-Brandenburg
* url: https://www.statistik-berlin-brandenburg.de/f-ii-2-j
* license: CC-BY-3.0-Namensnennung
* updated: 2024-06-07

**Files**

* [SB_F02-02-00_2023j01_BE.xlsx](https://download.statistik-berlin-brandenburg.de/8fca15dee88731ef/38ecf53a67a0/SB_F02-02-00_2023j01_BE.xlsx)

## Transformation Steps

* [Data extractor](https://github.com/open-data-product/open-data-product-python-lib/blob/main/opendataproduct/extract/data_extractor.py) extracts data from inout ports
* [Data copier](https://github.com/open-data-product/open-data-product-python-lib/blob/main/opendataproduct/transform/data_copier.py) copies and renames extracted data
* [Data CSV converter](https://github.com/open-data-product/open-data-product-python-lib/blob/main/opendataproduct/transform/data_csv_converter.py) converts Excel files to CSV format
* [Data aggregator](https://github.com/open-data-product/open-data-product-python-lib/blob/main/opendataproduct/transform/data_aggregator.py) aggregates data to be used as output ports

## Output Ports

### Berlin Building Completions 2020 00 Csv

* owner: Open Data Product
* url: https://github.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/tree/main/data/03-gold/berlin-building-completions-2020-00-csv
* updated: 2025-10-27

**Files**

* [berlin-building-completions-2020-00-12-completions-including-measures-on-existing-buildings-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2020-00-csv/berlin-building-completions-2020-00-12-completions-including-measures-on-existing-buildings-city.csv)
* [berlin-building-completions-2020-00-12-completions-including-measures-on-existing-buildings-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2020-00-csv/berlin-building-completions-2020-00-12-completions-including-measures-on-existing-buildings-districts.csv)
* [berlin-building-completions-2020-00-13-completions-new-buildings-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2020-00-csv/berlin-building-completions-2020-00-13-completions-new-buildings-city.csv)
* [berlin-building-completions-2020-00-13-completions-new-buildings-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2020-00-csv/berlin-building-completions-2020-00-13-completions-new-buildings-districts.csv)
* [berlin-building-completions-2020-00-14-completions-new-buildings-with-1-or-2-apartments-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2020-00-csv/berlin-building-completions-2020-00-14-completions-new-buildings-with-1-or-2-apartments-city.csv)
* [berlin-building-completions-2020-00-14-completions-new-buildings-with-1-or-2-apartments-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2020-00-csv/berlin-building-completions-2020-00-14-completions-new-buildings-with-1-or-2-apartments-districts.csv)
* [berlin-building-completions-2020-00-15-completions-new-non-residential-buildings-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2020-00-csv/berlin-building-completions-2020-00-15-completions-new-non-residential-buildings-city.csv)
* [berlin-building-completions-2020-00-15-completions-new-non-residential-buildings-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2020-00-csv/berlin-building-completions-2020-00-15-completions-new-non-residential-buildings-districts.csv)
* [berlin-building-completions-2020-00-16-construction-backlog-housing-projects-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2020-00-csv/berlin-building-completions-2020-00-16-construction-backlog-housing-projects-city.csv)
* [berlin-building-completions-2020-00-16-construction-backlog-housing-projects-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2020-00-csv/berlin-building-completions-2020-00-16-construction-backlog-housing-projects-districts.csv)
* [berlin-building-completions-2020-00-17-construction-backlog-apartments-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2020-00-csv/berlin-building-completions-2020-00-17-construction-backlog-apartments-city.csv)
* [berlin-building-completions-2020-00-17-construction-backlog-apartments-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2020-00-csv/berlin-building-completions-2020-00-17-construction-backlog-apartments-districts.csv)
* [berlin-building-completions-2020-00-18-construction-backlog-non-residential-buildings-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2020-00-csv/berlin-building-completions-2020-00-18-construction-backlog-non-residential-buildings-city.csv)
* [berlin-building-completions-2020-00-18-construction-backlog-non-residential-buildings-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2020-00-csv/berlin-building-completions-2020-00-18-construction-backlog-non-residential-buildings-districts.csv)
* [berlin-building-completions-2020-00-23-outflow-of-all-buildings-complete-districts-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2020-00-csv/berlin-building-completions-2020-00-23-outflow-of-all-buildings-complete-districts-city.csv)
* [berlin-building-completions-2020-00-23-outflow-of-all-buildings-complete-districts-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2020-00-csv/berlin-building-completions-2020-00-23-outflow-of-all-buildings-complete-districts-districts.csv)

### Berlin Building Completions 2020 00 Parquet

* owner: Open Data Product
* url: https://github.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/tree/main/data/03-gold/berlin-building-completions-2020-00-parquet
* updated: 2025-10-27

**Files**

* [berlin-building-completions-2020-00-12-completions-including-measures-on-existing-buildings-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2020-00-parquet/berlin-building-completions-2020-00-12-completions-including-measures-on-existing-buildings-city.parquet)
* [berlin-building-completions-2020-00-12-completions-including-measures-on-existing-buildings-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2020-00-parquet/berlin-building-completions-2020-00-12-completions-including-measures-on-existing-buildings-districts.parquet)
* [berlin-building-completions-2020-00-13-completions-new-buildings-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2020-00-parquet/berlin-building-completions-2020-00-13-completions-new-buildings-city.parquet)
* [berlin-building-completions-2020-00-13-completions-new-buildings-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2020-00-parquet/berlin-building-completions-2020-00-13-completions-new-buildings-districts.parquet)
* [berlin-building-completions-2020-00-14-completions-new-buildings-with-1-or-2-apartments-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2020-00-parquet/berlin-building-completions-2020-00-14-completions-new-buildings-with-1-or-2-apartments-city.parquet)
* [berlin-building-completions-2020-00-14-completions-new-buildings-with-1-or-2-apartments-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2020-00-parquet/berlin-building-completions-2020-00-14-completions-new-buildings-with-1-or-2-apartments-districts.parquet)
* [berlin-building-completions-2020-00-15-completions-new-non-residential-buildings-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2020-00-parquet/berlin-building-completions-2020-00-15-completions-new-non-residential-buildings-city.parquet)
* [berlin-building-completions-2020-00-15-completions-new-non-residential-buildings-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2020-00-parquet/berlin-building-completions-2020-00-15-completions-new-non-residential-buildings-districts.parquet)
* [berlin-building-completions-2020-00-16-construction-backlog-housing-projects-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2020-00-parquet/berlin-building-completions-2020-00-16-construction-backlog-housing-projects-city.parquet)
* [berlin-building-completions-2020-00-16-construction-backlog-housing-projects-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2020-00-parquet/berlin-building-completions-2020-00-16-construction-backlog-housing-projects-districts.parquet)
* [berlin-building-completions-2020-00-17-construction-backlog-apartments-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2020-00-parquet/berlin-building-completions-2020-00-17-construction-backlog-apartments-city.parquet)
* [berlin-building-completions-2020-00-17-construction-backlog-apartments-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2020-00-parquet/berlin-building-completions-2020-00-17-construction-backlog-apartments-districts.parquet)
* [berlin-building-completions-2020-00-18-construction-backlog-non-residential-buildings-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2020-00-parquet/berlin-building-completions-2020-00-18-construction-backlog-non-residential-buildings-city.parquet)
* [berlin-building-completions-2020-00-18-construction-backlog-non-residential-buildings-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2020-00-parquet/berlin-building-completions-2020-00-18-construction-backlog-non-residential-buildings-districts.parquet)
* [berlin-building-completions-2020-00-23-outflow-of-all-buildings-complete-districts-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2020-00-parquet/berlin-building-completions-2020-00-23-outflow-of-all-buildings-complete-districts-city.parquet)
* [berlin-building-completions-2020-00-23-outflow-of-all-buildings-complete-districts-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2020-00-parquet/berlin-building-completions-2020-00-23-outflow-of-all-buildings-complete-districts-districts.parquet)

### Berlin Building Completions 2021 00 Csv

* owner: Open Data Product
* url: https://github.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/tree/main/data/03-gold/berlin-building-completions-2021-00-csv
* updated: 2025-10-27

**Files**

* [berlin-building-completions-2021-00-12-completions-including-measures-on-existing-buildings-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2021-00-csv/berlin-building-completions-2021-00-12-completions-including-measures-on-existing-buildings-city.csv)
* [berlin-building-completions-2021-00-12-completions-including-measures-on-existing-buildings-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2021-00-csv/berlin-building-completions-2021-00-12-completions-including-measures-on-existing-buildings-districts.csv)
* [berlin-building-completions-2021-00-13-completions-new-buildings-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2021-00-csv/berlin-building-completions-2021-00-13-completions-new-buildings-city.csv)
* [berlin-building-completions-2021-00-13-completions-new-buildings-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2021-00-csv/berlin-building-completions-2021-00-13-completions-new-buildings-districts.csv)
* [berlin-building-completions-2021-00-14-completions-new-buildings-with-1-or-2-apartments-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2021-00-csv/berlin-building-completions-2021-00-14-completions-new-buildings-with-1-or-2-apartments-city.csv)
* [berlin-building-completions-2021-00-14-completions-new-buildings-with-1-or-2-apartments-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2021-00-csv/berlin-building-completions-2021-00-14-completions-new-buildings-with-1-or-2-apartments-districts.csv)
* [berlin-building-completions-2021-00-15-completions-new-non-residential-buildings-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2021-00-csv/berlin-building-completions-2021-00-15-completions-new-non-residential-buildings-city.csv)
* [berlin-building-completions-2021-00-15-completions-new-non-residential-buildings-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2021-00-csv/berlin-building-completions-2021-00-15-completions-new-non-residential-buildings-districts.csv)
* [berlin-building-completions-2021-00-16-construction-backlog-housing-projects-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2021-00-csv/berlin-building-completions-2021-00-16-construction-backlog-housing-projects-city.csv)
* [berlin-building-completions-2021-00-16-construction-backlog-housing-projects-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2021-00-csv/berlin-building-completions-2021-00-16-construction-backlog-housing-projects-districts.csv)
* [berlin-building-completions-2021-00-17-construction-backlog-apartments-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2021-00-csv/berlin-building-completions-2021-00-17-construction-backlog-apartments-city.csv)
* [berlin-building-completions-2021-00-17-construction-backlog-apartments-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2021-00-csv/berlin-building-completions-2021-00-17-construction-backlog-apartments-districts.csv)
* [berlin-building-completions-2021-00-18-construction-backlog-non-residential-buildings-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2021-00-csv/berlin-building-completions-2021-00-18-construction-backlog-non-residential-buildings-city.csv)
* [berlin-building-completions-2021-00-18-construction-backlog-non-residential-buildings-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2021-00-csv/berlin-building-completions-2021-00-18-construction-backlog-non-residential-buildings-districts.csv)
* [berlin-building-completions-2021-00-23-outflow-of-all-buildings-complete-districts-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2021-00-csv/berlin-building-completions-2021-00-23-outflow-of-all-buildings-complete-districts-city.csv)
* [berlin-building-completions-2021-00-23-outflow-of-all-buildings-complete-districts-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2021-00-csv/berlin-building-completions-2021-00-23-outflow-of-all-buildings-complete-districts-districts.csv)

### Berlin Building Completions 2021 00 Parquet

* owner: Open Data Product
* url: https://github.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/tree/main/data/03-gold/berlin-building-completions-2021-00-parquet
* updated: 2025-10-27

**Files**

* [berlin-building-completions-2021-00-12-completions-including-measures-on-existing-buildings-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2021-00-parquet/berlin-building-completions-2021-00-12-completions-including-measures-on-existing-buildings-city.parquet)
* [berlin-building-completions-2021-00-12-completions-including-measures-on-existing-buildings-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2021-00-parquet/berlin-building-completions-2021-00-12-completions-including-measures-on-existing-buildings-districts.parquet)
* [berlin-building-completions-2021-00-13-completions-new-buildings-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2021-00-parquet/berlin-building-completions-2021-00-13-completions-new-buildings-city.parquet)
* [berlin-building-completions-2021-00-13-completions-new-buildings-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2021-00-parquet/berlin-building-completions-2021-00-13-completions-new-buildings-districts.parquet)
* [berlin-building-completions-2021-00-14-completions-new-buildings-with-1-or-2-apartments-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2021-00-parquet/berlin-building-completions-2021-00-14-completions-new-buildings-with-1-or-2-apartments-city.parquet)
* [berlin-building-completions-2021-00-14-completions-new-buildings-with-1-or-2-apartments-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2021-00-parquet/berlin-building-completions-2021-00-14-completions-new-buildings-with-1-or-2-apartments-districts.parquet)
* [berlin-building-completions-2021-00-15-completions-new-non-residential-buildings-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2021-00-parquet/berlin-building-completions-2021-00-15-completions-new-non-residential-buildings-city.parquet)
* [berlin-building-completions-2021-00-15-completions-new-non-residential-buildings-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2021-00-parquet/berlin-building-completions-2021-00-15-completions-new-non-residential-buildings-districts.parquet)
* [berlin-building-completions-2021-00-16-construction-backlog-housing-projects-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2021-00-parquet/berlin-building-completions-2021-00-16-construction-backlog-housing-projects-city.parquet)
* [berlin-building-completions-2021-00-16-construction-backlog-housing-projects-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2021-00-parquet/berlin-building-completions-2021-00-16-construction-backlog-housing-projects-districts.parquet)
* [berlin-building-completions-2021-00-17-construction-backlog-apartments-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2021-00-parquet/berlin-building-completions-2021-00-17-construction-backlog-apartments-city.parquet)
* [berlin-building-completions-2021-00-17-construction-backlog-apartments-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2021-00-parquet/berlin-building-completions-2021-00-17-construction-backlog-apartments-districts.parquet)
* [berlin-building-completions-2021-00-18-construction-backlog-non-residential-buildings-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2021-00-parquet/berlin-building-completions-2021-00-18-construction-backlog-non-residential-buildings-city.parquet)
* [berlin-building-completions-2021-00-18-construction-backlog-non-residential-buildings-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2021-00-parquet/berlin-building-completions-2021-00-18-construction-backlog-non-residential-buildings-districts.parquet)
* [berlin-building-completions-2021-00-23-outflow-of-all-buildings-complete-districts-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2021-00-parquet/berlin-building-completions-2021-00-23-outflow-of-all-buildings-complete-districts-city.parquet)
* [berlin-building-completions-2021-00-23-outflow-of-all-buildings-complete-districts-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2021-00-parquet/berlin-building-completions-2021-00-23-outflow-of-all-buildings-complete-districts-districts.parquet)

### Berlin Building Completions 2022 00 Csv

* owner: Open Data Product
* url: https://github.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/tree/main/data/03-gold/berlin-building-completions-2022-00-csv
* updated: 2025-10-27

**Files**

* [berlin-building-completions-2022-00-12-completions-including-measures-on-existing-buildings-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2022-00-csv/berlin-building-completions-2022-00-12-completions-including-measures-on-existing-buildings-city.csv)
* [berlin-building-completions-2022-00-12-completions-including-measures-on-existing-buildings-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2022-00-csv/berlin-building-completions-2022-00-12-completions-including-measures-on-existing-buildings-districts.csv)
* [berlin-building-completions-2022-00-13-completions-new-buildings-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2022-00-csv/berlin-building-completions-2022-00-13-completions-new-buildings-city.csv)
* [berlin-building-completions-2022-00-13-completions-new-buildings-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2022-00-csv/berlin-building-completions-2022-00-13-completions-new-buildings-districts.csv)
* [berlin-building-completions-2022-00-14-completions-new-buildings-with-1-or-2-apartments-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2022-00-csv/berlin-building-completions-2022-00-14-completions-new-buildings-with-1-or-2-apartments-city.csv)
* [berlin-building-completions-2022-00-14-completions-new-buildings-with-1-or-2-apartments-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2022-00-csv/berlin-building-completions-2022-00-14-completions-new-buildings-with-1-or-2-apartments-districts.csv)
* [berlin-building-completions-2022-00-15-completions-new-non-residential-buildings-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2022-00-csv/berlin-building-completions-2022-00-15-completions-new-non-residential-buildings-city.csv)
* [berlin-building-completions-2022-00-15-completions-new-non-residential-buildings-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2022-00-csv/berlin-building-completions-2022-00-15-completions-new-non-residential-buildings-districts.csv)
* [berlin-building-completions-2022-00-16-construction-backlog-housing-projects-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2022-00-csv/berlin-building-completions-2022-00-16-construction-backlog-housing-projects-city.csv)
* [berlin-building-completions-2022-00-16-construction-backlog-housing-projects-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2022-00-csv/berlin-building-completions-2022-00-16-construction-backlog-housing-projects-districts.csv)
* [berlin-building-completions-2022-00-17-construction-backlog-apartments-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2022-00-csv/berlin-building-completions-2022-00-17-construction-backlog-apartments-city.csv)
* [berlin-building-completions-2022-00-17-construction-backlog-apartments-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2022-00-csv/berlin-building-completions-2022-00-17-construction-backlog-apartments-districts.csv)
* [berlin-building-completions-2022-00-18-construction-backlog-non-residential-buildings-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2022-00-csv/berlin-building-completions-2022-00-18-construction-backlog-non-residential-buildings-city.csv)
* [berlin-building-completions-2022-00-18-construction-backlog-non-residential-buildings-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2022-00-csv/berlin-building-completions-2022-00-18-construction-backlog-non-residential-buildings-districts.csv)
* [berlin-building-completions-2022-00-23-outflow-of-all-buildings-complete-districts-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2022-00-csv/berlin-building-completions-2022-00-23-outflow-of-all-buildings-complete-districts-city.csv)
* [berlin-building-completions-2022-00-23-outflow-of-all-buildings-complete-districts-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2022-00-csv/berlin-building-completions-2022-00-23-outflow-of-all-buildings-complete-districts-districts.csv)

### Berlin Building Completions 2022 00 Parquet

* owner: Open Data Product
* url: https://github.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/tree/main/data/03-gold/berlin-building-completions-2022-00-parquet
* updated: 2025-10-27

**Files**

* [berlin-building-completions-2022-00-12-completions-including-measures-on-existing-buildings-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2022-00-parquet/berlin-building-completions-2022-00-12-completions-including-measures-on-existing-buildings-city.parquet)
* [berlin-building-completions-2022-00-12-completions-including-measures-on-existing-buildings-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2022-00-parquet/berlin-building-completions-2022-00-12-completions-including-measures-on-existing-buildings-districts.parquet)
* [berlin-building-completions-2022-00-13-completions-new-buildings-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2022-00-parquet/berlin-building-completions-2022-00-13-completions-new-buildings-city.parquet)
* [berlin-building-completions-2022-00-13-completions-new-buildings-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2022-00-parquet/berlin-building-completions-2022-00-13-completions-new-buildings-districts.parquet)
* [berlin-building-completions-2022-00-14-completions-new-buildings-with-1-or-2-apartments-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2022-00-parquet/berlin-building-completions-2022-00-14-completions-new-buildings-with-1-or-2-apartments-city.parquet)
* [berlin-building-completions-2022-00-14-completions-new-buildings-with-1-or-2-apartments-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2022-00-parquet/berlin-building-completions-2022-00-14-completions-new-buildings-with-1-or-2-apartments-districts.parquet)
* [berlin-building-completions-2022-00-15-completions-new-non-residential-buildings-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2022-00-parquet/berlin-building-completions-2022-00-15-completions-new-non-residential-buildings-city.parquet)
* [berlin-building-completions-2022-00-15-completions-new-non-residential-buildings-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2022-00-parquet/berlin-building-completions-2022-00-15-completions-new-non-residential-buildings-districts.parquet)
* [berlin-building-completions-2022-00-16-construction-backlog-housing-projects-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2022-00-parquet/berlin-building-completions-2022-00-16-construction-backlog-housing-projects-city.parquet)
* [berlin-building-completions-2022-00-16-construction-backlog-housing-projects-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2022-00-parquet/berlin-building-completions-2022-00-16-construction-backlog-housing-projects-districts.parquet)
* [berlin-building-completions-2022-00-17-construction-backlog-apartments-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2022-00-parquet/berlin-building-completions-2022-00-17-construction-backlog-apartments-city.parquet)
* [berlin-building-completions-2022-00-17-construction-backlog-apartments-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2022-00-parquet/berlin-building-completions-2022-00-17-construction-backlog-apartments-districts.parquet)
* [berlin-building-completions-2022-00-18-construction-backlog-non-residential-buildings-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2022-00-parquet/berlin-building-completions-2022-00-18-construction-backlog-non-residential-buildings-city.parquet)
* [berlin-building-completions-2022-00-18-construction-backlog-non-residential-buildings-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2022-00-parquet/berlin-building-completions-2022-00-18-construction-backlog-non-residential-buildings-districts.parquet)
* [berlin-building-completions-2022-00-23-outflow-of-all-buildings-complete-districts-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2022-00-parquet/berlin-building-completions-2022-00-23-outflow-of-all-buildings-complete-districts-city.parquet)
* [berlin-building-completions-2022-00-23-outflow-of-all-buildings-complete-districts-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2022-00-parquet/berlin-building-completions-2022-00-23-outflow-of-all-buildings-complete-districts-districts.parquet)

### Berlin Building Completions 2023 00 Csv

* owner: Open Data Product
* url: https://github.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/tree/main/data/03-gold/berlin-building-completions-2023-00-csv
* updated: 2025-10-27

**Files**

* [berlin-building-completions-2023-00-12-completions-including-measures-on-existing-buildings-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2023-00-csv/berlin-building-completions-2023-00-12-completions-including-measures-on-existing-buildings-city.csv)
* [berlin-building-completions-2023-00-12-completions-including-measures-on-existing-buildings-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2023-00-csv/berlin-building-completions-2023-00-12-completions-including-measures-on-existing-buildings-districts.csv)
* [berlin-building-completions-2023-00-13-completions-new-buildings-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2023-00-csv/berlin-building-completions-2023-00-13-completions-new-buildings-city.csv)
* [berlin-building-completions-2023-00-13-completions-new-buildings-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2023-00-csv/berlin-building-completions-2023-00-13-completions-new-buildings-districts.csv)
* [berlin-building-completions-2023-00-14-completions-new-buildings-with-1-or-2-apartments-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2023-00-csv/berlin-building-completions-2023-00-14-completions-new-buildings-with-1-or-2-apartments-city.csv)
* [berlin-building-completions-2023-00-14-completions-new-buildings-with-1-or-2-apartments-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2023-00-csv/berlin-building-completions-2023-00-14-completions-new-buildings-with-1-or-2-apartments-districts.csv)
* [berlin-building-completions-2023-00-15-completions-new-non-residential-buildings-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2023-00-csv/berlin-building-completions-2023-00-15-completions-new-non-residential-buildings-city.csv)
* [berlin-building-completions-2023-00-15-completions-new-non-residential-buildings-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2023-00-csv/berlin-building-completions-2023-00-15-completions-new-non-residential-buildings-districts.csv)
* [berlin-building-completions-2023-00-16-construction-backlog-housing-projects-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2023-00-csv/berlin-building-completions-2023-00-16-construction-backlog-housing-projects-city.csv)
* [berlin-building-completions-2023-00-16-construction-backlog-housing-projects-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2023-00-csv/berlin-building-completions-2023-00-16-construction-backlog-housing-projects-districts.csv)
* [berlin-building-completions-2023-00-17-construction-backlog-apartments-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2023-00-csv/berlin-building-completions-2023-00-17-construction-backlog-apartments-city.csv)
* [berlin-building-completions-2023-00-17-construction-backlog-apartments-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2023-00-csv/berlin-building-completions-2023-00-17-construction-backlog-apartments-districts.csv)
* [berlin-building-completions-2023-00-18-construction-backlog-non-residential-buildings-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2023-00-csv/berlin-building-completions-2023-00-18-construction-backlog-non-residential-buildings-city.csv)
* [berlin-building-completions-2023-00-18-construction-backlog-non-residential-buildings-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2023-00-csv/berlin-building-completions-2023-00-18-construction-backlog-non-residential-buildings-districts.csv)
* [berlin-building-completions-2023-00-23-outflow-of-all-buildings-complete-districts-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2023-00-csv/berlin-building-completions-2023-00-23-outflow-of-all-buildings-complete-districts-city.csv)
* [berlin-building-completions-2023-00-23-outflow-of-all-buildings-complete-districts-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2023-00-csv/berlin-building-completions-2023-00-23-outflow-of-all-buildings-complete-districts-districts.csv)

### Berlin Building Completions 2023 00 Parquet

* owner: Open Data Product
* url: https://github.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/tree/main/data/03-gold/berlin-building-completions-2023-00-parquet
* updated: 2025-10-27

**Files**

* [berlin-building-completions-2023-00-12-completions-including-measures-on-existing-buildings-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2023-00-parquet/berlin-building-completions-2023-00-12-completions-including-measures-on-existing-buildings-city.parquet)
* [berlin-building-completions-2023-00-12-completions-including-measures-on-existing-buildings-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2023-00-parquet/berlin-building-completions-2023-00-12-completions-including-measures-on-existing-buildings-districts.parquet)
* [berlin-building-completions-2023-00-13-completions-new-buildings-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2023-00-parquet/berlin-building-completions-2023-00-13-completions-new-buildings-city.parquet)
* [berlin-building-completions-2023-00-13-completions-new-buildings-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2023-00-parquet/berlin-building-completions-2023-00-13-completions-new-buildings-districts.parquet)
* [berlin-building-completions-2023-00-14-completions-new-buildings-with-1-or-2-apartments-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2023-00-parquet/berlin-building-completions-2023-00-14-completions-new-buildings-with-1-or-2-apartments-city.parquet)
* [berlin-building-completions-2023-00-14-completions-new-buildings-with-1-or-2-apartments-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2023-00-parquet/berlin-building-completions-2023-00-14-completions-new-buildings-with-1-or-2-apartments-districts.parquet)
* [berlin-building-completions-2023-00-15-completions-new-non-residential-buildings-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2023-00-parquet/berlin-building-completions-2023-00-15-completions-new-non-residential-buildings-city.parquet)
* [berlin-building-completions-2023-00-15-completions-new-non-residential-buildings-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2023-00-parquet/berlin-building-completions-2023-00-15-completions-new-non-residential-buildings-districts.parquet)
* [berlin-building-completions-2023-00-16-construction-backlog-housing-projects-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2023-00-parquet/berlin-building-completions-2023-00-16-construction-backlog-housing-projects-city.parquet)
* [berlin-building-completions-2023-00-16-construction-backlog-housing-projects-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2023-00-parquet/berlin-building-completions-2023-00-16-construction-backlog-housing-projects-districts.parquet)
* [berlin-building-completions-2023-00-17-construction-backlog-apartments-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2023-00-parquet/berlin-building-completions-2023-00-17-construction-backlog-apartments-city.parquet)
* [berlin-building-completions-2023-00-17-construction-backlog-apartments-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2023-00-parquet/berlin-building-completions-2023-00-17-construction-backlog-apartments-districts.parquet)
* [berlin-building-completions-2023-00-18-construction-backlog-non-residential-buildings-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2023-00-parquet/berlin-building-completions-2023-00-18-construction-backlog-non-residential-buildings-city.parquet)
* [berlin-building-completions-2023-00-18-construction-backlog-non-residential-buildings-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2023-00-parquet/berlin-building-completions-2023-00-18-construction-backlog-non-residential-buildings-districts.parquet)
* [berlin-building-completions-2023-00-23-outflow-of-all-buildings-complete-districts-city.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2023-00-parquet/berlin-building-completions-2023-00-23-outflow-of-all-buildings-complete-districts-city.parquet)
* [berlin-building-completions-2023-00-23-outflow-of-all-buildings-complete-districts-districts.parquet](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions-source-aligned/main/data/03-gold/berlin-building-completions-2023-00-parquet/berlin-building-completions-2023-00-23-outflow-of-all-buildings-complete-districts-districts.parquet)

## Classification

**The nature of the exposed data (source-aligned, aggregate, consumer-aligned)**

source-aligned


---
This data product canvas uses the template of [datamesh-architecture.com](https://www.datamesh-architecture.com/data-product-canvas).