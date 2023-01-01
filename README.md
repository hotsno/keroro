<p align="center">
  <img src="https://user-images.githubusercontent.com/71658949/210159393-f8ead149-5076-4b76-b95b-11df38e871fd.png" width="300px"/>
</p>

## What is Keroro?
Keroro is a CLI tool + [mpv](https://github.com/mpv-player/mpv) script that uses AniList as a way to keep track of the watch progress of your locally downloaded anime. It allows you to watch the next episode of an anime in mpv as well as mark an episode as complete when >80% of the episode has been watched.

## Features
- Map a folder to an AniList entry
- Watch the next episode of an anime based on your progress on AniList
- Automatically marks episode as watched on AniList when you reach >80% watch completion
- Store progress locally when using without an internet connection
- Add an offset if you are missing some episodes
- Discord Rich Presence [(with posters!)](https://media.discordapp.net/attachments/826685810472124429/1058942983250120714/image.png)

<p align="center">
  <img width="932" alt="image" src="https://user-images.githubusercontent.com/71658949/210159831-17a98a13-2ef8-4483-bf38-f992654570c5.png">
</p>

## Installation

### Requirements
- Git
- Python (tested using 3.10.9)

### Step-by-step instructions
<details>
<summary>Windows</summary>
<br>

1) Open Command Prompt or Git Bash  
2) `cd` into the directory where you'll be keeping this project
3) Run `git clone https://github.com/hotsno/mpv-anilist`
4) Run `cd keroro`
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
4) Run `cd keroro`
5) Run `pip3 install -r requirements.txt`
6) Run `python3 main.py` and follow the instructions
7) Map some anime, and begin watching!


**NOTE:** The `mpv scripts` folder on Linux/macOS can be created in the `~/.config/mpv` directory. After creating the folder, copy `anilist.lua` into it.

</details>

## Usage
Run `main.py`. The first time you run, it'll walk you through configuring everything.  
  
Anime should be kept in folders that can correctly correspond to an AniList entry (e.g. if separate AL entries exist for each season, each season should have its own folder or sub-folder). Episode detection is done solely by the file's position alphabetically within the folder. Offsets can be added in the case that you are missing some of the early episodes.

## Tips
* Look into creating an alias for running `main.py`. For example, if you use zsh you can [add an alias](https://linuxhint.com/configure-use-aliases-zsh/) in your `~/.zshrc` file.

## Support, suggestions, and bug reports
Please feel free to open a GitHub issue if you need help, have any suggestions, or bugs to report!
