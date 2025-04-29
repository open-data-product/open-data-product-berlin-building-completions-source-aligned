
# Data Product Canvas - Berlin Building Completions (source-aligned)

## Metadata

* owner: Open Data Product
* description: Source-aligned data product combining Berlin LOR health and social structure data
* updated: 2025-06-13

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

## Transformation Steps

* [Data extractor](../lib/extract/data_extractor.py) extracts data from inout ports
* [Data copier](../lib/transform/data_copier.py) copies and renames extracted data
* [Data CSV converter](../lib/transform/convert_data_to_csv.py) converts Excel files to CSV format
* [Data aggregator](../lib/transform/aggregate_data.py) aggregates data to be used as output ports

## Output Ports

### Berlin Building Completions 2020 00

* owner: Open Data Product
* url: https://github.com/open-data-product/open-data-product-berlin-building-completions/tree/main/data/02-silver/berlin-building-completions-2020-00
* updated: 2025-06-13

**Files**

* [berlin-building-completions-2020-00-1-completions-new-buildings.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2020-00/berlin-building-completions-2020-00-1-completions-new-buildings.csv)
* [berlin-building-completions-2020-00-10-completions-by-type-and-predominant-building-material.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2020-00/berlin-building-completions-2020-00-10-completions-by-type-and-predominant-building-material.csv)
* [berlin-building-completions-2020-00-11-completions-by-execution.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2020-00/berlin-building-completions-2020-00-11-completions-by-execution.csv)
* [berlin-building-completions-2020-00-12-completions-including-measures-on-existing-buildings.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2020-00/berlin-building-completions-2020-00-12-completions-including-measures-on-existing-buildings.csv)
* [berlin-building-completions-2020-00-13-completions-new-buildings.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2020-00/berlin-building-completions-2020-00-13-completions-new-buildings.csv)
* [berlin-building-completions-2020-00-14-completions-new-buildings-with-1-or-2-apartments.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2020-00/berlin-building-completions-2020-00-14-completions-new-buildings-with-1-or-2-apartments.csv)
* [berlin-building-completions-2020-00-15-completions-new-non-residential-buildings.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2020-00/berlin-building-completions-2020-00-15-completions-new-non-residential-buildings.csv)
* [berlin-building-completions-2020-00-16-construction-backlog-housing-projects-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2020-00/berlin-building-completions-2020-00-16-construction-backlog-housing-projects-districts.csv)
* [berlin-building-completions-2020-00-16-construction-backlog-housing-projects.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2020-00/berlin-building-completions-2020-00-16-construction-backlog-housing-projects.csv)
* [berlin-building-completions-2020-00-17-construction-backlog-apartments-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2020-00/berlin-building-completions-2020-00-17-construction-backlog-apartments-districts.csv)
* [berlin-building-completions-2020-00-17-construction-backlog-apartments.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2020-00/berlin-building-completions-2020-00-17-construction-backlog-apartments.csv)
* [berlin-building-completions-2020-00-18-construction-backlog-non-residential-buildings-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2020-00/berlin-building-completions-2020-00-18-construction-backlog-non-residential-buildings-districts.csv)
* [berlin-building-completions-2020-00-18-construction-backlog-non-residential-buildings.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2020-00/berlin-building-completions-2020-00-18-construction-backlog-non-residential-buildings.csv)
* [berlin-building-completions-2020-00-19-outflow-of-residential-buildings.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2020-00/berlin-building-completions-2020-00-19-outflow-of-residential-buildings.csv)
* [berlin-building-completions-2020-00-2-completions-including-measures-on-existing-buildings.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2020-00/berlin-building-completions-2020-00-2-completions-including-measures-on-existing-buildings.csv)
* [berlin-building-completions-2020-00-20-outflow-of-residential-buildings-complete.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2020-00/berlin-building-completions-2020-00-20-outflow-of-residential-buildings-complete.csv)
* [berlin-building-completions-2020-00-21-outflow-of-non-residential-buildings.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2020-00/berlin-building-completions-2020-00-21-outflow-of-non-residential-buildings.csv)
* [berlin-building-completions-2020-00-22-outflow-of-non-residential-buildings-complete.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2020-00/berlin-building-completions-2020-00-22-outflow-of-non-residential-buildings-complete.csv)
* [berlin-building-completions-2020-00-23-outflow-of-all-buildings-complete-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2020-00/berlin-building-completions-2020-00-23-outflow-of-all-buildings-complete-districts.csv)
* [berlin-building-completions-2020-00-23-outflow-of-all-buildings-complete.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2020-00/berlin-building-completions-2020-00-23-outflow-of-all-buildings-complete.csv)
* [berlin-building-completions-2020-00-3-completions-by-type-and-constructor-including-measures-on-existing-buildings.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2020-00/berlin-building-completions-2020-00-3-completions-by-type-and-constructor-including-measures-on-existing-buildings.csv)
* [berlin-building-completions-2020-00-4-completions-by-type-and-constructor.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2020-00/berlin-building-completions-2020-00-4-completions-by-type-and-constructor.csv)
* [berlin-building-completions-2020-00-5-completions-by-building-type-and-heating.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2020-00/berlin-building-completions-2020-00-5-completions-by-building-type-and-heating.csv)
* [berlin-building-completions-2020-00-6-completions-by-primary-heating-energy.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2020-00/berlin-building-completions-2020-00-6-completions-by-primary-heating-energy.csv)
* [berlin-building-completions-2020-00-7-completions-by-secondary-heating-energy.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2020-00/berlin-building-completions-2020-00-7-completions-by-secondary-heating-energy.csv)
* [berlin-building-completions-2020-00-8-completions-by-primary-water-heating-energy.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2020-00/berlin-building-completions-2020-00-8-completions-by-primary-water-heating-energy.csv)
* [berlin-building-completions-2020-00-9-completions-by-secondary-water-heating-energy.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2020-00/berlin-building-completions-2020-00-9-completions-by-secondary-water-heating-energy.csv)

