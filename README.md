# py2teams

Utilidad en **python** para enviar la salida de un comando a un canal de **Microsoft Teams**.

![](./imgs/py2teams_logo.png)

##### Configuración
- Añadir el webhook al `config_template.py` y renombrar a `config.py`
- Crear alias:
  ```
  alias py2teams='python3 /cygdrive/c/Users/aalonsof/PycharmProjects/py2teams/py2teams.py'
  ```

##### Ejemplo de uso
```sh
$ nslookup www.prosodie.com 8.8.8.8 |& py2teams
```

![](./imgs/ejemplo_teams.jpg)

