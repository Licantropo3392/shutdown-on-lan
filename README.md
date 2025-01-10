# Shutdown On Lan

Shutdown On Lan is a FastAPI application that allows you to remotely shut down the system.

## Why?

- It's easy to integrate into existing projects like [UpSnap](https://github.com/seriousm4x/UpSnap) (It was created for it!)
- It simplifies the process of remotely shutting down the PC without requiring complex configurations.

### Example Use Case

I use this tool combined with [UpSnap](https://github.com/seriousm4x/UpSnap) for booting my gaming PC, [Tailscale](https://tailscale.com/) as VPN for the remote connection, and [Sunshine](https://github.com/LizardByte/Sunshine) for streaming so I can connect and play my games even when I'm not at home.

## Usage

1. Download the package:
    ```sh
    pip install shutdown-on-lan
    ```
2. Start the application:
    ```sh
    shutdown-on-lan
    ```
3. Send an HTTP request to shut down the computer. For example, using `curl`:

    Replace `<IP_ADDRESS>` with the IP address of the machine you want to shut down and `<PORT>` with the port number (default is 8000).
    ```sh
    curl "http://<IP_ADDRESS>:<PORT>/shutdown"
    ```

## Adding the Command to Startup on Windows

To run `shutdown-on-lan` automatically at startup on Windows without opening a terminal, follow these steps:

1. Create a batch file:
    - Open a text editor and paste the following content:
      ```batch
      @echo off
      start "" /B pythonw -m shutdown_on_lan.main
      ```
    - Save the file as `shutdown-on-lan.bat`.

2. Create a shortcut:
    - Right-click on your desktop or in a folder and select `New > Shortcut`.
    - In the location field, enter the path to the `shutdown-on-lan.bat` file.
    - Click `Next` and give the shortcut the name `shutdown-on-lan`.

3. Move the shortcut to the Startup folder:
    - Press `Win + R`, type `shell:startup`, and press `Enter`.
    - Move the shortcut you created into the Startup folder.

This will run `shutdown-on-lan` in the background without opening a terminal and add an icon to the system tray. You can quit the application by right-clicking the tray icon and selecting "Quit".

## Arguments

### Port

You can specify a custom port for the application to run on by using the `--port` argument. The default port is `8000`.

Example:
```sh
shutdown-on-lan --port 8080
```

### Message

You can specify a custom shutdown message to be displayed before the system shuts down by using the `--message` argument. The default message is `System will shut down in 5 minutes`

Example:
```sh
shutdown-on-lan --message "System will shut down in 5 minutes"
```

### Hide Message

You can hide the shutdown message by using the `--hide-message` argument. By default, the message is shown.

Example:
```sh
shutdown-on-lan --hide-message
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.