### Berlin Building Completions 2021 00

* owner: Open Data Product
* url: https://github.com/open-data-product/open-data-product-berlin-building-completions/tree/main/data/02-silver/berlin-building-completions-2021-00
* updated: 2025-06-13

**Files**

* [berlin-building-completions-2021-00-1-completions-new-buildings.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2021-00/berlin-building-completions-2021-00-1-completions-new-buildings.csv)
* [berlin-building-completions-2021-00-10-completions-by-type-and-predominant-building-material.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2021-00/berlin-building-completions-2021-00-10-completions-by-type-and-predominant-building-material.csv)
* [berlin-building-completions-2021-00-11-completions-by-execution.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2021-00/berlin-building-completions-2021-00-11-completions-by-execution.csv)
* [berlin-building-completions-2021-00-12-completions-including-measures-on-existing-buildings.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2021-00/berlin-building-completions-2021-00-12-completions-including-measures-on-existing-buildings.csv)
* [berlin-building-completions-2021-00-13-completions-new-buildings.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2021-00/berlin-building-completions-2021-00-13-completions-new-buildings.csv)
* [berlin-building-completions-2021-00-14-completions-new-buildings-with-1-or-2-apartments.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2021-00/berlin-building-completions-2021-00-14-completions-new-buildings-with-1-or-2-apartments.csv)
* [berlin-building-completions-2021-00-15-completions-new-non-residential-buildings.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2021-00/berlin-building-completions-2021-00-15-completions-new-non-residential-buildings.csv)
* [berlin-building-completions-2021-00-16-construction-backlog-housing-projects-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2021-00/berlin-building-completions-2021-00-16-construction-backlog-housing-projects-districts.csv)
* [berlin-building-completions-2021-00-16-construction-backlog-housing-projects.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2021-00/berlin-building-completions-2021-00-16-construction-backlog-housing-projects.csv)
* [berlin-building-completions-2021-00-17-construction-backlog-apartments-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2021-00/berlin-building-completions-2021-00-17-construction-backlog-apartments-districts.csv)
* [berlin-building-completions-2021-00-17-construction-backlog-apartments.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2021-00/berlin-building-completions-2021-00-17-construction-backlog-apartments.csv)
* [berlin-building-completions-2021-00-18-construction-backlog-non-residential-buildings-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2021-00/berlin-building-completions-2021-00-18-construction-backlog-non-residential-buildings-districts.csv)
* [berlin-building-completions-2021-00-18-construction-backlog-non-residential-buildings.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2021-00/berlin-building-completions-2021-00-18-construction-backlog-non-residential-buildings.csv)
* [berlin-building-completions-2021-00-19-outflow-of-residential-buildings.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2021-00/berlin-building-completions-2021-00-19-outflow-of-residential-buildings.csv)
* [berlin-building-completions-2021-00-2-completions-including-measures-on-existing-buildings.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2021-00/berlin-building-completions-2021-00-2-completions-including-measures-on-existing-buildings.csv)
* [berlin-building-completions-2021-00-20-outflow-of-residential-buildings-complete.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2021-00/berlin-building-completions-2021-00-20-outflow-of-residential-buildings-complete.csv)
* [berlin-building-completions-2021-00-21-outflow-of-non-residential-buildings.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2021-00/berlin-building-completions-2021-00-21-outflow-of-non-residential-buildings.csv)
* [berlin-building-completions-2021-00-22-outflow-of-non-residential-buildings-complete.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2021-00/berlin-building-completions-2021-00-22-outflow-of-non-residential-buildings-complete.csv)
* [berlin-building-completions-2021-00-23-outflow-of-all-buildings-complete-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2021-00/berlin-building-completions-2021-00-23-outflow-of-all-buildings-complete-districts.csv)
* [berlin-building-completions-2021-00-23-outflow-of-all-buildings-complete.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2021-00/berlin-building-completions-2021-00-23-outflow-of-all-buildings-complete.csv)
* [berlin-building-completions-2021-00-3-completions-by-type-and-constructor-including-measures-on-existing-buildings.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2021-00/berlin-building-completions-2021-00-3-completions-by-type-and-constructor-including-measures-on-existing-buildings.csv)
* [berlin-building-completions-2021-00-4-completions-by-type-and-constructor.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2021-00/berlin-building-completions-2021-00-4-completions-by-type-and-constructor.csv)
* [berlin-building-completions-2021-00-5-completions-by-building-type-and-heating.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2021-00/berlin-building-completions-2021-00-5-completions-by-building-type-and-heating.csv)
* [berlin-building-completions-2021-00-6-completions-by-primary-heating-energy.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2021-00/berlin-building-completions-2021-00-6-completions-by-primary-heating-energy.csv)
* [berlin-building-completions-2021-00-7-completions-by-secondary-heating-energy.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2021-00/berlin-building-completions-2021-00-7-completions-by-secondary-heating-energy.csv)
* [berlin-building-completions-2021-00-8-completions-by-primary-water-heating-energy.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2021-00/berlin-building-completions-2021-00-8-completions-by-primary-water-heating-energy.csv)
* [berlin-building-completions-2021-00-9-completions-by-secondary-water-heating-energy.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2021-00/berlin-building-completions-2021-00-9-completions-by-secondary-water-heating-energy.csv)

