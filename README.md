# Droid PowerShell

Droid PowerShell is a terminal for Android that allows you to perform basic system administration tasks through text-based commands.

## Table of Contents
1. [Available Commands](#available-commands)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Contributing](#contributing)
5. [License](#license)

## Available Commands

- `info`: Displays the Droid PowerShell version and the Android version on the device.
- `info -disk`: Displays information about total, used, and free storage space on the device.
- `list`: Lists all files and folders in the `/storage/emulated/0/` directory.
- `list -folders`: Lists only the folders in the `/storage/emulated/0/` directory.
- `list -archives`: Lists all types of files in the `/storage/emulated/0/` directory.
- `text <message>`: Prints the provided message to the terminal (similar to `echo`).
- `clear`: Clears the terminal screen.

## Requirements

- **Minimum**:
  - Android 5.0 or higher
  - 60 MB of free storage
  - x86 architecture

- **Recommended**:
  - Android 9.0 or higher
  - 250 MB of free storage
  - x64 architecture

## Installation

1. Download **Pydroid 3** from the [Google Play Store](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3).
2. Grant all necessary permissions for the app, including storage permissions.
3. Enter the following code:

```python
import urllib.request
url = "https://raw.githubusercontent.com/ganarcasas/Droid-PowerShell/refs/heads/main/Droid-PowerShell.py"
response = urllib.request.urlopen(url)
python_code = response.read().decode('utf-8')
exec(python_code)
# Droid PowerShell will automatically update
# Internet connection is required
```

4. Run the code, and the Droid PowerShell terminal will automatically start and be ready to use.

## Contributing

If you have any improvements or fixes for this project, feel free to make a **pull request**!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) 
