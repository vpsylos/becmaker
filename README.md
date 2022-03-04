# becmaker
A tool to create break even charts for the IB Business Management course. The tool is written in Python and uses Matplotlib, PySimpleGUI.

Update: The program can now also display the margin of safety.

## How to run becmaker
### In Linux:

1. Install dependencies:

`pip install PySimpleGUIQt`

`pip install matplotlib`

2. Clone the repository: `git clone https://github.com/vpsylos125/becmaker.git`
3. Change directory: `cd becmaker`
4. Allow the program to be executed: `chmod +x becmaker.py`
5. Execute the program: `./becmaker.py`

#### If using Arch Linux (or Arch-based distro)

1. Clone the repository: `git clone https://github.com/vpsylos125/becmaker.git`
2. Change directory: `cd becmaker`
3. Build the package: `makepkg -sirc`

### In Windows:

1. Download the `becmaker.exe` file under Releases
2. Enjoy!

## How to use becmaker

becmaker can be used to create break-even charts for the IB Business Management course. When launching the program, the user needs to insert the following information:
1. Business name (Used to create chart's title)
2. Fiscal period (Used to create chart's title)
3. Current level of output
4. Total fixed costs
5. Average variable costs
6. Price

Afterwards, the user must click the `Create break-even chart` button. The user can also save the chart in a `.png` file, by clicking on the save icon in the chart window.

## Additional features that may be added (any contribution welcome)

- Capability to create profit and loss accounts

- Creation of AppImage for the program, AU

- dmg for Macs

- Website version
