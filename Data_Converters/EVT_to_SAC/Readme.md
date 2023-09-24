## EVT_to_SAC_Converter

This Python program is designed to convert seismic data from the 'kinemetrics_evt' format to SAC (Seismic Analysis Code) files. It utilizes the ObsPy library to read seismic data, extract metadata, and transform trace data into SAC format. The conversion process allows for further analysis and visualization of seismic data using SAC-compatible tools.

## Getting Started

To use this program, follow the steps below:

1. Ensure you have Python 3.x, ObsPy, and SciPy installed on your system.
   ```bash
   pip install obspy
2. Replace event_name with the path to your seismic data file. Make sure that your data file is in the 'kinemetrics_evt' format.

3. Run the script to start the conversion process.

## Usage

- The program will prompt you to provide the name of the file you want to convert. Please ensure that your data file is in the same directory as the script or in one of its subdirectories.

- If the specified file is not found in the current directory or its subdirectories, the program will perform a recursive search to locate the file.

- The converted data will be saved in a directory named 'Converted_event_to_SAC' within the same directory as the script, in SAC format.

## Requirements

- Python 3.x
- ObsPy library

## Author

[ACHEMINE Yasmine]

## License

This code is provided under the MIT License. You are free to use, modify, and distribute it, provided that you include the original copyright notice in all copies or substantial portions of the software.

Note: If you use or modify this code in your project, it's considered good practice to provide attribution to the original author.

## Disclaimer

This program is provided as-is, without any warranties or guarantees. Use it at your own risk.

############################################################################

## Convertisseur Evt_SAC

Ce programme Python est conçu pour convertir des données sismiques du format 'kinemetrics_evt' en fichiers SAC (Seismic Analysis Code). Il utilise la bibliothèque ObsPy pour lire les données sismiques, extraire les métadonnées et transformer les données de trace en format SAC. Le processus de conversion permet une analyse et une visualisation ultérieures des données sismiques à l'aide d'outils compatibles avec SAC.

## Pour commencer

Pour utiliser ce programme, suivez les étapes ci-dessous :

- Assurez-vous d'avoir Python 3.x et ObsPy installés sur votre système.

	bash
		pip install obspy
- Remplacez event_name par le chemin de votre fichier de données sismiques. Assurez-vous que votre fichier de données est au format 'kinemetrics_evt'.

- Exécutez le script pour démarrer le processus de conversion.

## Utilisation

- Le programme vous demandera de fournir le nom du fichier que vous souhaitez convertir. Assurez-vous que votre fichier de données se trouve dans le même répertoire que le script ou dans l'un de ses sous-répertoires.

- Si le fichier spécifié n'est pas trouvé dans le répertoire actuel ou ses sous-répertoires, le programme effectuera une recherche récursive pour le localiser.

- Les données converties seront enregistrées dans un répertoire nommé 'Converted_event_to_SAC' dans le même répertoire que le script, au format SAC.

## Prérequis

- Python 3.x
- Bibliothèque ObsPy

## Auteur

[ACHEMINE Yasmine]

## Licence

Ce code est fourni sous licence MIT. Vous êtes libre de l'utiliser, de le modifier et de le distribuer, à condition d'inclure l'avis de droit d'auteur d'origine dans toutes les copies ou portions substantielles du logiciel.

Remarque : Si vous utilisez ou modifiez ce code dans votre projet, il est recommandé de mentionner l'auteur original.

## Avertissement

Ce programme est fourni tel quel, sans aucune garantie ni garantie. Utilisez-le à vos propres risques.

