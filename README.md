# Shutdown On Lan

Shutdown On Lan is a FastAPI application that allows you to remotely shut down the system.

## Why?
It's easy to integrate into existing projects like [UpSnap](https://github.com/seriousm4x/UpSnap) (It was created for it!)

## Usage
1. Download the package:
    ```sh
    pip install shutdown-on-lan
    ```
2. Start the application:
    ```sh
    fastapi run main.py
    ```
3. Send an HTTP request to shut down the computer. For example, using `curl`:
    ```sh
    curl "http://{IP of the machine}:8000/shutdown"
    ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.