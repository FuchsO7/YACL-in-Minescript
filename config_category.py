#!python

Minecraft = JavaClass("net.minecraft.client.Minecraft")
CLIENT = Minecraft.getInstance()
Component = JavaClass("net.minecraft.network.chat.Component")
YaclConfigCategory = JavaClass("dev.isxander.yacl3.api.ConfigCategory")
OptionGroup = JavaClass("dev.isxander.yacl3.api.OptionGroup")
Option = JavaClass("dev.isxander.yacl3.api.Option")
ButtonOption = JavaClass("dev.isxander.yacl3.api.ButtonOption")
BooleanControllerBuilder = JavaClass("dev.isxander.yacl3.api.controller.BooleanControllerBuilder")
IntegerFieldControllerBuilder = JavaClass("dev.isxander.yacl3.api.controller.IntegerFieldControllerBuilder")
LongFieldControllerBuilder = JavaClass("dev.isxander.yacl3.api.controller.LongFieldControllerBuilder")
FloatFieldControllerBuilder = JavaClass("dev.isxander.yacl3.api.controller.FloatFieldControllerBuilder")
DoubleFieldControllerBuilder = JavaClass("dev.isxander.yacl3.api.controller.DoubleFieldControllerBuilder")
StringControllerBuilder = JavaClass("dev.isxander.yacl3.api.controller.StringControllerBuilder")


class ConfigField:

	def __init__(self, defaults_object, config_object, field):
		self.name = field.getName()
		self.datatype = field.getType().getName()
		self.defaults_object = defaults_object
		self.config_object = config_object
		self.field = field

	def _get_accessible_field(self, object_, name):
		field = object_.getClass().getDeclaredField(name)
		field.setAccessible(True)
		return field

	def _get_field_value(self, object_, name):
		field = self._get_accessible_field(object_, name)
		return field.get(object_)

	def _set_field_value(self, object_, name, new_value):
		field = self._get_accessible_field(object_, name)
		field.set(object_, new_value)

	def default(self):
		return self._get_field_value(self.defaults_object, self.field.getName())

	def getter(self):
		return self._get_field_value(self.config_object, self.field.getName())

	def setter(self, new_value):
		self._set_field_value(self.config_object, self.field.getName(), new_value)
	

class ConfigCategory:

	def __init__(self, name):
		self.name = name
		return

	def _create_options(self, defaults, config):
		options = []
		for field in config.getClass().getDeclaredFields():
			if field.getType().getSimpleName() == "ConfigClassHandler":
				continue
			options.append(ConfigField(defaults, config, field))
		return options

	def _create_button_option(self, name, text, action): # lambda screen, button_option: print("Button tapped!")
		return ButtonOption.createBuilder().name(Component.literal(name)).text(Component.literal(text)).action(action).build()

	def _get_controller_type(self, controller_type):
		if controller_type =="boolean":
			return lambda opt: BooleanControllerBuilder.create(opt).coloured(True)
		elif controller_type == "int":
			return lambda opt: IntegerFieldControllerBuilder.create(opt)
		elif controller_type == "long":
			return lambda opt: LongFieldControllerBuilder.create(opt)
		elif controller_type == "float":
			return lambda opt: FloatFieldControllerBuilder.create(opt).formatValue(lambda value: Component.literal(f"{value:.1f}"))
		elif controller_type == "double":
			return lambda opt: DoubleFieldControllerBuilder.create(opt).formatValue(lambda value: Component.literal(f"{value:.2f}"))
		elif controller_type == "java.lang.String":
			return lambda opt: StringControllerBuilder.create(opt)
		else:
			raise Exception(f"Unknown Controller Type {controller_type}")

	def _create_controller_option(self, option):
		return Option.createBuilder().name(Component.literal(option.name)).controller(self._get_controller_type(option.datatype)).binding(option.default(), option.getter, option.setter).build()

	def _create_group(self, defaults, config):
		builder = OptionGroup.createBuilder().name(Component.literal("Configuration"))
		for option in self._create_options(defaults, config):
			builder.option(self._create_controller_option(option))
		return builder.build()

	def create_category(self, defaults, config):
		return YaclConfigCategory.createBuilder().name(Component.literal(self.name)).group(self._create_group(defaults, config)).build()