### Berlin Building Completions 2022 00

* owner: Open Data Product
* url: https://github.com/open-data-product/open-data-product-berlin-building-completions/tree/main/data/02-silver/berlin-building-completions-2022-00
* updated: 2025-06-13

**Files**

* [berlin-building-completions-2022-00-1-completions-new-buildings.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2022-00/berlin-building-completions-2022-00-1-completions-new-buildings.csv)
* [berlin-building-completions-2022-00-10-completions-by-type-and-predominant-building-material.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2022-00/berlin-building-completions-2022-00-10-completions-by-type-and-predominant-building-material.csv)
* [berlin-building-completions-2022-00-11-completions-by-execution.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2022-00/berlin-building-completions-2022-00-11-completions-by-execution.csv)
* [berlin-building-completions-2022-00-12-completions-including-measures-on-existing-buildings.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2022-00/berlin-building-completions-2022-00-12-completions-including-measures-on-existing-buildings.csv)
* [berlin-building-completions-2022-00-13-completions-new-buildings.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2022-00/berlin-building-completions-2022-00-13-completions-new-buildings.csv)
* [berlin-building-completions-2022-00-14-completions-new-buildings-with-1-or-2-apartments.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2022-00/berlin-building-completions-2022-00-14-completions-new-buildings-with-1-or-2-apartments.csv)
* [berlin-building-completions-2022-00-15-completions-new-non-residential-buildings.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2022-00/berlin-building-completions-2022-00-15-completions-new-non-residential-buildings.csv)
* [berlin-building-completions-2022-00-16-construction-backlog-housing-projects-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2022-00/berlin-building-completions-2022-00-16-construction-backlog-housing-projects-districts.csv)
* [berlin-building-completions-2022-00-16-construction-backlog-housing-projects.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2022-00/berlin-building-completions-2022-00-16-construction-backlog-housing-projects.csv)
* [berlin-building-completions-2022-00-17-construction-backlog-apartments-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2022-00/berlin-building-completions-2022-00-17-construction-backlog-apartments-districts.csv)
* [berlin-building-completions-2022-00-17-construction-backlog-apartments.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2022-00/berlin-building-completions-2022-00-17-construction-backlog-apartments.csv)
* [berlin-building-completions-2022-00-18-construction-backlog-non-residential-buildings-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2022-00/berlin-building-completions-2022-00-18-construction-backlog-non-residential-buildings-districts.csv)
* [berlin-building-completions-2022-00-18-construction-backlog-non-residential-buildings.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2022-00/berlin-building-completions-2022-00-18-construction-backlog-non-residential-buildings.csv)
* [berlin-building-completions-2022-00-19-outflow-of-residential-buildings.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2022-00/berlin-building-completions-2022-00-19-outflow-of-residential-buildings.csv)
* [berlin-building-completions-2022-00-2-completions-including-measures-on-existing-buildings.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2022-00/berlin-building-completions-2022-00-2-completions-including-measures-on-existing-buildings.csv)
* [berlin-building-completions-2022-00-20-outflow-of-residential-buildings-complete.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2022-00/berlin-building-completions-2022-00-20-outflow-of-residential-buildings-complete.csv)
* [berlin-building-completions-2022-00-21-outflow-of-non-residential-buildings.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2022-00/berlin-building-completions-2022-00-21-outflow-of-non-residential-buildings.csv)
* [berlin-building-completions-2022-00-22-outflow-of-non-residential-buildings-complete.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2022-00/berlin-building-completions-2022-00-22-outflow-of-non-residential-buildings-complete.csv)
* [berlin-building-completions-2022-00-23-outflow-of-all-buildings-complete-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2022-00/berlin-building-completions-2022-00-23-outflow-of-all-buildings-complete-districts.csv)
* [berlin-building-completions-2022-00-23-outflow-of-all-buildings-complete.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2022-00/berlin-building-completions-2022-00-23-outflow-of-all-buildings-complete.csv)
* [berlin-building-completions-2022-00-3-completions-by-type-and-constructor-including-measures-on-existing-buildings.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2022-00/berlin-building-completions-2022-00-3-completions-by-type-and-constructor-including-measures-on-existing-buildings.csv)
* [berlin-building-completions-2022-00-4-completions-by-type-and-constructor.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2022-00/berlin-building-completions-2022-00-4-completions-by-type-and-constructor.csv)
* [berlin-building-completions-2022-00-5-completions-by-building-type-and-heating.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2022-00/berlin-building-completions-2022-00-5-completions-by-building-type-and-heating.csv)
* [berlin-building-completions-2022-00-6-completions-by-primary-heating-energy.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2022-00/berlin-building-completions-2022-00-6-completions-by-primary-heating-energy.csv)
* [berlin-building-completions-2022-00-7-completions-by-secondary-heating-energy.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2022-00/berlin-building-completions-2022-00-7-completions-by-secondary-heating-energy.csv)
* [berlin-building-completions-2022-00-8-completions-by-primary-water-heating-energy.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2022-00/berlin-building-completions-2022-00-8-completions-by-primary-water-heating-energy.csv)
* [berlin-building-completions-2022-00-9-completions-by-secondary-water-heating-energy.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/02-silver/berlin-building-completions-2022-00/berlin-building-completions-2022-00-9-completions-by-secondary-water-heating-energy.csv)

