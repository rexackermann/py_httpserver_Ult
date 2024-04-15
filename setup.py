from setuptools import setup

setup(
    package_dir={"pyrobox": "src",},
    install_requires=[
        'natsort',
        "send2trash",
        "msgpack",
        "pyqrcode",
    ],
    entry_points='''
        [console_scripts]
        pyrobox=pyrobox:server.run
    ''',

    
)