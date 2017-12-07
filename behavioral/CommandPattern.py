class Command(object):
    def execute(self):
        pass

    def undo(self):
        pass


class FileCommand(Command):
    def __init__(self, command):
        self.command = command

    def execute(self):
        print 'execute %s' % self.command

    def undo(self):
        print 'undo execute %s' % self.command


class CommandHistory(object):
    def __init__(self):
        self._history = list()

    def execute(self, command):
        command.execute()
        self._history.append(command)

    def undo(self):
        command = self._history.pop()
        command.undo()


history = CommandHistory()

history.execute(FileCommand('copy file'))
history.execute(FileCommand('write file'))

history.undo()
history.undo()
