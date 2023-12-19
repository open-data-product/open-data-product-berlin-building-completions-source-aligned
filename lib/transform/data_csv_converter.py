import os

import pandas as pd

from lib.tracking_decorator import TrackingDecorator


@TrackingDecorator.track_time
def convert_data_to_csv(source_path, results_path, clean=False, quiet=False):
    # Iterate over files
    for subdir, dirs, files in sorted(os.walk(source_path)):

        # Make results path
        subdir = subdir.replace(f"{source_path}/", "")
        os.makedirs(os.path.join(results_path, subdir), exist_ok=True)

        for file_name in [file_name for file_name in sorted(files) if not file_name.startswith(f"~")]:
            source_file_path = os.path.join(source_path, subdir, file_name)
            convert_file_to_csv(source_file_path, clean=clean, quiet=quiet)


def convert_file_to_csv(source_file_path, clean=False, quiet=False):
    source_file_name, source_file_extension = os.path.splitext(source_file_path)
    file_path_csv = f"{source_file_name}.csv"

    # Check if result needs to be generated
    if clean or not os.path.exists(file_path_csv):
        # Determine engine
        if source_file_extension == ".xlsx":
            engine = "openpyxl"
        elif source_file_extension == ".xls":
            engine = None
        else:
            return

        year = os.path.basename(source_file_name).split(sep="-")[-2]

        try:
            dataframes = []

            # Iterate over sheets
            sheet = "Baufert. Tab. 1 u. 2"
            skiprows = 10
            names = ["year", "building_completion_total", "building_completion_residential_buildings",
                     "building_completion_non_residential_buildings",
                     "building_measure_on_existing_buildings", "usage_area", "living_area", "apartments",
                     "apartment_rooms", "total_costs"]
            drop_columns = []

            dataframe = pd.read_excel(source_file_path, engine=engine, sheet_name=sheet, skiprows=skiprows,
                                      usecols=list(range(0, len(names))), names=names) \
                .drop(columns=drop_columns, errors="ignore") \
                .dropna()
            dataframe = dataframe.loc[dataframe["year"] == int(year)].head(1)
            dataframes.append(dataframe)

            sheet = "Baufert. Tab. 1 u. 2"
            skiprows = 33
            names = ["year", "building_completions_new", "building_completions_new_with_1_apartment",
                     "building_completions_new_with_2_apartments",
                     "building_completions_new_with_3_or_more_apartment",
                     "building_completions_new_total_apartments", "building_completions_new_volume",
                     "building_completions_new_living_area", "building_completions_new_costs"]
            drop_columns = []
            dataframe = pd.read_excel(source_file_path, engine=engine, sheet_name=sheet, skiprows=skiprows,
                                      usecols=list(range(0, len(names))), names=names) \
                .drop(columns=drop_columns, errors="ignore") \
                .dropna()
            dataframe = dataframe.loc[dataframe["year"] == int(year)].head(1)
            dataframes.append(dataframe)

            # Join dataframes
            dataframe = pd.concat(dataframes, axis=1).drop(columns=["year"], errors="ignore")

            # Write csv file
            if dataframe.shape[0] > 0:
                dataframe.to_csv(file_path_csv, index=False)
            if not quiet:
                print(f"✓ Convert {os.path.basename(file_path_csv)}")
            else:
                if not quiet:
                    print(dataframe.head())
                    print(f"✗️ Empty {os.path.basename(file_path_csv)}")
        except Exception as e:
            print(f"✗️ Exception: {str(e)}")
    elif not quiet:
        print(f"✓ Already exists {os.path.basename(file_path_csv)}")
