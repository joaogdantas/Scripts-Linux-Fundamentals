#!/usr/bin/env python3
import os
import subprocess
import crypt

def main():
    print("Criando diretórios")
    os.makedirs("/public", exist_ok=True)
    os.makedirs("/adm", exist_ok=True)
    os.makedirs("/ven", exist_ok=True)
    os.makedirs("/sec", exist_ok=True)

    print("Criando grupos")
    subprocess.run(["groupadd", "GRP_ADM"])
    subprocess.run(["groupadd", "GRP_VEN"])
    subprocess.run(["groupadd", "GRP_SEC"])

    print("Criando usuários")
    users = [
        ("carlos", "Carlos", "GRP_ADM"),
        ("maria", "Maria", "GRP_ADM"),
        ("joao", "Joao", "GRP_ADM"),
        ("debora", "Debora", "GRP_VEN"),
        ("sebastiana", "Sebastiana", "GRP_VEN"),
        ("roberto", "Roberto", "GRP_VEN"),
        ("josefina", "Josefina", "GRP_SEC"),
        ("amanda", "Amanda", "GRP_SEC"),
        ("rogerio", "Rogerio", "GRP_SEC")
    ]
    for username, name, group in users:
        password = "senha123"
        hashed_password = crypt.crypt(password, crypt.mksalt(crypt.METHOD_SHA512))
        subprocess.run([
            "useradd",
            username,
            "-m",
            "-s", "/bin/bash",
            "-c", name,
            "-G", group,
            "-p", hashed_password
        ])

    print("Definindo permissões")
    subprocess.run(["chown", "root:GRP_ADM", "/adm"])
    subprocess.run(["chown", "root:GRP_VEN", "/ven"])
    subprocess.run(["chown", "root:GRP_SEC", "/sec"])
    os.chmod("/adm", 0o770)
    os.chmod("/ven", 0o770)
    os.chmod("/sec", 0o770)
    os.chmod("/public", 0o777)

if __name__ == "__main__":
    main()
