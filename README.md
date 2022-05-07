# vct-scores

This is a script that creates and continuously updates a text file that can be used as a source on OBS to display the current VCT game and match scores.

### Installation & Running

1. Install both `requirements.txt` and `vct_scores.py`
2. Navegate to where the files were downloaded and right click off to the right side somewhere and click "Open In Terminal"
3. Download dependencies via Terminal: `py -m pip install -r requirements.txt`
4. Run `vct_scores.py` via Terminal: `.\vct_scores.py` (Do not close Terminal until program is no longer of use.)

### Adding to OBS

1. Add a new `Text (GDI+)` source
2. Check the "Read from file" box
3. Browse to where `requirements.txt` and `vct_scores.py` were installed.
4. Select `scores.txt`
