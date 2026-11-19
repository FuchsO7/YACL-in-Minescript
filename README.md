
# YACL in Minescript
Create a YACL Config Screen with Minescript. Proof of concept for using other minecraft mods in Minescript scripts.

### Usage
Clone the python files into your `minescript` folder. To run it, enter `\config_handler` ingame. This will start the script and generate a config screen.

The config is generated based on the fields of the `config_class` with reflections. In this example, the `YACLConfig` class is used. To change the available configuration, pass a different `config_class` with the desired fields to the `ConfigManager`.

### Dependencies
- Minescript Mod
- YetAnotherConfigLib Mod

### License
This project is available under the MIT-0 License.
