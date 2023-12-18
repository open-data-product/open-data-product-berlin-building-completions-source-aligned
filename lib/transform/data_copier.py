import os
import shutil

from lib.tracking_decorator import TrackingDecorator


@TrackingDecorator.track_time
def copy_data(source_path, results_path, clean=False, quiet=False):
    # Iterate over files
    for subdir, dirs, files in sorted(os.walk(source_path)):

        # Make results path
        subdir = subdir.replace(f"{source_path}/", "")
        os.makedirs(os.path.join(results_path, subdir), exist_ok=True)

        for source_file_name in sorted(files):
            results_file_name = get_results_file_name(source_file_name)

            source_file_path = os.path.join(source_path, subdir, source_file_name)
            results_file_path = os.path.join(results_path, subdir, results_file_name)

            # Check if file needs to be copied
            if clean or not os.path.exists(results_file_path):
                shutil.copyfile(source_file_path, results_file_path)

                if not quiet:
                    print(f"✓ Copy {results_file_name}")
            else:
                print(f"✓ Already exists {results_file_name}")


def get_results_file_name(source_file_name):
    if source_file_name == "SB_F02-02-00_2020j01_BE.xlsx":
        return "berlin-building-completion-2020-00.xlsx"
    elif source_file_name == "SB_F02-02-00_2021j01_BE.xlsx":
        return "berlin-building-completion-2021-00.xlsx"
    elif source_file_name == "SB_F02-02-00_2022j01_BE.xlsx":
        return "berlin-building-completion-2022-00.xlsx"
    else:
        return source_file_name
