#!python

Thread = JavaClass("java.lang.Thread")
ByteClassLoader = JavaClass("de.minescript_javaclass_loader.classloader.ByteClassLoader")
InMemoryCompiler = JavaClass("de.minescript_javaclass_loader.compiler.InMemoryCompiler")

source = """
package net.minescript_custom_javaclasses;

public class Config {
    public boolean a = true;
    public int b = 1;
    public long c = -1L;
    public float d = 3.14f;
    public double e = 2.71;
    public String f = "Hello World!";
}
"""

def create_config_class():
	loader = ByteClassLoader(Thread.currentThread().getContextClassLoader())
	bytes_ = InMemoryCompiler.compileToBytes("net.minescript_custom_javaclasses.Config", source)
	return loader.loadFromBytes("net.minescript_custom_javaclasses.Config", bytes_)
