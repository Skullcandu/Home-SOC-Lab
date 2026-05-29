# 🛡️ Laboratorio de Operaciones de Seguridad (SOC) y Monitoreo Defensivo

## 🎯 Objetivo del Proyecto
Implementación de una arquitectura de seguridad defensiva en un entorno de laboratorio para la detección, gestión y mitigación automatizada de amenazas en la red. 

## 🗺️ Topología de Red y Arquitectura del Laboratorio

El entorno fue diseñado simulando una red corporativa segmentada, utilizando máquinas virtuales independientes para representar cada rol dentro del ciclo de ataque, detección y respuesta:

* **💻 Windows Server (Entorno Víctima):**
  * Actúa como el servidor objetivo en la red.
  * Configurado con **Sysmon** (System Monitor) para la captura avanzada de telemetría y eventos del sistema.
  * Cuenta con el **Agente de Wazuh** para la recolección y reenvío seguro de logs hacia el SIEM.

* **🛡️ Ubuntu Linux (Centro de Operaciones y Defensa):**
  * Funciona como el núcleo defensivo de la infraestructura.
  * Aloja el **Wazuh Manager** para la correlación y análisis de los eventos recibidos.
  * Ejecuta **Suricata** monitoreando el tráfico de red y **Fail2Ban** para ejecutar la respuesta activa y bloqueos en el firewall.

* **⚔️ Kali Linux (Entorno Atacante / Red Team):**
  * Máquina adversaria utilizada para lanzar simulaciones de ataque (escaneos con Nmap, fuerza bruta, explotación con Metasploit) y generar la telemetría maliciosa que pone a prueba las reglas del SOC.

* **🔍 OpenVAS (Gestión de Vulnerabilidades):**
  * Desplegado en una máquina virtual independiente para ejecutar análisis de vulnerabilidades y auditorías preventivas sobre los nodos de la red.
