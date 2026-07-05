# Awesome Intune Tools

[![](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

A curated list of the most useful and awesome community tools for managing Microsoft Intune. Feel free to contribute!

## Table of Contents
- [Device Management](#device-management)
- [Troubleshooting & Debugging](#troubleshooting--debugging)
- [Backup & Restore](#backup--restore)
- [Security](#security)
- [Automation](#automation)
- [Miscellaneous](#miscellaneous)

## Device Management
- **[Intune Maps – Shehan Perera](https://intunemaps.com/)** – Visual map of Intune blades and documentation to speed up portal navigation.[web:18]

- **[Rockn Roll Tool – Nicklas Ahlberg](https://www.rockenroll.tech/)** – Powerful management tools for Intune environments (policies, apps, Autopilot, helpdesk utilities).[web:16]

- **[Rock My Printers – Nicklas Ahlberg](https://www.rockenroll.tech/2023/03/14/rock-my-printers/)** – Simplifies printer management via Intune-managed devices.[web:16]

- **[Intune Remediation Repo – Jannik Reinhard](https://github.com/JayRHa/EndpointAnalyticsRemediationScripts)** – Large repository of Endpoint Analytics proactive remediation scripts for common Intune issues.[web:16]

- **[Intune Management – Mikael Karlsson](https://github.com/Micke-K/IntuneManagement)** – PowerShell + WPF GUI to copy, export, import, delete, document, and compare Intune policies and profiles, with ADMX ingestion and cross‑tenant migration support.[web:121][web:124]

- **[Device Offboarding Manager – Ugur Koc](https://github.com/ugurkocde/DeviceOffboardingManager)** – PowerShell GUI for bulk offboarding devices from Intune, Autopilot, and Entra ID with dashboards, stale device tracking, and BitLocker/FileVault key handling.[web:78][web:83]

- **[IntuneStuff Management Tool – Joery Van den Bosch](https://intunestuff.tools/)** – Windows desktop GUI for bulk Intune device operations and Entra ID group management with advanced filtering, dry‑run safety, and logging.[web:75][web:106]

- **[Intune Autopilot Tool – iamwillcode](https://github.com/iamwillcode/Intune-Autopilot-Tool)** – PowerShell WPF tool to onboard devices to Intune/Autopilot via Graph API, handling encryption, profiles, user assignment, and hardware checks.[web:122]

## Troubleshooting & Debugging
- **[System Information and Self-service Tool – Jannik Reinhard](https://jannikreinhard.com/2023/01/01/system-information-and-self-service-tool/)** – End‑user facing self‑service app showing device info and basic troubleshooting actions.[web:16]

- **[Device Validation Tool](https://www.powerofpowershell.com/post/device-validation-with-powershell-wpf-gui-post-imaging-or-autopilot)** – WPF GUI for validating devices post‑imaging or Autopilot (hardware, configuration, readiness checks).[web:16]

- **[Intune Debug Toolkit – Mattias Melkersen](https://github.com/MSEndpointMgr/IntuneDebugToolkit)** – Toolbox to troubleshoot Intune‑managed clients (Win32 re‑deploy, Autopilot/ESP, SyncML viewer, device event log helpers, and bundled community tools).[web:6][web:18]

- **[Intune Device Details UI – Petri Paavola](https://github.com/petripaavola/IntuneDeviceDetailsGUI)** – GUI providing Resultant Set of Policy‑style view of Intune device and user details, app and configuration deployments.[web:6][web:18]

- **[Get‑IntuneManagementExtensionDiagnostics – Petri Paavola](https://github.com/petripaavola/Get-IntuneManagementExtensionDiagnostics)** – Script that parses Intune Management Extension logs and builds an HTML timeline, plus a Log Viewer UI for detailed IME troubleshooting.[web:59][web:6]

- **[Intune Device Troubleshooter – Jannik Reinhard](https://github.com/JayRHa/IntuneDeviceTroubleshooter)** – PowerShell desktop UI for fast, device‑level Intune troubleshooting combining device data, compliance, app states, and remediation actions.[web:9]

- **[Get‑WindowsTroubleshootingReportCommunity – Petri Paavola](https://github.com/petripaavola/Get-WindowsTroubleshootingReportCommunity)** – Ultimate Windows and Intune troubleshooting tool that unifies Event Logs and Intune log files into a single interactive HTML timeline report.[web:117][web:134]

- **[Intune Log Reader for Windows – Somesh Pathak](https://github.com/pathaksomesh06/Intune-Log-Reader-for-Windows)** – Desktop app that provides real‑time analysis and monitoring of Intune Management Extension logs with dashboards, search, and export.[web:49][web:51]

- **[IntuneDiag – dsregcmd Analyzer](https://www.intunediag.com/)** – Web tool that analyzes `dsregcmd /status` output, showing Entra join state, certificate validity, PRT attempts, and registration issues with actionable guidance.[web:37][web:112]

- **[IntuneEndpointTools – David Just](https://github.com/djust270/IntuneEndpointTools)** – PowerShell module with functions like Get‑IntuneEventLogs and Get‑IntuneMDMDiagReport for quickly gathering Intune client diagnostics and MDMDiagnostics reports.[web:137]

- **[IntunePremier – Shepherd0619](https://github.com/Shepherd0619/IntunePremier)** – Set of open‑source tools to help helpdesk staff with daily Intune troubleshooting tasks.[web:135]

## Backup & Restore
- **[Intune Backup/Restore PowerShell Module – John Seerden](https://github.com/jseerden/IntuneBackupAndRestore)** – Scripted backup and restore of Intune configurations (policies, apps, settings) across tenants.[web:16]

- **[Automatic Microsoft 365 Documentation – Thomas Kurth](https://www.wpninjas.ch/2021/05/automatic-intune-documentation-evolves-to-automatic-microsoft365-documentation/)** – Automated documentation engine that generates Intune and Microsoft 365 configuration documentation.[web:16]

- **[TenuVault – Ugur Koc](https://ugurlabs.com/tools/tenuvault)** – Community backup solution for Intune, offering scheduled backups, configuration drift detection, and one‑click restores across multiple tenants.[web:117]

## Security
- **[BitLocker PIN – Intune – Oliver Kieselbach](https://oliverkieselbach.com/2019/08/02/how-to-enable-pre-boot-bitlocker-startup-pin-on-windows-with-intune/)** – Deep‑dive guide on enabling pre‑boot BitLocker startup PIN via Intune policy and deployment.[web:19]

- **[DCToolbox – Daniel Chronlund](https://danielchronlund.com/2020/11/09/dctoolbox-powershell-module-for-microsoft-365-security-conditional-access-automation-and-more/)** – PowerShell module for automating Microsoft 365 security and Conditional Access operations and documentation.[web:19]

- **[Windows LAPS Self‑Service Portal – Daniel Fraubaum](https://github.com/daniel-fraubaum/Intune-LAPS-SelfServicePortal)** – Azure Static Web Apps + Functions solution letting users securely retrieve the LAPS password for their own device with full audit trail.[web:54]

- **[Windows Hardening – R33Dfield](https://github.com/R33Dfield/WindowsHardening)** – Hardening scripts and baselines that can be deployed via Intune for stricter Windows security.[web:16]

## Automation
- **[Intune Script Viewer – Trevor Jones](https://smsagent.blog/2022/05/11/script-viewer-for-microsoft-endpoint-manager/)** – Script viewer/manager for Intune PowerShell scripts with search, filtering, and editing support.[web:16]

- **[IntuneCD – Tobias Almen](https://almenscorner.io/introducing-intunecd-tool/)** – CI/CD tool to export and deploy Intune configurations from source control pipelines.[web:16]

- **[Scloud's Florian – Proactive Remediation for Business](https://scloud.work/proactive-remediation-for-business/)** – Opinionated framework and examples for Intune proactive remediations in business environments.[web:16]

- **[Intune Assignment Checker – Ugur Koc](https://github.com/ugurkocde/IntuneAssignmentChecker)** – PowerShell module and scripts to analyze and audit Intune assignments for users, groups, and devices, including HTML reports, unassigned policies, and empty group detection.[web:23][web:27][web:31]

- **[Intune Assistant – Sander Rozemuller](https://intuneassistant.cloud/)** – Web‑based platform for assignment insights, configuration analysis, rollout assistance, and reporting across Intune tenants (community core, optional premium modules).[web:67][web:110][web:105]

- **[Intune Toolkit – Maxime Guillemin](https://github.com/MG-Cloudflow/Intune-Toolkit)** – PowerShell‑based toolkit with UI for connecting to Graph, managing policy assignments, and handling backup/restore of assignments.[web:8][web:36]

- **[Intune Registry Builder – Daniel Fraubaum](https://headsinthecloud.blog/intuneregistrybuilder/)** – Browser‑based tool to define registry changes and generate Intune‑ready detection/remediation scripts or Win32 app bundles, with optional direct push of remediations.[web:56][web:54]

- **[cmd.ms – Microsoft Cloud Command Line – Merill Fernando](https://cmd.ms)** – URL‑based “command line” and browser extension to jump straight to Azure, Entra, Intune, Defender, and other admin blades using short commands.[web:18][web:90][web:92]

- **[DUDE Manager – Daniel Petri](https://skotheimsvik.no/toolbox-rundown/#dude-manager)** – GUI to deploy and monitor the DUDE automation engine that syncs Intune device groups with Entra user groups.[web:117]

## Miscellaneous
- **[IntuneWin Build and Extract Tool – Damien Van Robaeys](https://www.systanddeploy.com/2023/05/intunewin-build-and-extract-tool-to.html)** – GUI tool to build and extract .intunewin packages for Intune Win32 apps.[web:16]

- **[Intune Drive Mapping Generator – Nicola Suter](https://intunedrivemapping.azurewebsites.net/)** – Web generator for Intune drive‑mapping policies targeting users and devices.[web:16]

- **[Enhanced Inventory for Intune – Jan Ketil Skanke](https://msendpointmgr.com/2022/01/17/securing-intune-enhanced-inventory-with-azure-function/)** – Azure Function‑based solution that enriches Intune inventory data for reporting and security.[web:16]

- **[Intune Log Reader for Windows App Health Check Remediation – Niall Brady & Paul Winstanley](https://github.com/niallbrady/WindowsAppHealthCheckLogReader)** – Intune remediation solution that copies Windows app health check logs into IntuneManagementExtension logs for easier remote diagnostics.[web:119]

- **[Intune Premier Toolbox – Simon Skotheimsvik’s Toolbox Rundown](https://skotheimsvik.no/toolbox-rundown/)** – Curated list of endpoint‑management tools including Intune Assignment Checker, Intune Debug Toolkit, Intune Diff, and more, useful as a discovery hub.[web:117]

---

## License

[![Creative Commons](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)
This list is licensed under a Creative Commons Attribution 4.0 International License.
