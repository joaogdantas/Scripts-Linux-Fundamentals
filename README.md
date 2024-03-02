# README.md

## Linux Fundamentals - Simple User and Group Management Script

Este é um script simples desenvolvido durante o curso de Linux Fundamentals. O script visa automatizar a criação de diretórios, grupos de usuários e a atribuição de permissões em um ambiente Linux.

### Conteúdo do Script

O script realiza as seguintes operações:

#### 1. Criação de Diretórios

```bash
mkdir /public
mkdir /adm
mkdir /ven
mkdir /sec
```

Foram criados diretórios pensando em setores de uma empresa.

#### 2. Criação de Grupos
```bash
groupadd GRP_ADM
groupadd GRP_VEN
groupadd GRP_SEC
```

Três grupos foram criados: GRP_ADM, GRP_VEN e GRP_SEC, que serão associados a usuários posteriormente.

#### 3. Criação de Usuários
```bash
useradd carlos -m -s /bin/bash -c "Carlos" -p $(openssl passwd -crypt senha123) -G GRP_ADM
useradd maria -m -s /bin/bash -c "Maria" -p $(openssl passwd -crypt senha123) -G GRP_ADM
useradd joao -m -s /bin/bash -c "Joao" -p $(openssl passwd -crypt senha123) -G GRP_ADM

useradd debora -m -s /bin/bash -c "Debora" -p $(openssl passwd -crypt senha123) -G GRP_VEN
useradd sebastiana -m -s /bin/bash -c "Sebastiana" -p $(openssl passwd -crypt senha123) -G GRP_VEN
useradd roberto -m -s /bin/bash -c "Roberto" -p $(openssl passwd -crypt senha123) -G GRP_VEN

useradd josefina -m -s /bin/bash -c "Josefina" -p $(openssl passwd -crypt senha123) -G GRP_SEC
useradd amanda -m -s /bin/bash -c "Amanda" -p $(openssl passwd -crypt senha123) -G GRP_SEC
useradd rogerio -m -s /bin/bash -c "Rogerio" -p $(openssl passwd -crypt senha123) -G GRP_SEC
```

Nove usuários foram criados e associados aos grupos GRP_ADM, GRP_VEN e GRP_SEC.

#### 4. Definição de Permissões
```bash
chown root:GRP_ADM /adm
chown root:GRP_VEN /ven
chown root:GRP_SEC /sec

chmod 770 /adm
chmod 770 /ven
chmod 770 /sec
chmod 777 /public
```

As permissões foram configuradas de acordo, garantindo acesso apropriado aos diretórios para os grupos correspondentes, cada grupo terá acesso total ao seu diretório mas nenhuma permissão nos demais. No público todos têm todas as permissões.

#### Como Executar o Script

Para executar o script, abra o terminal e copie e cole os comandos abaixo:

```bash
chmod +x ScriptIaCUsers.sh
./ScriptIaCUsers.sh
```