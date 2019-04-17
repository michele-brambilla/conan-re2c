import os

from conans import AutoToolsBuildEnvironment, ConanFile, tools


class Re2cConan(ConanFile):
    name = "re2c"
    version = "0.1"
    license = "<Put the package license here>"
    url = "https://github.com/skvadrik/re2c.git"
    description = "<Description of re2c here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "gcc"

    def source(self):
        pass
        self.run("git clone " + self.url)
        self.run("cd " + self.name)

    def build(self):
        pass
        with tools.chdir('re2c'):
            autotools = AutoToolsBuildEnvironment(self)
            self.run('./autogen.sh')
            autotools.configure(configure_dir=os.getcwd())
            autotools.make()
            autotools.install()

    def package(self):
        with tools.chdir('re2c'):
            self.copy("re2c", dst="bin", keep_path=False)

    def package_info(self):
        self.cpp_info.bindirs = ["bin"]
