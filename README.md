# veo-metadata

This repo contains the code to format and generate the label files for the veo application. No venv or requirements.txt file is provided as vanilla python3 should do all the work. Raw label files are found in the /raw directory while output files get dropped in /out.
#### Process all files (metadata, downloads, schema)
```bash
cd src && python3 generate_all.py
```

#### Only metadata
```bash
cd src && python3 generate_metadata.py
```

#### Only downloadable
```bash
cd src && python3 generate_downloads.py
```

#### Only schema formatted files:
```bash
cd src && python3 generate_appdata.py
```

TODO: 
* build any necessary state data
* set the generate_downloads and generate_metadata to drop into /out subdirectories
* run progs from root dir and refactor relative paths
