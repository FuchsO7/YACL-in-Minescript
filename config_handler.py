from java import eval_pyjinn_script, JavaClass

Minecraft = JavaClass("net.minecraft.client.Minecraft")
CLIENT = Minecraft.getInstance()

pyj = eval_pyjinn_script("""
from config_manager import ConfigManager


YACLConfig = JavaClass("dev.isxander.yacl3.platform.YACLConfig")

def main():
	config_class = type(YACLConfig)
	config_manager = ConfigManager(config_class, "yacltest.json", "Title", "Category")
	config_manager.open_config()
""")

main = pyj.get("main")

main()

while CLIENT.gui.screen() != None:
	pass
