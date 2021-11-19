import cx_Freeze
executables = [cx_Freeze.Executable(script ="jogo.py", icon="assets/aranhaicone.ico")]

cx_Freeze.setup(
    name="Spider Man Dead",
    options= {"buil_exe":{
        "packages":["pygame"],
        "include_files": ["assets"]
    }},
    executables=executables
)