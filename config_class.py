IS_PYJINN_PLUS_PRESENT = True
try:
	import pyjinn_plus
except:
	IS_PYJINN_PLUS_PRESENT = False

def create_config_class_with_pyjinn_plus(name, source):	
	if not IS_PYJINN_PLUS_PRESENT:
		raise Exception("Pyjinn Plus was not found")
	class_ = pyjinn_plus.ClassBuilder.new_class(name, source)
	return type(class_)

def create_config_class_with_addon_mod(name, source):
	InMemoryCompiler = JavaClass("de.minescript_javaclass_loader.compiler.InMemoryCompiler")
	compiler = InMemoryCompiler()
	return compiler.compileAndLoadClass(name, source)
