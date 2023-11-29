# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['06_simpleCalculator_2.py'],
             pathex=['/home/rgregor/majstaf/coding/PYTHON_d/PYTHON_d_testing/pn074_gui-simple-calculator-with-tkinter_20210610/simple_calculator'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='06_simpleCalculator_2',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
