from abc import ABC, abstractmethod
import datetime


class Write(ABC):
    def __init__(self, file_name):
        self.file_name = file_name
        self.dt_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    @abstractmethod
    def write(self, data):
        return
    def write_line(self, data):
        f = open(self.file_name, "a+")
        f.write(self.dt_str + "\t" + data + "\n")
        f.close()

class LogFile(Write):
    def write(self, data):
        self.write_line(data)


class DelimFile(Write):
    def __init__(self, file_name, delim):
        super(DelimFile, self).__init__(file_name)
        self.delim = delim

    def write(self, data):
        data = self.delim.join(data)
        self.write_line(data)

#testing
log = LogFile('log.txt')
mydelim = DelimFile('data.csv',',')
log.write('this is a log message')   # writes a message to the file
log.write('this is another log message')
mydelim.write(['a', 'b', 'c', 'd'])       # writes a list of values separated
                                          # by comma to the file
mydelim.write(['1', '2', '3', '4'])       # same
