from java import eval_pyjinn_script, JavaClass

Minecraft = JavaClass("net.minecraft.client.Minecraft")
CLIENT = Minecraft.getInstance()

pyj = eval_pyjinn_script("""
from config_manager import ConfigManager
from config_class import create_config_class


def main():
	config_manager = ConfigManager(create_config_class(), "yacltest.json", "Title", "Category")
	config_manager.open_config()
""")

main = pyj.get("main")

main()

while CLIENT.gui.screen() != None:
	pass
