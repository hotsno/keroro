# mpv-anilist
- Map locally downloaded anime to an AniList ID
- Continue watching (based off AniList episode status) with mpv
- `anilist.lua` mpv script automatically marks episode as watched on AniList when it reaches 80% watch completion

<img width="932" alt="image" src="https://user-images.githubusercontent.com/71658949/192674357-e9939bab-ae03-4411-b7f5-b58e040f14e9.png">


## Installation

### Requirements
- Git
- Python 3.x

### Step-by-step instructions
<details>
<summary>Windows</summary>
<br>

1) Open Command Prompt or Git Bash  
2) `cd` into the directory where you'll be keeping this project
3) Run `git clone https://github.com/hotsno/mpv-anilist`
4) Run `cd mpv-anilist`
5) Run `pip install -r requirements.txt`
6) Run `python main.py` and follow the instructions
7) Map some anime, and begin watching!


**NOTE:** The `mpv scripts` folder on Windows can be created in the same directory as `mpv.exe`. After creating the folder, copy `anilist.lua` into it.

</details>

<details>
<summary>Linux/macOS</summary>
<br>

1) Open a terminal
2) `cd` into the directory where you'll be keeping this project
3) Run `git clone https://github.com/hotsno/mpv-anilist`
4) Run `cd mpv-anilist`
5) Run `pip3 install -r requirements.txt`
6) Run `python3 main.py` and follow the instructions
7) Map some anime, and begin watching!


**NOTE:** The `mpv scripts` folder on Linux/macOS can be created in the `~/.config/mpv` directory. After creating the folder, copy `anilist.lua` into it.

</details>

## Usage
Run `main.py` and things *should* be self-explanatory. The first time you run, it'll walk you through configuring everything.  
  
Anime should be kept in folders that can correctly correspond to an AniList entry (e.g. if separate AL entries exist for each season, each season should have its own folder). Episode detection is done solely by the file's position alphabetically within the folder. Offsets can be added in the case that you are missing some of the early episodes.

## Tips
* Look into creating an alias for running `main.py`. For example, if you use zsh you can [add an alias](https://linuxhint.com/configure-use-aliases-zsh/) in your `~/.zshrc` file.

## Help, suggestions, and bug reports
Please feel free to open a GitHub issue if you have any suggestions, bugs to report, or need help!

## Planned improvements
- [ ] Remove the need for proprietary naming scheme by using [Anitomy](https://github.com/erengy/anitomy)
- [ ] Improve aesthetics/UI
- [ ] Make it work on Windows
- [x] Make installation more user friendly
