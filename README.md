# mpv-anilist
- Python script to "map" locally downloaded anime to an AniList ID
- Python script to continue watching a mapped anime with mpv
- mpv script to automatically mark episodes as watched on AniList when a file reaches 80% completion
- Other helper scripts (check usage section for more details)

## Installation
### Video (commands differ by OS)
https://user-images.githubusercontent.com/71658949/163731187-be5c182a-4b0e-46e9-9f6f-a3599e9c1f1a.mp4

1) `git clone https://github.com/hotsno/mpv-anilist` to copy all the files from this repo.
2) Run `cd mpv-anilist`.
3) Run `pip3 install -r requirements.txt`.
4) Run `python3 setup.py` and follow the instructions.
5) Move the `anilist.lua` file inside the `scripts` folder to your [mpv scripts](https://mpv.io/manual/master/#script-location) folder.
6) Edit the `"command"` variable in `anilist.lua` to match your setup's proper Python and `update.py` paths.
7) You should be done!

## Usage
### Adding an anime (`add_anime.py`)
Run `python3 add_anime.py` (may differ depending on OS).
### Watch a mapped anime (`continue.py`)
Run `python3 continue.py` (may differ depending on OS).
### AniList updater mpv script
As long as you've properly run `add_anime.py` on the anime you're watching, this should work automatically once an episode reaches 80% played!
### (Extra) Map unmapped folders (`mapper.py`)
If you have anime in your anime folder which follows proper naming scheme, and isn't yet mapped to an AniList ID, you can map it. Run `python3 mapper.py` (may differ depending on OS).

## Naming scheme
The scripts currently rely on a strict file naming scheme in order to be properly picked up. They must be named in the following format: `Episode 01.mkv`, where the episode number must always equal to the digit count of the highest episode.  
Ex. If there are 12 episodes, each episode count must have 2 digits, so episodes 1-9 must be padded with one 0 `(Episode 01.mkv - Episode 09.mkv)`.

## Tips
* If you use this regularly, I recommend adding an alias to `add_anime.py` and `continue.py` in your terminal so that you can quickly run these without typing the whole command out
  - For example if you use `zsh` as your shell, you can add `alias add="python3 ~/mpv-anilist/add_anime.py"` and `alias a="python3 ~/mpv-anilist/continue.py"` to your `.zshrc` config file, modifying the commands accordingly. This example added aliases `add` and `a`.

## Limitations
- File names need to follow a strict naming scheme
- Current code is only tested to work with macOS, might work on Linux. Currently doesn't for Windows.

## Planned improvements
- Make it work on Windows
- Make installation more user friendly
- ~~Remove the need for proprietary naming scheme by using [Anitomy](https://github.com/erengy/anitomy)~~ Not planned unless I gain the time/motivation
