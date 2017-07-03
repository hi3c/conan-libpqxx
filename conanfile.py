from conans import ConanFile, CMake, tools
import os
import shutil

class LibpqxxConan(ConanFile):
    name = "libpqxx"
    version = "5.0.1_1"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"
    exports = "CMakeLists.txt"
    requires = "libpq/9.6.3@hi3c/experimental"

    def source(self):
        tools.download("https://github.com/jtv/libpqxx/archive/5.0.1.tar.gz", "libpqxx.tar.gz")
        tools.unzip("libpqxx.tar.gz")
        os.remove("libpqxx.tar.gz")

        shutil.copy("CMakeLists.txt", "libpqxx-5.0.1")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_dir="libpqxx-5.0.1")
        cmake.build()

    def package(self):
        self.copy("*", src="libpqxx-5.0.1/include", dst="include")
        self.copy("*", src="libpqxx-5.0.1/config/sample-headers/compiler/VisualStudio2013", dst="include")
        self.copy("*.lib", src="lib", dst="lib")
        if self.options.shared:
            self.copy("*.dll", src="bin", dst="bin")
            self.copy("*.so*", src=".", dst="lib")
            self.copy("*.dylib", src=".", dst="lib")
        else:
            self.copy("*.a", src=".", dst="lib")

    def package_info(self):
        self.cpp_info.libs = ["pqxx"]

        if self.settings.os == "Windows":
            self.cpp_info.libs = ["libpqxx"]
