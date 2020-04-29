# veo-metadata

This repo contains the code to format and generate the label files for the veo application. 
* No venv or requirements.txt file is provided as vanilla python3 should do all the work.
* Raw label files are found in the /raw directory while output files get dropped in /out.
* Run 'cd src && python3 generate_metadata.py' to fire off the script

This repo also contains code to generate the output files packaged for download by each view
* run 'cd src && python3 generate_downloads.py' to fire off the script

... and now the repo contains a script to fill in the required schema, even if empty for raw data files
* run 'cd src && python3 generate_appdata.py" to fire off the script

TODO: 
* set the generate_downloads and generate_metadata to drop into /out subdirectories
* run progs from root dir and refactor relative paths
