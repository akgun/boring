# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['.'],
             binaries=[],
             datas=[
                 # TODO: I'm too old for this shit
                 ('venv/lib/python3.6/site-packages/wikiquote/langs', 'wikiquote/langs')
             ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='boring',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
