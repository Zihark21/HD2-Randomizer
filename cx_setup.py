from cx_Freeze import setup, Executable

build_options = {
    "build_exe": {
        "build_exe": 'HD2',
        "include_files": ['assets', 'lists'],
        "optimize": 2,
        'silent': 1
    }
}

setup(
    name="HD2",
    version="1.0",
    description="",
    options=build_options,
    executables=[Executable("HD2-Randomizer.py", base="Win32GUI", icon='assets/HD2.ico')],
)