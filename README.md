# veo-metadata

This repo contains the code to format and generate the label files for the veo application. 
* No venv or requirements.txt file is provided as vanilla python3 should do all the work.
* Raw label files are found in the /raw directory while output files get dropped in /out.
* Run 'cd src && python3 generate_metadata.py' to fire off the script

This repo also contains code to generate the output files packaged for download by each view
* run 'cd src && python3 generate_downloads.py' to fire off the script
