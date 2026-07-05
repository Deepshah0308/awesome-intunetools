# Awesome Intune Tools

[![](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

A curated list of the most useful and awesome community tools for managing Microsoft Intune. Feel free to contribute!

## Table of Contents
- [How to Use This List](#how-to-use-this-list)
- [Contributing](#contributing)
- [Device Management](#device-management)
- [Troubleshooting & Debugging](#troubleshooting--debugging)
- [Backup & Restore](#backup--restore)
- [Security](#security)
- [Automation](#automation)
- [Miscellaneous](#miscellaneous)

## How to Use This List

This list is designed for Intune consultants, MSPs, and in‑house admins who want a practical toolbox instead of just documentation.

- **Tenant audit starter kit**  
  Begin with:
  - Device and policy overview: Intune Management, IntuneStuff Management Tool, Intune Toolkit.  
  - Assignment visibility: Intune Assignment Checker, Intune Assistant.  
  - Inventory and drift: Enhanced Inventory for Intune, TenuVault.

- **Troubleshooting toolkit for helpdesk/operations**  
  Recommended core set:
  - Day‑to‑day device troubleshooting: Intune Debug Toolkit, Intune Device Details UI, Intune Device Troubleshooter, IntunePremier.  
  - Log and timeline analysis: Get‑IntuneManagementExtensionDiagnostics, Intune Log Reader for Windows, Get‑WindowsTroubleshootingReportCommunity.  
  - Registration and connectivity issues: IntuneDiag (dsregcmd Analyzer), IntuneEndpointTools.

- **Packaging and configuration pipeline**  
  Combine these tools with your own packaging flow (for example Winget2Intune or the Win32 Content Prep Tool):
  - Win32 packaging: IntuneWin Build and Extract Tool, Intune Autopilot Tool for onboarding, Intune Registry Builder for registry‑based settings.  
  - Policy and assignment automation: IntuneCD, Intune Toolkit, DUDE Manager.  
  - Navigation and admin productivity: cmd.ms to jump quickly between Azure, Entra, Intune and Defender blades.

Treat this README as a directory: pick 2–3 tools per use case, test them in a lab tenant, and then standardize them into your consulting or MSP “baseline toolkit”.

## Contributing

Contributions from the Intune community are very welcome.

### What belongs here

- Community‑built tools, scripts, modules, or web apps that help manage, troubleshoot, secure, or automate Intune.  
- Free or primarily community/open‑source projects (commercial SaaS with aggressive marketing is out of scope).  
- Well‑maintained or realistically usable tools (tested on modern Intune tenants, documented enough for others to adopt).

### How to contribute

1. **Fork the repository**  
   Go to [awesome-intunetools](https://github.com/Deepshah0308/awesome-intunetools) and create a fork.

2. **Create a branch**  
   Use a descriptive name, for example:
   - `feature/add-intune-assignment-tool`  
   - `docs/update-troubleshooting-section`

3. **Add your entry**  
   - Edit `README.md`.  
   - Add your tool to the bottom of the most appropriate section.  
   - Use this format:

   ```markdown
   - **[Tool Name – Author](https://link-to-tool-or-repo)** – One‑sentence description of what problem it solves and why it’s useful.
   ```

   - Link to the canonical GitHub repo or project website (not a marketing landing page).  
   - Keep descriptions short, clear, and non‑marketing.

4. **Open a Pull Request**  
   - Explain briefly what you’re adding and why it’s helpful for Intune admins.  
   - If your tool overlaps with an existing one, call out what’s unique (e.g., focuses on macOS, adds HTML reports, supports multi‑tenant, etc.).

### Guidelines

- Only suggest tools you have used or can reasonably recommend.  
- Avoid vendor marketing copy; describe the practical value instead.  
- Group tools logically under existing sections—propose new sections only if the scope clearly doesn’t fit any current ones.  
- Keep the markdown clean: proper headings, consistent bullet formatting, and working links.

If you’re unsure where your tool fits, open an issue first and we can discuss where it should live.

## Device Management

- **[Intune Maps – Shehan Perera](https://intunemaps.com/)** – Visual map of Intune blades and documentation to speed up portal navigation.

- **[Rockn Roll Tool – Nicklas Ahlberg](https://www.rockenroll.tech/)** – Powerful management tools for Intune environments (policies, apps, Autopilot, helpdesk utilities).

- **[Rock My Printers – Nicklas Ahlberg](https://www.rockenroll.tech/2023/03/14/rock-my-printers/)** – Simplifies printer management via Intune-managed devices.

- **[Intune Remediation Repo – Jannik Reinhard](https://github.com/JayRHa/EndpointAnalyticsRemediationScripts)** – Large repository of Endpoint Analytics proactive remediation scripts for common Intune issues.

- **[Intune Management – Mikael Karlsson](https://github.com/Micke-K/IntuneManagement)** – PowerShell + WPF GUI to copy, export, import, delete, document, and compare Intune policies and profiles, with ADMX ingestion and cross‑tenant migration support.

- **[Device Offboarding Manager – Ugur Koc](https://github.com/ugurkocde/DeviceOffboardingManager)** – PowerShell GUI for bulk offboarding devices from Intune, Autopilot, and Entra ID with dashboards, stale device tracking, and BitLocker/FileVault key handling.

- **[IntuneStuff Management Tool – Joery Van den Bosch](https://intunestuff.tools/)** – Windows desktop GUI for bulk Intune device operations and Entra ID group management with advanced filtering, dry‑run safety, and logging.

- **[Intune Autopilot Tool – iamwillcode](https://github.com/iamwillcode/Intune-Autopilot-Tool)** – PowerShell WPF tool to onboard devices to Intune/Autopilot via Graph API, handling encryption, profiles, user assignment, and hardware checks.

## Troubleshooting & Debugging

- **[System Information and Self-service Tool – Jannik Reinhard](https://jannikreinhard.com/2023/01/01/system-information-and-self-service-tool/)** – End‑user facing self‑service app showing device info and basic troubleshooting actions.

- **[Device Validation Tool](https://www.powerofpowershell.com/post/device-validation-with-powershell-wpf-gui-post-imaging-or-autopilot)** – WPF GUI for validating devices post‑imaging or Autopilot (hardware, configuration, readiness checks).

- **[Intune Debug Toolkit – Mattias Melkersen](https://github.com/MSEndpointMgr/IntuneDebugToolkit)** – Toolbox to troubleshoot Intune‑managed clients (Win32 re‑deploy, Autopilot/ESP, SyncML viewer, device event log helpers, and bundled community tools).

- **[Intune Device Details UI – Petri Paavola](https://github.com/petripaavola/IntuneDeviceDetailsGUI)** – GUI providing Resultant Set of Policy‑style view of Intune device and user details, app and configuration deployments.

- **[Get‑IntuneManagementExtensionDiagnostics – Petri Paavola](https://github.com/petripaavola/Get-IntuneManagementExtensionDiagnostics)** – Script that parses Intune Management Extension logs and builds an HTML timeline, plus a Log Viewer UI for detailed IME troubleshooting.

- **[Intune Device Troubleshooter – Jannik Reinhard](https://github.com/JayRHa/IntuneDeviceTroubleshooter)** – PowerShell desktop UI for fast, device‑level Intune troubleshooting combining device data, compliance, app states, and remediation actions.

- **[Get‑WindowsTroubleshootingReportCommunity – Petri Paavola](https://github.com/petripaavola/Get-WindowsTroubleshootingReportCommunity)** – Windows and Intune troubleshooting tool that unifies Event Logs and Intune log files into a single interactive HTML timeline report.

- **[Intune Log Reader for Windows – Somesh Pathak](https://github.com/pathaksomesh06/Intune-Log-Reader-for-Windows)** – Desktop app that provides real‑time analysis and monitoring of Intune Management Extension logs with dashboards, search, and export.

- **[IntuneDiag – dsregcmd Analyzer](https://www.intunediag.com/)** – Web tool that analyzes `dsregcmd /status` output, showing Entra join state, certificate validity, PRT attempts, and registration issues with actionable guidance.

- **[IntuneEndpointTools – David Just](https://github.com/djust270/IntuneEndpointTools)** – PowerShell module with functions for quickly gathering Intune client diagnostics and MDMDiagnostics reports.

- **[IntunePremier – Shepherd0619](https://github.com/Shepherd0619/IntunePremier)** – Set of open‑source tools to help helpdesk staff with daily Intune troubleshooting tasks.

## Backup & Restore

- **[Intune Backup/Restore PowerShell Module – John Seerden](https://github.com/jseerden/IntuneBackupAndRestore)** – Scripted backup and restore of Intune configurations (policies, apps, settings) across tenants.

- **[Automatic Microsoft 365 Documentation – Thomas Kurth](https://www.wpninjas.ch/2021/05/automatic-intune-documentation-evolves-to-automatic-microsoft365-documentation/)** – Automated documentation engine that generates Intune and Microsoft 365 configuration documentation.

- **[TenuVault – Ugur Koc](https://ugurlabs.com/tools/tenuvault)** – Community backup solution for Intune, offering scheduled backups, configuration drift detection, and one‑click restores across multiple tenants.

## Security

- **[BitLocker PIN – Intune – Oliver Kieselbach](https://oliverkieselbach.com/2019/08/02/how-to-enable-pre-boot-bitlocker-startup-pin-on-windows-with-intune/)** – Guide on enabling pre‑boot BitLocker startup PIN via Intune policy and deployment.

- **[DCToolbox – Daniel Chronlund](https://danielchronlund.com/2020/11/09/dctoolbox-powershell-module-for-microsoft-365-security-conditional-access-automation-and-more/)** – PowerShell module for automating Microsoft 365 security and Conditional Access operations and documentation.

- **[Windows LAPS Self‑Service Portal – Daniel Fraubaum](https://github.com/daniel-fraubaum/Intune-LAPS-SelfServicePortal)** – Azure Static Web Apps + Functions solution letting users securely retrieve the LAPS password for their own device with full audit trail.

- **[Windows Hardening – R33Dfield](https://github.com/R33Dfield/WindowsHardening)** – Hardening scripts and baselines that can be deployed via Intune for stricter Windows security.

## Automation

- **[Intune Script Viewer – Trevor Jones](https://smsagent.blog/2022/05/11/script-viewer-for-microsoft-endpoint-manager/)** – Script viewer/manager for Intune PowerShell scripts with search, filtering, and editing support.

- **[IntuneCD – Tobias Almen](https://almenscorner.io/introducing-intunecd-tool/)** – CI/CD tool to export and deploy Intune configurations from source control pipelines.

- **[Scloud's Florian – Proactive Remediation for Business](https://scloud.work/proactive-remediation-for-business/)** – Opinionated framework and examples for Intune proactive remediations in business environments.

- **[Intune Assignment Checker – Ugur Koc](https://github.com/ugurkocde/IntuneAssignmentChecker)** – PowerShell module and scripts to analyze and audit Intune assignments for users, groups, and devices, including HTML reports, unassigned policies, and empty group detection.

- **[Intune Assistant – Sander Rozemuller](https://intuneassistant.cloud/)** – Web‑based platform for assignment insights, configuration analysis, rollout assistance, and reporting across Intune tenants.

- **[Intune Toolkit – Maxime Guillemin](https://github.com/MG-Cloudflow/Intune-Toolkit)** – PowerShell‑based toolkit with UI for connecting to Graph, managing policy assignments, and handling backup/restore of assignments.

- **[Intune Registry Builder – Daniel Fraubaum](https://headsinthecloud.blog/intuneregistrybuilder/)** – Browser‑based tool to define registry changes and generate Intune‑ready detection/remediation scripts or Win32 app bundles.

- **[cmd.ms – Microsoft Cloud Command Line – Merill Fernando](https://cmd.ms)** – URL‑based “command line” and browser extension to jump straight to Azure, Entra, Intune, Defender, and other admin blades using short commands.

- **[DUDE Manager – Daniel Petri](https://skotheimsvik.no/toolbox-rundown/#dude-manager)** – GUI to deploy and monitor the DUDE automation engine that syncs Intune device groups with Entra user groups.

## Miscellaneous

- **[IntuneWin Build and Extract Tool – Damien Van Robaeys](https://www.systanddeploy.com/2023/05/intunewin-build-and-extract-tool-to.html)** – GUI tool to build and extract .intunewin packages for Intune Win32 apps.

- **[Intune Drive Mapping Generator – Nicola Suter](https://intunedrivemapping.azurewebsites.net/)** – Web generator for Intune drive‑mapping policies targeting users and devices.

- **[Enhanced Inventory for Intune – Jan Ketil Skanke](https://msendpointmgr.com/2022/01/17/securing-intune-enhanced-inventory-with-azure-function/)** – Azure Function‑based solution that enriches Intune inventory data for reporting and security.

- **[Intune Log Reader for Windows App Health Check Remediation – Niall Brady & Paul Winstanley](https://github.com/niallbrady/WindowsAppHealthCheckLogReader)** – Intune remediation solution that copies Windows app health check logs into IntuneManagementExtension logs for easier remote diagnostics.

- **[Intune Premier Toolbox – Simon Skotheimsvik’s Toolbox Rundown](https://skotheimsvik.no/toolbox-rundown/)** – Curated list of endpoint‑management tools including Intune Assignment Checker, Intune Debug Toolkit, Intune Diff, and more, useful as a discovery hub.

---

## License

[![Creative Commons](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)
This list is licensed under a Creative Commons Attribution 4.0 International License.
