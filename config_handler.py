from java import eval_pyjinn_script, JavaClass

Minecraft = JavaClass("net.minecraft.client.Minecraft")
CLIENT = Minecraft.getInstance()

pyj = eval_pyjinn_script("""
from config_manager import ConfigManager
from config_class import create_config_class_with_addon_mod, create_config_class_with_pyjinn_plus

name = "net.minescript_custom_javaclasses.Config"

source = \"\"\"
package net.minescript_custom_javaclasses;

import dev.isxander.yacl3.config.v2.api.SerialEntry;

public class Config {
    @SerialEntry
    public boolean a = true;
	@SerialEntry
    public int b = 1;
	@SerialEntry
    public long c = -1L;
	@SerialEntry
    public float d = 3.14f;
	@SerialEntry
    public double e = 2.71;
	@SerialEntry
    public String f = "Hello World!";
}
\"\"\"

def main():
	config = create_config_class_with_pyjinn_plus(name, source)
	config_manager = ConfigManager(config, "yacltest.json", "Title", "Category")
	config_manager.open_config()
""")

main = pyj.get("main")

main()

while CLIENT.gui.screen() != None:
	pass
