# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Hunspell(AutotoolsPackage):
    """The most popular spellchecking library (sez the author...)."""

    homepage = "http://hunspell.github.io/"
    url      = "https://github.com/hunspell/hunspell/archive/v1.6.0.tar.gz"

    version('1.7.0', sha256='57be4e03ae9dd62c3471f667a0d81a14513e314d4d92081292b90435944ff951')
    version('1.6.0', sha256='512e7d2ee69dad0b35ca011076405e56e0f10963a02d4859dbcc4faf53ca68e2')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')
    depends_on('gettext')

    # TODO: If https://github.com/spack/spack/pull/12344 is merged, this
    # method is unnecessary.
    def autoreconf(self, spec, prefix):
        autoreconf = which('autoreconf')
        autoreconf('-fiv')
