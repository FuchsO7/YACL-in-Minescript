#!python
from config_category import ConfigCategory

FabricLoader = JavaClass("net.fabricmc.loader.api.FabricLoader")
FieldNamingPolicy = JavaClass("com.google.gson.FieldNamingPolicy")
Minecraft = JavaClass("net.minecraft.client.Minecraft")
CLIENT = Minecraft.getInstance()
Component = JavaClass("net.minecraft.network.chat.Component")
YetAnotherConfigLib = JavaClass("dev.isxander.yacl3.api.YetAnotherConfigLib")
ConfigClassHandler = JavaClass("dev.isxander.yacl3.config.v2.api.ConfigClassHandler")
GsonConfigSerializerBuilder = JavaClass("dev.isxander.yacl3.config.v2.api.serializer.GsonConfigSerializerBuilder")


class ConfigManager:
	
	def __init__(self, config_class, file_name, title, category_name):
		self.PATH = FabricLoader.getInstance().getConfigDir().resolve(file_name)
		self.HANDLER = self._create_handler(config_class)
		self._load_config()
		self.title = title
		self.category = ConfigCategory(category_name)

	def _create_handler(self, config_class):
			return ConfigClassHandler.createBuilder(config_class).serializer(self._serialize_config).build()
	
	def _serialize_config(self, config):
		return GsonConfigSerializerBuilder.create(config).setPath(self.PATH).setJson5(True).appendGsonBuilder(self._configurate_gson_builder).build()
	
	def _configurate_gson_builder(self, builder):
		return builder.setFieldNamingPolicy(FieldNamingPolicy.IDENTITY)

	def _load_config(self):
		self.HANDLER.load()

	def _save_config(self):
		self.HANDLER.save()

	def _build_gui(self, defaults, config, builder):
		builder.category(self.category.create_category(defaults, config))
		return builder.title(Component.literal(self.title)).save(self._save_config)

	def create_gui(self, parent):
		return YetAnotherConfigLib.create(self.HANDLER, self._build_gui).generateScreen(parent)

	def open_config(self):
		CLIENT.gui.setScreen(self.create_gui(CLIENT.gui.screen()))