### Berlin Building Completions 2020 00

* owner: Open Data Product
* url: https://github.com/open-data-product/open-data-product-berlin-building-completions/tree/main/data/03-gold/berlin-building-completions-2020-00
* updated: 2025-06-13

**Files**

* [berlin-building-completions-2020-00-12-completions-including-measures-on-existing-buildings-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2020-00/berlin-building-completions-2020-00-12-completions-including-measures-on-existing-buildings-city.csv)
* [berlin-building-completions-2020-00-12-completions-including-measures-on-existing-buildings-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2020-00/berlin-building-completions-2020-00-12-completions-including-measures-on-existing-buildings-districts.csv)
* [berlin-building-completions-2020-00-13-completions-new-buildings-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2020-00/berlin-building-completions-2020-00-13-completions-new-buildings-city.csv)
* [berlin-building-completions-2020-00-13-completions-new-buildings-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2020-00/berlin-building-completions-2020-00-13-completions-new-buildings-districts.csv)
* [berlin-building-completions-2020-00-14-completions-new-buildings-with-1-or-2-apartments-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2020-00/berlin-building-completions-2020-00-14-completions-new-buildings-with-1-or-2-apartments-city.csv)
* [berlin-building-completions-2020-00-14-completions-new-buildings-with-1-or-2-apartments-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2020-00/berlin-building-completions-2020-00-14-completions-new-buildings-with-1-or-2-apartments-districts.csv)
* [berlin-building-completions-2020-00-15-completions-new-non-residential-buildings-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2020-00/berlin-building-completions-2020-00-15-completions-new-non-residential-buildings-city.csv)
* [berlin-building-completions-2020-00-15-completions-new-non-residential-buildings-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2020-00/berlin-building-completions-2020-00-15-completions-new-non-residential-buildings-districts.csv)
* [berlin-building-completions-2020-00-16-construction-backlog-housing-projects-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2020-00/berlin-building-completions-2020-00-16-construction-backlog-housing-projects-city.csv)
* [berlin-building-completions-2020-00-16-construction-backlog-housing-projects-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2020-00/berlin-building-completions-2020-00-16-construction-backlog-housing-projects-districts.csv)
* [berlin-building-completions-2020-00-17-construction-backlog-apartments-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2020-00/berlin-building-completions-2020-00-17-construction-backlog-apartments-city.csv)
* [berlin-building-completions-2020-00-17-construction-backlog-apartments-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2020-00/berlin-building-completions-2020-00-17-construction-backlog-apartments-districts.csv)
* [berlin-building-completions-2020-00-18-construction-backlog-non-residential-buildings-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2020-00/berlin-building-completions-2020-00-18-construction-backlog-non-residential-buildings-city.csv)
* [berlin-building-completions-2020-00-18-construction-backlog-non-residential-buildings-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2020-00/berlin-building-completions-2020-00-18-construction-backlog-non-residential-buildings-districts.csv)
* [berlin-building-completions-2020-00-23-outflow-of-all-buildings-complete-districts-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2020-00/berlin-building-completions-2020-00-23-outflow-of-all-buildings-complete-districts-city.csv)
* [berlin-building-completions-2020-00-23-outflow-of-all-buildings-complete-districts-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2020-00/berlin-building-completions-2020-00-23-outflow-of-all-buildings-complete-districts-districts.csv)

