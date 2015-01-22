from UM.Job import Job
from UM.Application import Application

import os.path

##  A Job subclass that performs workspace loading.
#
#   The result of this Job is a MeshData object.
class LoadWorkspaceJob(Job):
    def __init__(self, filename):
        super().__init__(description = "Loading workspace {0}".format(os.path.basename(filename)), visible = True)
        self._filename = filename
        self._handler = Application.getInstance().getWorkspaceFileHandler()
        self._device = Application.getInstance().getStorageDevice('local')

    def run(self):
        self.setResult(self._handler.read(self._filename, self._device))
