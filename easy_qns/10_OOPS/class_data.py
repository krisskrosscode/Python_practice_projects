import os
import logging as lg

# if "logging" not in os.listdir():
#     os.mkdir("logging")
#     os.chdir("logging")
#     lg.basicConfig(filename="project.log", level=)


class data:
    def __init__(self, filename,filetype, date, size) -> None:
        try:
            self.filename = filename
            self.filetype = filetype
            self.date = date
            self.size = size
            self.logger("Initiated file")
        except Exception as e:
            self.logger(e)

    def file_open(self, filename):
        if filename not in os.listdir():
            f = open(filename, "w")
            f.write("------File begins here-----------\n\n")
            f.close()
    
    def file_read(self, filename):
        try:
            f = open(filename, "r")
            print(f.read())
            f.close()
            self.logger("read file " + filename)
        except Exception as e:
            self.logger(e)

    def file_append(self, filename, append_str):
        try:
            f = open(filename, "a")
            f.write(append_str + "\n")
            f.close()
            self.logger("\n-----Appended to file: " + '"' + append_str + '"' + "-------\n")
        except Exception as e:
            self.logger(e)
    def logger(self, msg):
        if "logging" not in os.listdir():
            os.mkdir("logging")

        if(type(msg) != str):
            msg = str(msg)
        os.chdir("logging")
        lg.basicConfig(filename= self.filename.split(".")[0] + ".log", level=lg.DEBUG, format = '%(asctime)s %(message)s')
        lg.debug(msg)
        os.chdir("..")
