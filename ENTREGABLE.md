# Ficha de blindaje

## Sistema y equipo
- Sector: Agua potable
- Nombre: Maipo Sur - Los Pillos del Sure
- Roles:
  - Operador de planta: Alexander
  - Desarrollador: Valentina
  - Guardián del pipeline: Alexander
  - Auditor de IA: Valentina
  - Relator: Alexander

## Tres amenazas
1. Suplantación (S) / Credencial de fábrica del PLC accesible en el código / Si un atacante la obtiene, puede abrir válvulas y alterar la dosificación de cloro / Control: Gitleaks + gestión de secretos.
2. Manipulación (T) / Dependencias sin versión fijada con CVEs conocidos / Un atacante puede explotar Flask 2.0.1 para ejecutar código / Control: Trivy + fijar versiones exactas.
3. Elevación de privilegios (E) / Configuración de Terraform con acceso abierto a internet (0.0.0.0/0) / Cualquiera puede intentar conectarse al PLC desde internet / Control: Trivy config + restringir CIDR.

## Controles
- Enlace a Actions: https://github.com/valentinaleon-star/maipo-sure-Alexander-Ruiz-Tagle-Valentina-Leon/actions/runs/37483920492
- Controles ejecutados: Gitleaks, Semgrep, Trivy fs, Trivy config, OSV-Scanner

## Hallazgo y decisión
- Hallazgo: Gitleaks detectó `password: "admin123"` en `config.yaml` línea 14 (Rule ID: plc-password-fabrica).
- Gravedad: Crítico (credencial de fábrica expuesta en repositorio).
- Decisión y justificación: Corregir ahora. Se retiró la contraseña del archivo y se reemplazó por `password_env: PLC_PASSWORD`. Se creó el secreto en GitHub. Pendiente: rotar la credencial en el PLC real (simulado).
- Responsable y fecha: Alexander Ruiz-Tagle, Valentina León], 2026-10-06.

## Parche de IA
- Paquete verificado: No. `plc_helper_utils` no existe en PyPI.
- Tratamiento de entradas: Inseguro. Concatena texto en `subprocess.run(..., shell=True)`.
- Protecciones desactivadas: Sí. `verify=False` desactiva la validación TLS.
- Destino de datos: `http://telemetria-externa.example.com/upload`, no justificado.
- Veredicto y evidencia: RECHAZAR. Combina paquete no verificado, shell injection, TLS desactivado y envío de datos a destino desconocido.

## Pendientes para un sistema real
- Rotar la credencial en el PLC real.
- Limpiar el historial de Git (git filter-repo o BFG).
- Fijar versiones exactas de dependencias y actualizar Flask, PyYAML, requests.
- Restringir el CIDR de acceso al PLC a la red operacional.
- Auditar el paquete `plc_helper_utils` antes de instalarlo.
