#pip install -r requirements.txt
from art import *
from datetime import date
import getpass
import platform
import subprocess
import os
import sys



def fileheaderPy(file):
        try:
                users=getpass.getuser()
                res = subprocess.run(["git", "config", "user.name"], stdout=subprocess.PIPE)
                git_username = res.stdout.strip().decode()
                fileName = file.replace(' ', '_')

                with open(f"{fileName}.py", "w", encoding='UTF-8') as output:
                    title = text2art(f"Hello,{users}!", font='fancy1',chr_ignore=False)
                    file_name = f"filename: {fileName}.py"
                    so = platform.system()
                    system = f"system: {so}"
                    ma = platform.architecture()
                    bit = f"version: {ma[0]}"
                    by = f"by: {users} <https://github.com/{git_username}>"
                    data_atual = date.today()
                    data = f"""created: {data_atual.strftime('%Y-%m-%d')}"""
                    ast = '*'
                    spac = ' '
                    final = "import your librarys below"

                    output.write(f"""

                        #{ast.ljust(80,ast)}#
                        #{spac.ljust(80,spac)}#
                        #{title.center(80)}#
                        #{spac.ljust(80,spac)}#
                        #   {file_name[:50].ljust(77)}#
                        #   {data.ljust(77)}#
                        #   {system.ljust(77)}#
                        #   {bit.ljust(77)}#
                        #   {by.rjust(76)} #
                        #{ast.ljust(80,ast)}#
                        #{final.center(80)}#
                        #{ast.ljust(80,ast)}#

                        """)
                    print(f"the {fileName}.py was built successfully!")
                    print(f"the {fileName}.py is locate here: {os.path.abspath(os.getcwd())}\{fileName}.py")
        except:
                users=getpass.getuser()
                res = subprocess.run(["git", "config", "user.name"], stdout=subprocess.PIPE)
                git_username = res.stdout.strip().decode()
                fileName = file.replace(' ', '_')

                with open(f"{fileName}.py","w", encoding='UTF-8') as output:
                    title = text2art(f"Hello, coder !", font='fancy1',chr_ignore=False)
                    file_name = f"filename: {fileName}.py"
                    so = platform.system()
                    system = "system: coder!"
                    ma = platform.architecture()
                    bit = "version: coder!"
                    by = f"by: coder <https://github.com/coder>"
                    data_atual = date.today()
                    data = f"""created: {data_atual.strftime('%Y-%m-%d')}"""
                    ast = '*'
                    spac = ' '
                    final = "import your librarys below"

                    output.write(f"""

                        #{ast.ljust(80,ast)}#
                        #{spac.ljust(80,spac)}#
                        #{title.center(80)}#
                        #{spac.ljust(80,spac)}#
                        #   {file_name[:50].ljust(77)}#
                        #   {data.ljust(77)}#
                        #   {system.ljust(77)}#
                        #   {bit.ljust(77)}#
                        #   {by.rjust(76)} #
                        #{ast.ljust(80,ast)}#
                        #{final.center(80)}#
                        #{ast.ljust(80,ast)}#

                        """)
                    print(f"the {fileName}.py was built successfully!")