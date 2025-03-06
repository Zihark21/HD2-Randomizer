import PyInstaller.__main__, os, shutil

ico = os.path.join('assets', 'HD2.ico')

options = [
    '--clean',
    '--noconfirm',
    '--optimize=2',
    '--onefile',
    '--noconsole',
    '--log-level=WARN',
    f'--icon={ico}',
    f'--add-data=assets;assets',
    f'--add-data=src;src',
    f'--add-data=ui;ui',
    'HD2-Randomizer.py'
]

PyInstaller.__main__.run(options)

shutil.copytree("lists", "dist/lists", dirs_exist_ok=True)
shutil.copy("LICENSE", "dist")
shutil.copy("README.md", "dist")
shutil.make_archive("HD2-Randomizer", 'zip', "dist")

for folder in ['dist', 'build']:
    if os.path.exists(folder):
        shutil.rmtree(folder)

if os.path.exists('HD2-Randomizer.spec'):
    os.remove('HD2-Randomizer.spec')