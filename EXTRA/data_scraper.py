import os
import urllib.request
import gzip
from io import BytesIO

# General Link used to gather my data
URL = "https://opendata.dwd.de/climate_environment/CDC/grids_germany/annual/"

# Used in combination of URL, creates the link that contains all of the data
# # example:: 
# ## URL + air == https://opendata.dwd.de/climate_environment/CDC/grids_germany/annual/ + air_temperature_mean/
url_dict = {"air" : URL + 'air_temperature_mean/', 
            "frost": URL + "frost_days/"}

# Used to specify location of folder
dir_dict = {"air" : "air_temperature", 
            "frost" : "frost_days"}

##### WRITE THE KEY HERE
KEY = ""

def download_and_extract(key: str) -> __file__:
    """
        Retrieves document from given link, then unzips and saves it
        in the desired folder location

    Args:
        key (str): Key from url/dir dictionary
    """

    url = url_dict[key]
    dirc = dir_dict[key]
    
    for i in range(1961, 2022 + 1):
        try:

            name_dict = {"air" : f"grids_germany_annual_air_temp_mean_{i}17.asc.gz",
                        "frost": f"grids_germany_annual_frost_days_{i}_17.asc.gz",
                        "":"",
                        "":"",
                        "":""}

            name = name_dict[key]

            filename = name

            print(filename)

            urllib.request.urlretrieve(url + filename, filename)
            
            my_dir = os.path.join("./raw_data/" + dirc, filename)

            # Extracts the file
            with gzip.open(filename, 'rb') as f_in:
                with open(my_dir[:-3], 'wb') as f_out:
                    f_out.write(f_in.read())

            # Removes the compressed file
            os.remove(filename)

        except:
            print(i, "--> Is invalid")
            continue


def main(key: str):
    download_and_extract(key)

if __name__ == "__main__":
    main(KEY)