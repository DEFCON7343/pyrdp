#!/usr/bin/env python

from distutils.core import setup, Extension

setup(name='rdpy',
    version='1.3.2',
    description='Remote Desktop Protocol in Python',
    long_description="""
    RDPY is a pure Python implementation of the Microsoft RDP (Remote Desktop Protocol) protocol (Client and Server side). RDPY is built over the event driven network engine Twisted.
    
    RDPY provide RDP and VNC binaries : RDP Man In The Middle proxy which record session, RDP Honeypot, RDP screenshoter, RDP client, VNC client, VNC screenshoter, RSS Player
    """,
    author='Sylvain Peyrefitte',
    author_email='citronneur@gmail.com',
    url='https://github.com/citronneur/rdpy',
    packages=[
        'rdpy',
        'rdpy.core',
        'rdpy.security',
        'rdpy.protocol',
        'rdpy.protocol.rdp',
        'rdpy.protocol.rdp.pdu',
        'rdpy.protocol.rdp.nla',
        'rdpy.protocol.rdp.t125',
        'rdpy.protocol.rfb',
        'rdpy.ui',

        'rdpy.enum',
        'rdpy.enum.virtual_channel',
        'rdpy.enum.virtual_channel.clipboard',
        'rdpy.layer',
        'rdpy.layer.rdp',
        'rdpy.layer.rdp.virtual_channel',
        'rdpy.layer.rdp.virtual_channel.clipboard',
        'rdpy.mcs',
        'rdpy.mitm',
        'rdpy.mitm.virtual_channel',
        'rdpy.mitm.virtual_channel.clipboard',
        'rdpy.parser',
        'rdpy.parser.rdp',
        'rdpy.parser.rdp.virtual_channel',
        'rdpy.parser.rdp.virtual_channel.clipboard',
        'rdpy.pdu',
        'rdpy.pdu.rdp',
        'rdpy.pdu.rdp.virtual_channel',
        'rdpy.pdu.rdp.virtual_channel.clipboard',
        'rdpy.recording',
        'rdpy.security',
    ],
    ext_modules=[Extension('rle', ['ext/rle.c'])],
    scripts=[
            'bin/rdpy-rdpmitm.py',
            'bin/rdpy-player.py'
    ],
    install_requires=[
            'twisted',
            'pyopenssl',
            'service_identity',
            'qt4reactor',
            'rsa',
            'pyasn1',
            'notify2',
            'Crypto',
            'appdirs'
    ],
)
