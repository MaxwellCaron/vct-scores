# vct-scores

This is a script that creates and continuously updates a text file that can be used as a source on OBS to display the current VCT game and match scores.

<br>

Any questions or comments you can DM me on discord: `Meeks#5150`

<br>

### Installation & Running

1. Install both `requirements.txt` and `vct_scores.py` by going over to the right side of the page and going to the `download` release.
2. Navegate to where the files were downloaded and right click off to the right side somewhere and click "Open In Terminal"
3. Download dependencies via Terminal: `py -m pip install -r requirements.txt`
4. Run `vct_scores.py` via Terminal: `py .\vct_scores.py` (Do not close Terminal until program is no longer of use.)

### Adding to OBS

1. Add a new `Text (GDI+)` source
2. Check the "Read from file" box
3. Browse to where `requirements.txt` and `vct_scores.py` were installed.
4. Select `scores.txt`

### Format Example

![image](https://user-images.githubusercontent.com/69171981/167242192-6fceb0f6-0268-45f8-adce-1c954e5ef427.png)

<br><br>

### Video Walkthough

https://user-images.githubusercontent.com/69171981/167242165-62f8c749-053a-42d1-b451-2fd779ddedb9.mp4


