# Taller DevSecOps - Planta Maipo Sur

Planta de agua potable simulada para el taller de DevSecOps sobre infraestructura crítica.

## Estructura

- `lector_cloro.py` — Servicio que lee el PLC y publica el valor de cloro.
- `config.yaml` — Configuración del servicio.
- `requirements.txt` — Dependencias Python.
- `infra/plc.tf` — Configuración de infraestructura (Terraform).
- `.github/workflows/seguridad.yml` — Pipeline de seguridad.
- `ENTREGABLE.md` — Ficha de entrega del taller.

## Cómo funciona el pipeline

Cada vez que haces push, se ejecuta `seguridad.yml` que corre:

1. **Gitleaks** — Busca secretos (contraseñas) escritos en el código.
2. **Semgrep** — Busca patrones peligrosos (SQL injection, comandos, etc.).
3. **Trivy** — Revisa dependencias y configuración insegura.
4. **OSV-Scanner** — Verifica si las dependencias tienen CVEs conocidos.

## Cómo corregir la contraseña olvidada

1. La contraseña está en `config.yaml`.
2. Debes sacarla del archivo y guardarla como secreto en GitHub:
   - Settings → Secrets and variables → Actions → New repository secret
   - Nombre: `PLC_PASSWORD`
   - Valor: (el que te asigne el facilitador)
3. En `config.yaml`, reemplaza la contraseña por `password_env: PLC_PASSWORD`.
4. Haz commit y verifica que el pipeline pase en verde.
