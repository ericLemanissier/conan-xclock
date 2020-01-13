from conans import tools
import os
from conanfile_base import BaseLib

class xclockConan(BaseLib):
    basename = "xclock"
    name = basename.lower()
    version = "1.0.9"
    tags = ("conan", "xclock")
    description = '{description}'
    exports = ["conanfile_base.py"]
    requires = [ 'libx11/1.6.8@bincrafters/stable',
                 'libxt/1.2.0@bincrafters/stable',
                 'libxaw/1.0.13@bincrafters/stable',
                 'libxmu/1.1.3@bincrafters/stable',
                 'xproto/7.0.31@bincrafters/stable',
                 'libxrender/0.9.10@bincrafters/stable',
                 'libxft/2.3.3@bincrafters/stable',
                 'libxkbfile/1.1.0@bincrafters/stable']

    def source(self):
        url = "https://www.x.org/archive/individual/app/xclock-1.0.9.tar.gz"
        tools.get(url, sha256="4f0dd4d7d969b55c64f6e58242bca201d19e49eb8c9736dc099330bb0c5385b1")
        extracted_dir = "xclock-" + self.version
        os.rename(extracted_dir, self._source_subfolder)
    
    def build(self):
        super(xclockConan, self).build()
        self.run(os.path.join('source_subfolder', 'xclock'))
