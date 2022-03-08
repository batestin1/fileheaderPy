from art import *
from datetime import date
import getpass
import platform


def scriptHeaderPy(usuario=getpass.getuser(), arquivo=input("What is the name of your project(s)?"), quat = int(input("How many files do you want to generate? "))):
        num = 0
        for num in range(quat):
            num=num+1
            path = f"{arquivo}_{num}.py"
            with open(path, "w", encoding='UTF-8') as output:
                title = text2art(f"Hello,{usuario}!", font='fancy1',chr_ignore=False)
                file_name = f"filename: {arquivo}_{num}.py"
                so = platform.system()
                system = f"system: {so}"
                ma = platform.architecture()
                bit = f"version: {ma[0]}"
                by = f"by: {usuario} <https://github.com/{usuario.lower()}>"
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
                print("Arquivo(s) construido(s) com Sucesso!")
