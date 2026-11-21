#!python

Thread = JavaClass("java.lang.Thread")
ByteClassLoader = JavaClass("de.minescript_javaclass_loader.classloader.ByteClassLoader")
InMemoryCompiler = JavaClass("de.minescript_javaclass_loader.compiler.InMemoryCompiler")

source = """
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
"""

def create_config_class():
	loader = ByteClassLoader(Thread.currentThread().getContextClassLoader())
	bytes_ = InMemoryCompiler.compileToBytes("net.minescript_custom_javaclasses.Config", source)
	return loader.loadFromBytes("net.minescript_custom_javaclasses.Config", bytes_)
