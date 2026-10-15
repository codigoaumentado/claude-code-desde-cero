# claude-code-desde-cero

Proyecto de ejemplo del video **"Claude Code desde cero"** del canal [Código Aumentado](https://www.youtube.com/@codigoaumentado).

Una calculadora para dividir la cuenta de un grupo, con propina. Es pequeña a propósito: sirve para practicar el flujo completo de Claude Code (explorar, planificar, implementar con tests y verificar).

| Tag | Qué tiene |
|---|---|
| `antes` | El bug: 100 entre 3 personas cobra $99.99. Los tests pasan igual (92 % de cobertura) |
| `despues` | El arreglo con test primero, validaciones y la configuración de Claude Code |

## Requisitos
- Python 3.11 o superior
- [Claude Code](https://code.claude.com/docs/en/setup) (requiere un plan Pro, Max, Team, Enterprise o una cuenta de Console)

## Uso
```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements-dev.txt
.venv/bin/pytest
.venv/bin/python -m cuentas 100 3 --propina 10
```

## Configuración de Claude Code incluida
| Archivo | Para qué |
|---|---|
| `CLAUDE.md` | Memoria del proyecto: comandos, reglas de negocio y forma de trabajar |
| `.claude/settings.json` | Permisos (qué puede correr sin preguntar y qué nunca) y un hook |
| `.claude/hooks/formatear.sh` | Formatea con ruff cada `.py` que Claude edita (requiere `jq`) |
| `.claude/skills/nueva-regla/SKILL.md` | `/nueva-regla <regla>`: agrega una regla con el test primero |
| `.claude/agents/revisor.md` | Subagente que revisa el diff antes del commit |

## Prompts del video
```text
Explícame este proyecto: qué hace, cómo se prueba y dónde están las reglas de negocio.
```
```text
/plan Al dividir 100 entre 3 personas se cobran 99.99: se pierde un centavo.
Propón cómo arreglarlo para que la suma sea exacta, sin usar float.
Primero escribe un test que demuestre el bug y confirma que falla.
```
```text
/nueva-regla rechazar total negativo, cero personas y propina fuera de 0 a 100, con mensajes en español
```
```text
Usa el subagente revisor para revisar el cambio antes del commit.
```

## Licencia
MIT
