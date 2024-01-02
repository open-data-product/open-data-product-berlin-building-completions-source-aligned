# Data Product Canvas

## Domain

## Data Product Name

## Input Ports

**Input ports define the format and protocol in which data can be read (database, file, API, visualizations)**

This data product uses statistical population data provided
by [Amt für Statistik Berlin-Brandenburg](https://www.statistik-berlin-brandenburg.de/) available under the following
URLs

* [SB_F02-02-00_2022j01_BE.xlsx](https://download.statistik-berlin-brandenburg.de/2bd07d614def86bb/6dba9f3eaa0a/SB_F02-02-00_2022j01_BE.xlsx)
* [SB_F02-02-00_2021j01_BE.xlsx](https://download.statistik-berlin-brandenburg.de/d712acdbe5af5c59/885f96bb0c20/SB_F02-02-00_2021j01_BE.xlsx)
* [SB_F02-02-00_2020j01_BE.xlsx](https://download.statistik-berlin-brandenburg.de/629351f64cf37f48/60bed0ed87bb/SB_F02-02-00_2020j01_BE.xlsx)

## Data Product Design

**Describe everything you need to design a data product on a conceptual level.**
**Ingestion, storage, transport, wrangling, cleaning, transformations, enrichment, augmentation, analytics, SQL
statements, or used data platform services.**

This data product

* [converts Excel data into csv](../lib/transform/data_csv_converter.py)

## Output Port

**Output ports define the format and protocol in which data can be exposed (db, file, API, visualizations)**

The data of this data product is available under the following URLs

* [berlin-building-completion-2020-00/berlin-building-completion-2020-00-1-completions-new-buildings.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2020-00/berlin-building-completion-2020-00-1-completions-new-buildings.csv)
* [berlin-building-completion-2020-00/berlin-building-completion-2020-00-2-completions-including-measures-on-existing-buildings.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2020-00/berlin-building-completion-2020-00-2-completions-including-measures-on-existing-buildings.csv)
* [berlin-building-completion-2020-00/berlin-building-completion-2020-00-3-completions-by-type-and-constructor-including-measures-on-existing-buildings.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2020-00/berlin-building-completion-2020-00-3-completions-by-type-and-constructor-including-measures-on-existing-buildings.csv)
* [berlin-building-completion-2020-00/berlin-building-completion-2020-00-4-completions-by-type-and-constructor.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2020-00/berlin-building-completion-2020-00-4-completions-by-type-and-constructor.csv)
* [berlin-building-completion-2020-00/berlin-building-completion-2020-00-5-completions-by-building-type-and-heating.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2020-00/berlin-building-completion-2020-00-5-completions-by-building-type-and-heating.csv)
* [berlin-building-completion-2020-00/berlin-building-completion-2020-00-6-completions-by-primary-heating-energy.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2020-00/berlin-building-completion-2020-00-6-completions-by-primary-heating-energy.csv)
* [berlin-building-completion-2020-00/berlin-building-completion-2020-00-7-completions-by-secondary-heating-energy.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2020-00/berlin-building-completion-2020-00-7-completions-by-secondary-heating-energy.csv)
* [berlin-building-completion-2020-00/berlin-building-completion-2020-00-8-completions-by-primary-water-heating-energy.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2020-00/berlin-building-completion-2020-00-8-completions-by-primary-water-heating-energy.csv)
* [berlin-building-completion-2020-00/berlin-building-completion-2020-00-9-completions-by-secondary-water-heating-energy.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2020-00/berlin-building-completion-2020-00-9-completions-by-secondary-water-heating-energy.csv)
* [berlin-building-completion-2020-00/berlin-building-completion-2020-00-10-completions-by-type-and-predominant-building-material.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2020-00/berlin-building-completion-2020-00-10-completions-by-type-and-predominant-building-material.csv)
* [berlin-building-completion-2020-00/berlin-building-completion-2020-00-11-completions-by-execution.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2020-00/berlin-building-completion-2020-00-11-completions-by-execution.csv)
* [berlin-building-completion-2020-00/berlin-building-completion-2020-00-12-completions-by-district-including-measures-on-existing-buildings.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2020-00/berlin-building-completion-2020-00-12-completions-by-district-including-measures-on-existing-buildings.csv)
* [berlin-building-completion-2020-00/berlin-building-completion-2020-00-13-completions-by-district-new-buildings.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2020-00/berlin-building-completion-2020-00-13-completions-by-district-new-buildings.csv)
* [berlin-building-completion-2020-00/berlin-building-completion-2020-00-14-completions-by-district-new-buildings-with-1-or-2-apartments.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2020-00/berlin-building-completion-2020-00-14-completions-by-district-new-buildings-with-1-or-2-apartments.csv)
* [berlin-building-completion-2020-00/berlin-building-completion-2020-00-15-completions-by-district-new-non-residential-buildings.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2020-00/berlin-building-completion-2020-00-15-completions-by-district-new-non-residential-buildings.csv)
* [berlin-building-completion-2020-00/berlin-building-completion-2020-00-16-construction-backlog-housing-projects.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2020-00/berlin-building-completion-2020-00-16-construction-backlog-housing-projects.csv)
* [berlin-building-completion-2020-00/berlin-building-completion-2020-00-17-construction-backlog-apartments.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2020-00/berlin-building-completion-2020-00-17-construction-backlog-apartments.csv)
* [berlin-building-completion-2020-00/berlin-building-completion-2020-00-18-construction-backlog-non-residential-buildings.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2020-00/berlin-building-completion-2020-00-18-construction-backlog-non-residential-buildings.csv)
* [berlin-building-completion-2020-00/berlin-building-completion-2020-00-19-outflow-of-residential-buildings.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2020-00/berlin-building-completion-2020-00-19-outflow-of-residential-buildings.csv)
* [berlin-building-completion-2020-00/berlin-building-completion-2020-00-20-outflow-of-residential-buildings-complete.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2020-00/berlin-building-completion-2020-00-20-outflow-of-residential-buildings-complete.csv)
* [berlin-building-completion-2020-00/berlin-building-completion-2020-00-21-outflow-of-non-residential-buildings.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2020-00/berlin-building-completion-2020-00-21-outflow-of-non-residential-buildings.csv)
* [berlin-building-completion-2020-00/berlin-building-completion-2020-00-22-outflow-of-non-residential-buildings-complete.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2020-00/berlin-building-completion-2020-00-22-outflow-of-non-residential-buildings-complete.csv)
* [berlin-building-completion-2020-00/berlin-building-completion-2020-00-23-outflow-of-all-buildings-complete.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2020-00/berlin-building-completion-2020-00-23-outflow-of-all-buildings-complete.csv)
* [berlin-building-completion-2021-00/berlin-building-completion-2021-00-1-completions-new-buildings.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2021-00/berlin-building-completion-2021-00-1-completions-new-buildings.csv)
* [berlin-building-completion-2021-00/berlin-building-completion-2021-00-2-completions-including-measures-on-existing-buildings.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2021-00/berlin-building-completion-2021-00-2-completions-including-measures-on-existing-buildings.csv)
* [berlin-building-completion-2021-00/berlin-building-completion-2021-00-3-completions-by-type-and-constructor-including-measures-on-existing-buildings.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2021-00/berlin-building-completion-2021-00-3-completions-by-type-and-constructor-including-measures-on-existing-buildings.csv)
* [berlin-building-completion-2021-00/berlin-building-completion-2021-00-4-completions-by-type-and-constructor.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2021-00/berlin-building-completion-2021-00-4-completions-by-type-and-constructor.csv)
* [berlin-building-completion-2021-00/berlin-building-completion-2021-00-5-completions-by-building-type-and-heating.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2021-00/berlin-building-completion-2021-00-5-completions-by-building-type-and-heating.csv)
* [berlin-building-completion-2021-00/berlin-building-completion-2021-00-6-completions-by-primary-heating-energy.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2021-00/berlin-building-completion-2021-00-6-completions-by-primary-heating-energy.csv)
* [berlin-building-completion-2021-00/berlin-building-completion-2021-00-7-completions-by-secondary-heating-energy.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2021-00/berlin-building-completion-2021-00-7-completions-by-secondary-heating-energy.csv)
* [berlin-building-completion-2021-00/berlin-building-completion-2021-00-8-completions-by-primary-water-heating-energy.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2021-00/berlin-building-completion-2021-00-8-completions-by-primary-water-heating-energy.csv)
* [berlin-building-completion-2021-00/berlin-building-completion-2021-00-9-completions-by-secondary-water-heating-energy.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2021-00/berlin-building-completion-2021-00-9-completions-by-secondary-water-heating-energy.csv)
* [berlin-building-completion-2021-00/berlin-building-completion-2021-00-10-completions-by-type-and-predominant-building-material.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2021-00/berlin-building-completion-2021-00-10-completions-by-type-and-predominant-building-material.csv)
* [berlin-building-completion-2021-00/berlin-building-completion-2021-00-11-completions-by-execution.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2021-00/berlin-building-completion-2021-00-11-completions-by-execution.csv)
* [berlin-building-completion-2021-00/berlin-building-completion-2021-00-12-completions-by-district-including-measures-on-existing-buildings.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2021-00/berlin-building-completion-2021-00-12-completions-by-district-including-measures-on-existing-buildings.csv)
* [berlin-building-completion-2021-00/berlin-building-completion-2021-00-13-completions-by-district-new-buildings.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2021-00/berlin-building-completion-2021-00-13-completions-by-district-new-buildings.csv)
* [berlin-building-completion-2021-00/berlin-building-completion-2021-00-14-completions-by-district-new-buildings-with-1-or-2-apartments.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2021-00/berlin-building-completion-2021-00-14-completions-by-district-new-buildings-with-1-or-2-apartments.csv)
* [berlin-building-completion-2021-00/berlin-building-completion-2021-00-15-completions-by-district-new-non-residential-buildings.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2021-00/berlin-building-completion-2021-00-15-completions-by-district-new-non-residential-buildings.csv)
* [berlin-building-completion-2021-00/berlin-building-completion-2021-00-16-construction-backlog-housing-projects.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2021-00/berlin-building-completion-2021-00-16-construction-backlog-housing-projects.csv)
* [berlin-building-completion-2021-00/berlin-building-completion-2021-00-17-construction-backlog-apartments.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2021-00/berlin-building-completion-2021-00-17-construction-backlog-apartments.csv)
* [berlin-building-completion-2021-00/berlin-building-completion-2021-00-18-construction-backlog-non-residential-buildings.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2021-00/berlin-building-completion-2021-00-18-construction-backlog-non-residential-buildings.csv)
* [berlin-building-completion-2021-00/berlin-building-completion-2021-00-19-outflow-of-residential-buildings.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2021-00/berlin-building-completion-2021-00-19-outflow-of-residential-buildings.csv)
* [berlin-building-completion-2021-00/berlin-building-completion-2021-00-20-outflow-of-residential-buildings-complete.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2021-00/berlin-building-completion-2021-00-20-outflow-of-residential-buildings-complete.csv)
* [berlin-building-completion-2021-00/berlin-building-completion-2021-00-21-outflow-of-non-residential-buildings.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2021-00/berlin-building-completion-2021-00-21-outflow-of-non-residential-buildings.csv)
* [berlin-building-completion-2021-00/berlin-building-completion-2021-00-22-outflow-of-non-residential-buildings-complete.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2021-00/berlin-building-completion-2021-00-22-outflow-of-non-residential-buildings-complete.csv)
* [berlin-building-completion-2021-00/berlin-building-completion-2021-00-23-outflow-of-all-buildings-complete.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2021-00/berlin-building-completion-2021-00-23-outflow-of-all-buildings-complete.csv)
* [berlin-building-completion-2022-00/berlin-building-completion-2022-00-1-completions-new-buildings.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2022-00/berlin-building-completion-2022-00-1-completions-new-buildings.csv)
* [berlin-building-completion-2022-00/berlin-building-completion-2022-00-2-completions-including-measures-on-existing-buildings.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2022-00/berlin-building-completion-2022-00-2-completions-including-measures-on-existing-buildings.csv)
* [berlin-building-completion-2022-00/berlin-building-completion-2022-00-3-completions-by-type-and-constructor-including-measures-on-existing-buildings.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2022-00/berlin-building-completion-2022-00-3-completions-by-type-and-constructor-including-measures-on-existing-buildings.csv)
* [berlin-building-completion-2022-00/berlin-building-completion-2022-00-4-completions-by-type-and-constructor.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2022-00/berlin-building-completion-2022-00-4-completions-by-type-and-constructor.csv)
* [berlin-building-completion-2022-00/berlin-building-completion-2022-00-5-completions-by-building-type-and-heating.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2022-00/berlin-building-completion-2022-00-5-completions-by-building-type-and-heating.csv)
* [berlin-building-completion-2022-00/berlin-building-completion-2022-00-6-completions-by-primary-heating-energy.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2022-00/berlin-building-completion-2022-00-6-completions-by-primary-heating-energy.csv)
* [berlin-building-completion-2022-00/berlin-building-completion-2022-00-7-completions-by-secondary-heating-energy.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2022-00/berlin-building-completion-2022-00-7-completions-by-secondary-heating-energy.csv)
* [berlin-building-completion-2022-00/berlin-building-completion-2022-00-8-completions-by-primary-water-heating-energy.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2022-00/berlin-building-completion-2022-00-8-completions-by-primary-water-heating-energy.csv)
* [berlin-building-completion-2022-00/berlin-building-completion-2022-00-9-completions-by-secondary-water-heating-energy.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2022-00/berlin-building-completion-2022-00-9-completions-by-secondary-water-heating-energy.csv)
* [berlin-building-completion-2022-00/berlin-building-completion-2022-00-10-completions-by-type-and-predominant-building-material.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2022-00/berlin-building-completion-2022-00-10-completions-by-type-and-predominant-building-material.csv)
* [berlin-building-completion-2022-00/berlin-building-completion-2022-00-11-completions-by-execution.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2022-00/berlin-building-completion-2022-00-11-completions-by-execution.csv)
* [berlin-building-completion-2022-00/berlin-building-completion-2022-00-12-completions-by-district-including-measures-on-existing-buildings.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2022-00/berlin-building-completion-2022-00-12-completions-by-district-including-measures-on-existing-buildings.csv)
* [berlin-building-completion-2022-00/berlin-building-completion-2022-00-13-completions-by-district-new-buildings.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2022-00/berlin-building-completion-2022-00-13-completions-by-district-new-buildings.csv)
* [berlin-building-completion-2022-00/berlin-building-completion-2022-00-14-completions-by-district-new-buildings-with-1-or-2-apartments.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2022-00/berlin-building-completion-2022-00-14-completions-by-district-new-buildings-with-1-or-2-apartments.csv)
* [berlin-building-completion-2022-00/berlin-building-completion-2022-00-15-completions-by-district-new-non-residential-buildings.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2022-00/berlin-building-completion-2022-00-15-completions-by-district-new-non-residential-buildings.csv)
* [berlin-building-completion-2022-00/berlin-building-completion-2022-00-16-construction-backlog-housing-projects.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2022-00/berlin-building-completion-2022-00-16-construction-backlog-housing-projects.csv)
* [berlin-building-completion-2022-00/berlin-building-completion-2022-00-17-construction-backlog-apartments.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2022-00/berlin-building-completion-2022-00-17-construction-backlog-apartments.csv)
* [berlin-building-completion-2022-00/berlin-building-completion-2022-00-18-construction-backlog-non-residential-buildings.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2022-00/berlin-building-completion-2022-00-18-construction-backlog-non-residential-buildings.csv)
* [berlin-building-completion-2022-00/berlin-building-completion-2022-00-19-outflow-of-residential-buildings.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2022-00/berlin-building-completion-2022-00-19-outflow-of-residential-buildings.csv)
* [berlin-building-completion-2022-00/berlin-building-completion-2022-00-20-outflow-of-residential-buildings-complete.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2022-00/berlin-building-completion-2022-00-20-outflow-of-residential-buildings-complete.csv)
* [berlin-building-completion-2022-00/berlin-building-completion-2022-00-21-outflow-of-non-residential-buildings.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2022-00/berlin-building-completion-2022-00-21-outflow-of-non-residential-buildings.csv)
* [berlin-building-completion-2022-00/berlin-building-completion-2022-00-22-outflow-of-non-residential-buildings-complete.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2022-00/berlin-building-completion-2022-00-22-outflow-of-non-residential-buildings-complete.csv)
* [berlin-building-completion-2022-00/berlin-building-completion-2022-00-23-outflow-of-all-buildings-complete.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-completions-source-aligned/main/data/berlin-building-completion-2022-00/berlin-building-completion-2022-00-23-outflow-of-all-buildings-complete.csv)

## Metadata

### Ownership

**Domain, data product owner, organizational unit, license, version and expiration date**

* ownership: Open Lifeworlds
* domain: statistics
* license: CC-BY-4.0

### Schema

**Attributes, data types, constraints, and relationships to other elements**

### Semantics

**Description, logical model**

#### 1 completions new buildings
- `year`: year
- `building_completion_total`: number of building completions
- `building_completion_residential_buildings`: number of building completions (residential buildings)
- `building_completion_non_residential_buildings`: number of building completions (non-residential buildings)
- `building_measure_on_existing_buildings`: number of building measures in existing buildings
- `usage_area`: building completions usage area in 100sqm
- `living_area`: building completions living area 100sqm
- `apartments`: number of apartments
- `apartment_rooms`: number of living rooms
- `estimated_costs`: estimated costs
#### 2 completions including measures on existing buildings
- `building_completions_new`: number of new building completions
- `building_completions_new_with_1_apartment`: number of new building completions with 1 apartment
- `building_completions_new_with_2_apartments`: number of new building completions with 2 apartments
- `building_completions_new_with_3_or_more_apartment`: number of new building completions with 3 or more apartments
- `building_completions_new_total_apartments`: number of
- `building_completions_new_volume`: volume of apartments in 1000qm
- `building_completions_new_living_area`: living area in 100sqm
- `building_completions_new_estimated_costs`: estimated costs
- `apartments_in_new_non_residential_buildings`: apartments in new non-residential buildings
#### 3 completions by type and constructor including measures on existing buildings +  4 completions by type and constructor
- `type`: type
- `measures`: number of measures
- `usage_area`: usage area in 100sqm
- `apartments`: number of apartments
- `living_area`: living are in 100sqm
- `living_rooms`: number of living rooms
- `estimated_costs`: estimated costs
#### 5 completions by building type and heating
- `type`: type
- `buildings`: number of buildings
- `district_heating`: number of buildings with district heating
- `block_heating`: number of buildings with block heating
- `central_heating`: number of buildings with central heating
- `floor_heating`: number of buildings with floor heating
- `single_room_heating`: number of buildings with single room heating
- `without_heating`: number of buildings without heating4
#### 6 completions by primary heating energy + 7 completions by secondary heating energy + 8 completions by primary water heating energy + completions by secondary water heating energy
- `type`: type
- `buildings`: number of buildings
- `oil`: number of buildings with oil heating
- `gas`: number of buildings with gas heating
- `electricity`: number of buildings with electric heating
- `district_heating`: number of buildings with district heating
- `geothermal_energy`: number of buildings with geothermal energy heating
- `environmental_thermal_energy`: number of buildings with environmental thermal energy heating
- `solar_thermal_energy`: number of buildings with solar thermal energy heating
- `wood`: number of buildings with wood heating
- `biogas_bio_methane`: number of buildings with biogas or bio methane heating
- `other_bio_mass`: number of buildings with other bio mass heating
- `other_heating`: number of buildings with other heating heating
- `no_heating`: number of buildings with no heating heating
- `conventional_energy`: number of buildings with conventional energy heating
- `renewable_energy`: number of buildings with renewable energy heating
#### 10 completions by predominant building material
- `type`: type
- `buildings`: number of buildings
- `steel`: steel
- `reinforced_concrete`: reinforced concrete
- `bricks`: bricks
- `sand_lime_bricks`: sand lime bricks
- `aerated_concrete`: aerated concrete
- `light_concrete`: light concrete
- `wood`: wood
- `other`: other
#### 11 completions by execution time
- `type`: type
- `unit`: unit
- `buildings`: number of buildings
- `execution_time_between_6_12_months`:  execution time between 6 12 months
- `execution_time_between_12_18_months`: execution time between 12 and 18 months
- `execution_time_between_18_24_months`: execution time between 18 and 24 months
- `execution_time_between_24_30_months`: execution time between 24 and 30 months
- `execution_time_between_30_36_months`: execution time between 30 and 36 months
- `execution_time_above_36_months`: execution time above 36 months
#### 12 completions by district including measures on existing buildings + 13 completions by districts new buildings
- `buildings`: number of buildings
- `usage_area`: buildings usage area in 100sqm
- `apartments`: number of apartments
- `apartments_usage_area`: apartments usage area in 100sqm
- `estimated_costs`: estimated costs
#### 14 completions by district new buildings with 1 or 2 apartments + 15 completions by district new non-residential buildings
- `buildings`: number of buildings
- `volume`: buildings volume in 1000qm
- `usage_area`: buildings usage are in 100sqm
- `apartments`: number of apartments
- `apartments_usage_area`: apartments usage are in 100sqm
- `estimated_costs`: estimated costs
#### 16 construction backlog housing projects + 17 construction backlog apartments + 18 construction backlog non-residential buildings
- `type`: type
- `backlog_total`: backlog total
- `backlog_new_buildings`: backlog of new buildings
- `backlog_new_buildings_under_roof`: backlog of new buildings under roof
- `backlog_new_buildings_not_yet_under_roof`: backlog of new buildings not yet under roof
- `backlog_new_buildings_not_yet_started`: backlog of new buildings not yet started
- `expired_building_permits`: expired_building_permits
#### 19 outflow of residential buildings + 20 outflow of residential buildings complete + 21 outflow of non-residential buildings + 22 outflow of non-residential buildings-complete
- `type`: type
- `buildings`: number of buildings
- `usage_area`: usage area in 1000sqm
- `living_area`: living area in 1000sqm
- `apartments`: number of apartments
#### 23 outflow of complete buildings
- `residential_buildings`: residential_buildings
- `residential_buildings_apartments`: number of apartments in non-residential buildings
- `residential_buildings_usage_area`: usage area residential buildings
- `non_residential_buildings`: number of non-residential buildings
- `non_residential_buildings_apartments`: number of apartments in non-residential buildings
- `non_residential_buildings_usage_area`: usage area non-residential buildings

### Security

**Security rules applied to the data product usage e.g. public org, internal, personally identifiable information (PII)
attributes**

## Observability

### Quality metrics

**Requirements and metrics such as accuracy, completeness, integrity, or compliance to Data Governance policies**

### Operational metrics

**Interval of change, freshness, usage statistics, availability, number of users, data versioning, etc.**

### SLOs

**Thresholds for service level objectives to up alerting**

## Consumer

**Who is the consumer of the Data Product?**

## Use Case

**We believe that ...**
**We help achieving ...**
**We know, we are getting there based on ..., ..., ...**

We believe that this data product can be used to derive any kind of data based product.

## Classification

**The nature of the exposed data (source-aligned, aggregate, consumer-aligned)**

This data product is source-aligned since the contained csv files represent the source data.

## Ubiquitous Language

**Context-specific domain terminology (relevant for Data Product), Data Product polysemes which are used to create the
current Data Product**

---
This data product canvas uses the template
of [datamesh-architecture.com](https://www.datamesh-architecture.com/data-product-canvas).