### Berlin Building Completions 2021 00

* owner: Open Data Product
* url: https://github.com/open-data-product/open-data-product-berlin-building-completions/tree/main/data/03-gold/berlin-building-completions-2021-00
* updated: 2025-06-13

**Files**

* [berlin-building-completions-2021-00-12-completions-including-measures-on-existing-buildings-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2021-00/berlin-building-completions-2021-00-12-completions-including-measures-on-existing-buildings-city.csv)
* [berlin-building-completions-2021-00-12-completions-including-measures-on-existing-buildings-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2021-00/berlin-building-completions-2021-00-12-completions-including-measures-on-existing-buildings-districts.csv)
* [berlin-building-completions-2021-00-13-completions-new-buildings-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2021-00/berlin-building-completions-2021-00-13-completions-new-buildings-city.csv)
* [berlin-building-completions-2021-00-13-completions-new-buildings-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2021-00/berlin-building-completions-2021-00-13-completions-new-buildings-districts.csv)
* [berlin-building-completions-2021-00-14-completions-new-buildings-with-1-or-2-apartments-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2021-00/berlin-building-completions-2021-00-14-completions-new-buildings-with-1-or-2-apartments-city.csv)
* [berlin-building-completions-2021-00-14-completions-new-buildings-with-1-or-2-apartments-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2021-00/berlin-building-completions-2021-00-14-completions-new-buildings-with-1-or-2-apartments-districts.csv)
* [berlin-building-completions-2021-00-15-completions-new-non-residential-buildings-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2021-00/berlin-building-completions-2021-00-15-completions-new-non-residential-buildings-city.csv)
* [berlin-building-completions-2021-00-15-completions-new-non-residential-buildings-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2021-00/berlin-building-completions-2021-00-15-completions-new-non-residential-buildings-districts.csv)
* [berlin-building-completions-2021-00-16-construction-backlog-housing-projects-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2021-00/berlin-building-completions-2021-00-16-construction-backlog-housing-projects-city.csv)
* [berlin-building-completions-2021-00-16-construction-backlog-housing-projects-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2021-00/berlin-building-completions-2021-00-16-construction-backlog-housing-projects-districts.csv)
* [berlin-building-completions-2021-00-17-construction-backlog-apartments-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2021-00/berlin-building-completions-2021-00-17-construction-backlog-apartments-city.csv)
* [berlin-building-completions-2021-00-17-construction-backlog-apartments-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2021-00/berlin-building-completions-2021-00-17-construction-backlog-apartments-districts.csv)
* [berlin-building-completions-2021-00-18-construction-backlog-non-residential-buildings-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2021-00/berlin-building-completions-2021-00-18-construction-backlog-non-residential-buildings-city.csv)
* [berlin-building-completions-2021-00-18-construction-backlog-non-residential-buildings-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2021-00/berlin-building-completions-2021-00-18-construction-backlog-non-residential-buildings-districts.csv)
* [berlin-building-completions-2021-00-23-outflow-of-all-buildings-complete-districts-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2021-00/berlin-building-completions-2021-00-23-outflow-of-all-buildings-complete-districts-city.csv)
* [berlin-building-completions-2021-00-23-outflow-of-all-buildings-complete-districts-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2021-00/berlin-building-completions-2021-00-23-outflow-of-all-buildings-complete-districts-districts.csv)

