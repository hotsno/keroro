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
  <img width="932" alt="image" src="https://github.com/hotsno/keroro/assets/71658949/61a492b2-1e52-41ef-a81f-437d0f3a82a5">
</p>

## Installation

### Requirements
- Git
- Python (tested using 3.10.9)
- mpv

### Step-by-step instructions
<details>
<summary>Windows</summary>
<br>

If you are on Windows, I **highly** suggest you take a look at the [Taiga](https://taiga.moe/) project first. It most likely does what you want
and more. The reason I created keroro was because I didn't like any of the alternatives for macOS and Linux.

1) Open Terminal (or Command Prompt, Git Bash, or Windows Powershell)  
2) `cd` into the directory where you'll be keeping this project
3) Run `git clone https://github.com/hotsno/keroro`
4) Run `cd keroro`
5) Run `pip install -r requirements.txt`
6) Run `python main.py` and follow the instructions
7) Map some anime, and begin watching!


**NOTE:** The mpv `scripts` folder on Windows can be created in the same directory as `mpv.exe`. After creating the folder, copy `anilist.lua` into it.

</details>

<details>
<summary>Linux/macOS</summary>
<br>

1) Open a terminal
2) `cd` into the directory where you'll be keeping this project
3) Run `git clone https://github.com/hotsno/keroro`
4) Run `cd keroro`
5) Run `pip3 install -r requirements.txt`
6) Run `python3 main.py` and follow the instructions
7) Map some anime, and begin watching!


**NOTE:** The mpv `scripts` folder on Linux/macOS can be created in the `~/.config/mpv` directory. After creating the folder, copy `anilist.lua` into it.

</details>

## Usage
Run `main.py`. The first time you run, it'll walk you through configuring everything.  
  
Anime should be kept in folders that can correctly correspond to an AniList entry (e.g. if separate AL entries exist for each season, each season should have its own folder or sub-folder). Episode detection is done solely by the file's position alphabetically within the folder. Offsets can be added in the case that you are missing some of the early episodes.  

---

In order for a mapped anime to show up in keroro, it must satisfy a few conditions:
1) You must have properly mapped the anime. keroro will prompt you to do this when it detects a new folder within your anime folder.
2) The AniList entry must be of "Watching" status on your AniList.
3) keroro must think that the next episode is available to watch. E.g., if you have only 1 file in a folder, and your episode status on AniList is 11, keroro will think that you only have ep 1 downloaded, and thus it can't play the next episode (episode 12). This can be resolved by having ALL of the episodes for that anime in the folder (in alphabetical order), OR by adding an offset with `m` then `o`. 

## Tips
* Look into creating an alias for running `main.py`. For example, if you use zsh you can [add an alias](https://linuxhint.com/configure-use-aliases-zsh/) in your `~/.zshrc` file.

## Support, suggestions, and bug reports
Please feel free to open a GitHub issue if you need help, have any suggestions, or bugs to report!
