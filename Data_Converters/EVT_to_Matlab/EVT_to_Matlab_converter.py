# -*- coding: utf-8 -*-
# coding: utf-8


"""
EVT_to_Matlab_converter

This Python program converts seismic data from the 'kinemetrics_evt' format to MATLAB .mat files. It utilizes the ObsPy library for data processing and SciPy for file I/O.

Usage:
- Ensure you have Python 3.x, ObsPy, and SciPy installed.
  !pip install obspy
  !pip install scipy
- Replace 'event_name' with the path to your seismic data file.
- Run the script to start the conversion process.

Requirements:
- Python 3.x
- ObsPy library
- SciPy library

License:
This code is provided under the MIT License.

Disclaimer:
This program is provided as-is, without any warranties or guarantees. Use it at your own risk.

Author: ACHEMINE Yasmine
Date: September 09, 2023
"""

from obspy import read
from scipy.io import savemat
import os

# printing the welcome messages
print("*" * len("Bienvenue au convertisseur Evt_Matlab"))
print("Bienvenue au convertisseur Evt_Matlab")
print("*" * len("Bienvenue au convertisseur Evt_Matlab"))

print(
    "\n Avant de commencer, assurez-vous que vos données sont dans le même dossier (ou l'un de ses sous-dossiers) que le programme."
)
# EVT file that will be converted
event_name = input("\nDonnez le nom du fichier à convertir : ")

if not os.path.exists(event_name):
    # Getting the current working directory's path as a start point for the search
    start_directory = os.getcwd()
    event_not_found = False
    # Searching for file in all subdirectories
    for root, _, files in os.walk(start_directory):
        if event_name in files:
            event_name = os.path.join(root, event_name)
        else:
            event_not_found = True

    if event_not_found:
        print(
            f"ATTENTION : '{event_name}' n'existe ni dans '{start_directory}' ni dans ses sous-dossiers."
        )

else:
    # reading the recording
    st = read(event_name, format="kinemetrics_evt").detrend()

    # Change the channel data
    split_file_name = event_name.split(".")
    for tr in st:
        tr.stats.network = "CGS"
        tr.stats.station = tr.stats.kinemetrics_evt.stnid
        tr.stats.location = split_file_name[1]
        tr.stats.channel = tr.stats.kinemetrics_evt.chan_id

        # Converting the data fron Conts to acceleration (cm/s²)
        tr.data = (
            (tr.data / tr.stats.kinemetrics_evt.chan_sensitivity) * tr.stats.calib * 100
        )

    # creating a directory to store the converted recoding
    directory_name = "Converted_event_to_Matlab"
    if not os.path.exists(directory_name):
        os.mkdir(directory_name)
    path_to_directory = os.path.abspath(directory_name)

    # converting and saving the recording
    for i, tr in enumerate(st):
        mdict = {k: str(v) for k, v in tr.stats.items()}
        mdict["data"] = tr.data
        output_file_name = f"{split_file_name[0][-14:-1]}.{split_file_name[1]}.{split_file_name[3]}_{tr.stats.channel}.mat"
        output_file_path = os.path.join(path_to_directory, output_file_name)
        savemat(output_file_path, mdict)

    print("\t**** Operation terminée avec succès ****")