### Berlin Building Completions 2022 00

* owner: Open Data Product
* url: https://github.com/open-data-product/open-data-product-berlin-building-completions/tree/main/data/03-gold/berlin-building-completions-2022-00
* updated: 2025-06-13

**Files**

* [berlin-building-completions-2022-00-12-completions-including-measures-on-existing-buildings-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2022-00/berlin-building-completions-2022-00-12-completions-including-measures-on-existing-buildings-city.csv)
* [berlin-building-completions-2022-00-12-completions-including-measures-on-existing-buildings-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2022-00/berlin-building-completions-2022-00-12-completions-including-measures-on-existing-buildings-districts.csv)
* [berlin-building-completions-2022-00-13-completions-new-buildings-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2022-00/berlin-building-completions-2022-00-13-completions-new-buildings-city.csv)
* [berlin-building-completions-2022-00-13-completions-new-buildings-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2022-00/berlin-building-completions-2022-00-13-completions-new-buildings-districts.csv)
* [berlin-building-completions-2022-00-14-completions-new-buildings-with-1-or-2-apartments-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2022-00/berlin-building-completions-2022-00-14-completions-new-buildings-with-1-or-2-apartments-city.csv)
* [berlin-building-completions-2022-00-14-completions-new-buildings-with-1-or-2-apartments-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2022-00/berlin-building-completions-2022-00-14-completions-new-buildings-with-1-or-2-apartments-districts.csv)
* [berlin-building-completions-2022-00-15-completions-new-non-residential-buildings-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2022-00/berlin-building-completions-2022-00-15-completions-new-non-residential-buildings-city.csv)
* [berlin-building-completions-2022-00-15-completions-new-non-residential-buildings-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2022-00/berlin-building-completions-2022-00-15-completions-new-non-residential-buildings-districts.csv)
* [berlin-building-completions-2022-00-16-construction-backlog-housing-projects-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2022-00/berlin-building-completions-2022-00-16-construction-backlog-housing-projects-city.csv)
* [berlin-building-completions-2022-00-16-construction-backlog-housing-projects-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2022-00/berlin-building-completions-2022-00-16-construction-backlog-housing-projects-districts.csv)
* [berlin-building-completions-2022-00-17-construction-backlog-apartments-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2022-00/berlin-building-completions-2022-00-17-construction-backlog-apartments-city.csv)
* [berlin-building-completions-2022-00-17-construction-backlog-apartments-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2022-00/berlin-building-completions-2022-00-17-construction-backlog-apartments-districts.csv)
* [berlin-building-completions-2022-00-18-construction-backlog-non-residential-buildings-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2022-00/berlin-building-completions-2022-00-18-construction-backlog-non-residential-buildings-city.csv)
* [berlin-building-completions-2022-00-18-construction-backlog-non-residential-buildings-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2022-00/berlin-building-completions-2022-00-18-construction-backlog-non-residential-buildings-districts.csv)
* [berlin-building-completions-2022-00-23-outflow-of-all-buildings-complete-districts-city.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2022-00/berlin-building-completions-2022-00-23-outflow-of-all-buildings-complete-districts-city.csv)
* [berlin-building-completions-2022-00-23-outflow-of-all-buildings-complete-districts-districts.csv](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-building-completions/main/data/03-gold/berlin-building-completions-2022-00/berlin-building-completions-2022-00-23-outflow-of-all-buildings-complete-districts-districts.csv)

## Classification

**The nature of the exposed data (source-aligned, aggregate, consumer-aligned)**

source-aligned


---
This data product canvas uses the template of [datamesh-architecture.com](https://www.datamesh-architecture.com/data-product-canvas).