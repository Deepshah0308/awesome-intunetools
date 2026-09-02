# Awesome Intune Tools

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

A curated directory of community tools, scripts and utilities for Microsoft Intune administrators.

**Browse it as a searchable website: [deepshah0308.github.io/awesome-intunetools](https://deepshah0308.github.io/awesome-intunetools/)**

122 tools across 14 categories. Contributions welcome - see [Contributing](#contributing).

## Contents

- [How to use this list](#how-to-use-this-list)
- [Contributing](#contributing)
- [Device Management](#device-management) (11)
- [Troubleshooting & Debugging](#troubleshooting-debugging) (14)
- [App Packaging & Deployment](#app-packaging-deployment) (19)
- [Autopilot & Provisioning](#autopilot-provisioning) (7)
- [Baselines & Configuration as Code](#baselines-configuration-as-code) (6)
- [macOS & Apple](#macos-apple) (15)
- [Android & Cross-platform](#android-cross-platform) (3)
- [Graph API & PowerShell](#graph-api-powershell) (8)
- [Reporting & Analytics](#reporting-analytics) (8)
- [Remediations & Scripts](#remediations-scripts) (9)
- [Backup, Restore & Documentation](#backup-restore-documentation) (4)
- [Security & Hardening](#security-hardening) (5)
- [Automation & Assignments](#automation-assignments) (7)
- [Utilities & Discovery](#utilities-discovery) (6)

## How to use this list

This is a directory for Intune consultants, MSPs, and in-house admins who want a working toolbox rather than more documentation. Pick two or three tools per use case, test them in a lab tenant, then standardise them into your own baseline toolkit.

**Auditing a tenant you have just inherited**  
Start with Intune Management or Intune Inspector for a policy overview, Intune Assignment Checker for assignment hygiene, and IntuneCD or Microsoft365DSC to get the configuration into source control where you can diff it.

**Equipping a helpdesk**  
Intune Debug Toolkit and Intune Device Troubleshooter cover day-to-day device work. CMTraceOpen and Get-IntuneManagementExtensionDiagnostics turn IME logs into something readable. IntuneDiag handles Entra join and PRT problems.

**Building an app packaging pipeline**  
WinTuner or IntuneGet for Winget-sourced apps, PSAppDeployToolkit for anything needing user interaction, and Intune App Factory when you want the whole thing running unattended in a pipeline.

**Standing up a new tenant**  
OpenIntuneBaseline gives you a defensible Windows starting point. IntuneHydrationKit fills a lab quickly. Add the platform baselines for macOS, iOS, and Android as needed.

## Contributing

Contributions from the Intune community are very welcome.

### What belongs here

- Community-built tools, scripts, modules, or web apps that help manage, troubleshoot, secure, or automate Intune.
- Free or primarily community and open-source projects. Commercial SaaS with aggressive marketing is out of scope.
- Tools that are realistically usable: tested on modern tenants and documented well enough for someone else to adopt.

### How to contribute

The website and this README are both generated from [`data/tools.json`](data/tools.json), so that is the only file you need to edit. Do not edit `README.md` or anything in `docs/` by hand - your changes will be overwritten on the next build.

1. Fork the repository and create a branch, for example `add-my-tool`.
2. Add an entry to the `tools` array in `data/tools.json`:

```json
{
  "name": "Tool Name",
  "author": "Author or handle",
  "url": "https://github.com/owner/repo",
  "category": "troubleshooting",
  "kind": "repo",
  "desc": "One sentence on the problem it solves and why it is useful."
}
```

`category` must be one of the ids listed at the top of `data/tools.json`. `kind` is `repo` for source repositories, `web` for hosted tools, or `guide` for a blog post or written walkthrough.

3. Open a pull request explaining what you are adding. If it overlaps with something already listed, say what is different about it.

### Guidelines

- Only suggest tools you have used or can reasonably recommend.
- Link to the canonical repository or project page, not a marketing landing page.
- Describe practical value in plain language. No vendor copy.
- Every link in this list is automatically checked. Entries whose links break will be fixed or removed.

## Device Management

Consoles, bulk operations, and lifecycle tooling for the devices in your tenant.

- **[Intune Maps - Shehan Perera](https://intunemaps.com/)** - Visual map of Intune blades and documentation to speed up portal navigation.
- **[Rockn Roll Tool - Nicklas Ahlberg](https://www.rockenroll.tech/)** - Management tools for Intune environments covering policies, apps, Autopilot, and helpdesk utilities.
- **[Rock My Printers - Nicklas Ahlberg](https://www.rockenroll.tech/2023/03/14/rock-my-printers/)** - Simplifies printer management across Intune-managed devices.
- **[Intune Management - Mikael Karlsson](https://github.com/Micke-K/IntuneManagement)** - PowerShell and WPF GUI to copy, export, import, delete, document, and compare Intune policies and profiles, with ADMX ingestion and cross-tenant migration.
- **[Device Offboarding Manager - Ugur Koc](https://github.com/ugurkocde/DeviceOffboardingManager)** - PowerShell GUI for bulk offboarding devices from Intune, Autopilot, and Entra ID with dashboards, stale device tracking, and BitLocker key handling.
- **[IntuneStuff Management Tool - Joery Van den Bosch](https://intunestuff.tools/)** - Windows desktop GUI for bulk Intune device operations and Entra ID group management with advanced filtering, dry-run safety, and logging.
- **[Intune Autopilot Tool - iamwillcode](https://github.com/iamwillcode/Intune-Autopilot-Tool)** - PowerShell WPF tool to onboard devices to Intune and Autopilot via Graph API, handling encryption, profiles, user assignment, and hardware checks.
- **[InSight - MrOlof](https://github.com/MrOlof/InSight)** - PowerShell GUI for Intune administration including device ownership analysis and tenant overview.
- **[Intune Device Classification - MrWyss-MSFT](https://github.com/MrWyss-MSFT/IntuneDeviceClassification)** - Classifies and tags devices so dynamic Entra ID groups can be built from device characteristics rather than manual membership.
- **[Intune Help Desk - backuploki](https://github.com/backuploki/Intune-Help-Desk)** - Interactive CLI dashboard for helpdesk teams to query Intune devices and view compliance without opening the portal.
- **[Intune Inspector - fscorrupt](https://github.com/fscorrupt/IntuneInspector)** - WPF GUI that caches every policy type locally and full-text searches across them, including decoded PowerShell script content.

## Troubleshooting & Debugging

Log readers, diagnostics collectors, and device-level investigation tools.

- **[System Information and Self-service Tool - Jannik Reinhard](https://jannikreinhard.com/2023/01/01/system-information-and-self-service-tool/)** - End-user facing self-service app showing device info and basic troubleshooting actions.
- **[Intune Debug Toolkit - MSEndpointMgr](https://github.com/MSEndpointMgr/IntuneDebugToolkit)** - Toolbox for troubleshooting Intune-managed clients with Win32 re-deploy, Autopilot and ESP inspection, a SyncML viewer, and event log helpers.
- **[Intune Device Details UI - Petri Paavola](https://github.com/petripaavola/IntuneDeviceDetailsGUI)** - GUI providing a Resultant Set of Policy style view of Intune device and user details, app and configuration deployments.
- **[Get-IntuneManagementExtensionDiagnostics - Petri Paavola](https://github.com/petripaavola/Get-IntuneManagementExtensionDiagnostics)** - Parses Intune Management Extension logs into an HTML timeline, with a log viewer UI for detailed IME troubleshooting.
- **[Intune Device Troubleshooter - Jannik Reinhard](https://github.com/JayRHa/IntuneDeviceTroubleshooter)** - PowerShell desktop UI for device-level troubleshooting combining device data, compliance, app states, and remediation actions.
- **[Get-WindowsTroubleshootingReportCommunity - Petri Paavola](https://github.com/petripaavola/Get-WindowsTroubleshootingReportCommunity)** - Unifies Windows Event Logs and Intune log files into a single interactive HTML timeline report.
- **[Intune Log Reader for Windows - Somesh Pathak](https://github.com/pathaksomesh06/Intune-Log-Reader-for-Windows)** - Desktop app providing real-time analysis of Intune Management Extension logs with dashboards, search, and export.
- **[IntuneDiag - IntuneDiag](https://www.intunediag.com/)** - Browser tool that analyzes dsregcmd /status output, showing Entra join state, certificate validity, PRT attempts, and registration issues.
- **[IntuneEndpointTools - David Just](https://github.com/djust270/IntuneEndpointTools)** - PowerShell module for quickly gathering Intune client diagnostics and MDMDiagnostics reports.
- **[IntunePremier - Shepherd0619](https://github.com/Shepherd0619/IntunePremier)** - Open-source tools aimed at helpdesk staff handling daily Intune troubleshooting tasks.
- **[CMTraceOpen - Adam Gell](https://github.com/adamgell/cmtraceopen)** - Free, open-source CMTrace replacement for reading ConfigMgr, Intune IME, and Autopilot ESP log files on modern Windows.
- **[Intune One Data Collector - markstan](https://github.com/markstan/IntuneOneDataCollector)** - Automated collector that gathers the full diagnostic data set Microsoft support asks for when opening an Intune case.
- **[IntuneWUTools - markstan](https://github.com/markstan/IntuneWUTools)** - Tools for troubleshooting Windows Update behaviour on Intune-managed clients.
- **[MHimken Toolbox - MHimken](https://github.com/MHimken/toolbox)** - Collection of endpoint management scripts covering Autopilot diagnostics, ESP inspection, and client-side troubleshooting.

## App Packaging & Deployment

Win32 packaging, Winget pipelines, and app delivery automation.

- **[Microsoft Win32 Content Prep Tool - Microsoft](https://github.com/microsoft/Microsoft-Win32-Content-Prep-Tool)** - The official utility that wraps Win32 installers into the .intunewin format required for upload.
- **[PSAppDeployToolkit - PSAppDeployToolkit](https://github.com/PSAppDeployToolkit/PSAppDeployToolkit)** - Framework for building consistent, user-aware application installs with deferral prompts, process handling, and logging.
- **[WinTuner - Stephan van Rooij](https://github.com/svrooij/WinTuner)** - Packages any Winget app straight into Intune from the command line or a PowerShell module, including icons and detection rules.
- **[IntuneGet - Ugur Koc](https://github.com/ugurkocde/IntuneGet)** - Skips the manual packaging workflow and deploys Winget apps to Intune in a few clicks.
- **[Winget-Install - Romanitho](https://github.com/Romanitho/Winget-Install)** - PowerShell scripts for installing and updating Winget packages in system context from Intune or ConfigMgr.
- **[WingetIntunePackager - Romanitho](https://github.com/Romanitho/WingetIntunePackager)** - GUI packager that turns Winget packages into ready-to-upload Intune Win32 apps.
- **[WinGet-Wrapper - Soren Lundt](https://github.com/SorenLundt/WinGet-Wrapper)** - Bulk-imports Winget packages into Intune including all package metadata, detection, and requirement rules.
- **[IntuneWin32Deployer - Florian Salzmann](https://github.com/FlorianSLZ/IntuneWin32Deployer)** - Creates and deploys Winget and Chocolatey apps to Intune as Win32 packages in one command.
- **[Intune App Factory - MSEndpointMgr](https://github.com/MSEndpointMgr/IntuneAppFactory)** - Azure DevOps pipeline that automates Win32 application packaging and publishing to Intune end to end.
- **[IntuneWin32AppPackager - MSEndpointMgr](https://github.com/MSEndpointMgr/IntuneWin32AppPackager)** - Framework that packages, creates, and simultaneously documents Win32 applications for Intune.
- **[Package Factory - Aaron Parker](https://github.com/aaronparker/packagefactory)** - Packaging factory for Intune built on Evergreen and VcRedist, keeping app packages continuously current.
- **[IntunePrepTool - Rink Turksma](https://github.com/rink-turksma/IntunePrepTool)** - GUI front end for the Win32 Content Prep Tool that speeds up repetitive packaging work.
- **[Intune App Deploy - Ben Reader](https://github.com/tabs-not-spaces/Intune-App-Deploy)** - Reliable path to package Win32 applications and deploy them to Intune from any source, including CI pipelines.
- **[IntuneAppCreator - Jannik Reinhard](https://github.com/JayRHa/IntuneAppCreator)** - Automates creation, packaging, and deployment preparation of Intune Win32 apps.
- **[Win32 Toolkit - Maxime Guillemin](https://github.com/MG-Cloudflow/win32-toolkit)** - End-to-end Win32 packaging that accepts a Winget package or your own installer and produces a deployable app.
- **[WrapTune - thefinder808](https://github.com/thefinder808/WrapTune)** - Friendly GUI for IntuneWinAppUtil.exe for admins who would rather not memorise its arguments.
- **[Deployment Editor - tugich](https://github.com/tugich/DeploymentEditor)** - Click-together sequence builder for PSAppDeployToolkit packages, lowering the scripting barrier for packagers.
- **[IntuneWin Build and Extract Tool - Damien Van Robaeys](https://www.systanddeploy.com/2023/05/intunewin-build-and-extract-tool-to.html)** - GUI tool to build and, crucially, extract .intunewin packages when you need to inspect what shipped.
- **[IntuneAppAssigner - Nick Benton](https://github.com/ennnbeee/IntuneAppAssigner)** - Bulk updates or replaces assignments across many Intune applications at once.

## Autopilot & Provisioning

Hardware hashes, enrollment, imaging media, and provisioning workflows.

- **[Intune.USB.Creator - Ben Reader](https://github.com/tabs-not-spaces/Intune.USB.Creator)** - Builds a bootable WinPE USB used to provision devices for Autopilot enrollment.
- **[Intune.HV.Tools - Ben Reader](https://github.com/tabs-not-spaces/Intune.HV.Tools)** - Spins up Intune-managed Hyper-V virtual machines for testing enrollment and policy without touching real hardware.
- **[Foundry - foundry-osd](https://github.com/foundry-osd/foundry)** - Modern open-source Windows deployment solution with a graphical interface for creating bootable provisioning media.
- **[WinAutopilotImport - tugich](https://github.com/tugich/WinAutopilotImport)** - Simple GUI for registering a Windows device with Autopilot during OOBE.
- **[Get-WindowsAutopilotImportCommunity - markorr321](https://github.com/markorr321/Get-WindowsAutopilotImportCommunity)** - Registers devices with Autopilot from a real GUI instead of a console, supporting hardware hash collection and Group Tag selection.
- **[Autopilot Cleanup - markorr321](https://github.com/markorr321/Autopilot-Cleanup)** - Interactive tool for bulk device cleanup across Autopilot, Intune, and Entra ID in a single pass.
- **[IntuneMigrationV2 - stevecapacity](https://github.com/stevecapacity/IntuneMigrationV2)** - Tenant-to-tenant device migration supporting in-place migration as well as hardware hash re-import.

## Baselines & Configuration as Code

Ready-to-import baselines and declarative tenant configuration.

- **[OpenIntuneBaseline - SkipToTheEndpoint](https://github.com/SkipToTheEndpoint/OpenIntuneBaseline)** - Community-driven Intune baseline covering Windows configuration, security, and update policies as importable JSON.
- **[Microsoft365DSC - Microsoft365DSC](https://github.com/microsoft/Microsoft365DSC)** - Manages the entire Microsoft 365 configuration, Intune included, as declarative PowerShell DSC code with drift reporting.
- **[IntuneHydrationKit - jorgeasaurus](https://github.com/jorgeasaurus/IntuneHydrationKit)** - Imports a set of starter configurations into a fresh tenant so a lab or new deployment is usable quickly.
- **[IntuneBaselines - Wolkenman](https://github.com/IntuneAdmin/IntuneBaselines)** - Intune baseline profiles in JSON format for standing up a modern workplace configuration.
- **[IntuneLinuxBaseline - glueckkanja](https://github.com/glueckkanja/IntuneLinuxBaseline)** - Baseline configuration for managing Linux endpoints through Intune.
- **[Intune Preflight - kevinmalinoski](https://github.com/kevinmalinoski/intune-preflight)** - Simulates an Intune endpoint and previews the merged policy baseline a device would actually receive, read-only.

## macOS & Apple

Tooling for Mac, iOS, and iPadOS fleets managed through Intune.

- **[Shell Intune Samples - Microsoft](https://github.com/microsoft/shell-intune-samples)** - Microsoft's reference shell scripts for macOS and Linux Intune admins, covering app installs, custom attributes, and detection.
- **[intune-my-macs - Microsoft](https://github.com/microsoft/intune-my-macs)** - Automation project that configures an Intune environment for macOS management quickly and repeatably.
- **[Intune Mac Admins - Ugur Koc](https://github.com/ugurkocde/intunemacadmins)** - Community platform with detailed guides, scripts, and best practices for managing macOS devices via Intune.
- **[IntuneBrew - Ugur Koc](https://github.com/ugurkocde/IntuneBrew)** - Simplifies uploading and managing macOS applications in Intune, drawing on a large catalog of maintained app definitions.
- **[MISA (macOS Intune Support Assistant) - Somesh Pathak](https://github.com/pathaksomesh06/MISA)** - Support assistant for macOS endpoints that surfaces enrollment and policy state for helpdesk staff.
- **[IntuneLogWatch - Gil Burns](https://github.com/gilburns/IntuneLogWatch)** - macOS application that analyzes Intune agent logs and delivers human-readable insight instead of raw text.
- **[Third Party Patcher - Gil Burns](https://github.com/gilburns/Third-Party-Patcher)** - MDM-agnostic, MDM-managed daemon that handles third-party patching and software distribution on macOS.
- **[macOS MDM Profiles - homotechsual](https://github.com/homotechsual/macOS-MDM-Profiles)** - Ready-made MDM profiles for configuring permissions and services on macOS devices through Intune.
- **[Intune Goodies - Oktay Sari](https://github.com/oktay-sari/Intune-Goodies)** - Collection of scripts and tools covering macOS and cross-platform Intune management tasks.
- **[JUMP-IN - Somesh Pathak](https://github.com/pathaksomesh06/JUMP-IN)** - macOS application that simplifies migration between MDM solutions, aimed at moving Macs into Intune.
- **[WrapTune for macOS - thefinder808](https://github.com/thefinder808/WrapTune-MacOS)** - Builds Intune .intunewin packages from a Mac, so packagers are not forced onto a Windows box.
- **[macOS Hardening - R33Dfield](https://github.com/R33Dfield/MacOSHardening)** - Intune configuration files for hardening macOS against a documented security standard.
- **[iOS Hardening - R33Dfield](https://github.com/R33Dfield/iOSHardening)** - Intune configuration files for hardening iOS and iPadOS devices.
- **[iOS/iPadOS Intune Baseline - UniFy-Endpoint](https://github.com/UniFy-Endpoint/iOS-iPadOS-Intune-Baseline)** - CIS-aligned baseline for iOS and iPadOS with importable JSON policies and deployment guides.
- **[Intune App SDK for iOS - Microsoft](https://github.com/microsoftconnect/ms-intune-app-sdk-ios)** - Official SDK enabling app protection and data protection features inside in-house iOS applications.

## Android & Cross-platform

Android Enterprise, Linux, and multi-platform management.

- **[Android Enterprise Baseline - UniFy-Endpoint](https://github.com/UniFy-Endpoint/Android-Enterprise-Baseline)** - Android Enterprise baseline policies and deployment guides for Intune.
- **[Intune Android QR Wizard - brommet87](https://github.com/brommet87/Intune-Android-QR-Wizard)** - Generates Wi-Fi QR codes to simplify network configuration during Android Enterprise enrollment.
- **[Intune Apps - Aaron Parker](https://github.com/aaronparker/intune-apps)** - Definitions for managing Windows, macOS, Android, and iOS applications in Intune from one place.

## Graph API & PowerShell

SDKs, sample libraries, and scripting interfaces for the Intune Graph API.

- **[PowerShell Intune Samples - Microsoft Graph](https://github.com/microsoftgraph/powershell-intune-samples)** - Microsoft's long-standing sample library showing how to reach every Intune Graph resource from PowerShell.
- **[Microsoft Graph PowerShell Intune Samples - Microsoft](https://github.com/microsoft/mggraph-intune-samples)** - Current sample set built for the Microsoft Graph PowerShell SDK, replacing the older Intune-specific module.
- **[Intune PowerShell SDK - Microsoft](https://github.com/microsoft/Intune-PowerShell-SDK)** - Native PowerShell cmdlets wrapping the Intune Graph API for IT Pro scenario automation.
- **[GraphXray - Merill Fernando](https://github.com/merill/graphxray)** - Watches actions you take in the Entra or Intune portal and shows the equivalent Graph calls and PowerShell to script them.
- **[InTUI - jorgeasaurus](https://github.com/jorgeasaurus/InTUI)** - Terminal user interface for Intune management, driving Graph from a keyboard-first console.
- **[IntuneQL - Ugur Koc](https://github.com/ugurkocde/IntuneQL)** - Keyboard-driven terminal workspace for querying the Graph API and browsing Intune resources visually.
- **[MgGraphCommunity - Ugur Koc](https://github.com/ugurkocde/MgGraphCommunity)** - Community drop-in alternative to Connect-MgGraph in pure PowerShell, avoiding WAM and MSAL dependencies.
- **[Aaron Parker's Intune Scripts - Aaron Parker](https://github.com/aaronparker/intune)** - Broad, well-maintained collection of scripts and tooling for use with Intune.

## Reporting & Analytics

Dashboards, compliance exports, and executive-facing reporting.

- **[MSEndpointMgr Reporting - MSEndpointMgr](https://github.com/MSEndpointMgr/Reporting)** - Intune reporting built on Azure Monitor, Log Analytics, and Azure Workbooks.
- **[Intune.Reporting - Ben Reader](https://github.com/tabs-not-spaces/Intune.Reporting)** - Generates presentable Intune reports from PowerShell for stakeholders who will not log into the portal.
- **[Intune Reporting - Damien Van Robaeys](https://github.com/damienvanrobaeys/Intune-Reporting)** - Reporting scripts covering device, app, and policy status across the tenant.
- **[Power BI Dashboards for Intune - Jannik Reinhard](https://github.com/JayRHa/PowerBIDashboards)** - Power BI templates for Endpoint Analytics and device management reporting.
- **[Intune Patching & OS Compliance Dashboard - greebo-labs](https://github.com/greebo-labs/intune-patching-os-compliance-dashboard)** - Browser-based dashboard for patch compliance, Windows OS lifecycle tracking, and executive reporting.
- **[M365-Assess - Galvnyz](https://github.com/Galvnyz/M365-Assess)** - Runs hundreds of automated checks across multiple compliance frameworks and produces an interactive HTML report locally.
- **[IntuneComplianceReport - DanStutz](https://github.com/DanStutz/IntuneComplianceReport)** - Exports device compliance to a wide CSV via Graph, one row per device with each policy as a column.
- **[Enhanced Inventory for Intune - Jan Ketil Skanke](https://msendpointmgr.com/2022/01/17/securing-intune-enhanced-inventory-with-azure-function/)** - Azure Function solution that enriches Intune inventory data for reporting and security use.

## Remediations & Scripts

Detection and remediation script libraries plus authoring tools.

- **[Endpoint Analytics Remediation Scripts - Jannik Reinhard](https://github.com/JayRHa/EndpointAnalyticsRemediationScripts)** - Large library of ready-to-use proactive remediation detection and remediation script pairs.
- **[Intune Remediation Scripts - Damien Van Robaeys](https://github.com/damienvanrobaeys/Intune-Remediation-scripts)** - Practical remediation scripts covering common Windows configuration and repair scenarios.
- **[Remediations - Aaron Parker](https://github.com/aaronparker/remediations)** - Curated remediation scripts written for Intune with an emphasis on idempotence and clean detection logic.
- **[RemediationCreator - Jannik Reinhard](https://github.com/JayRHa/RemediationCreator)** - Creates and manages proactive remediation script packages rather than hand-uploading each pair.
- **[IROD (Intune Remediations On-Demand) - markorr321](https://github.com/markorr321/IROD)** - Runs remediation scripts on demand from a WPF GUI backed by the Graph API, instead of waiting for schedules.
- **[Intune Registry Management - Martin Bengtsson](https://github.com/imabdk/Intune-Registry-Management)** - Single reusable script for managing Windows registry values through Intune remediations.
- **[Endpoint Manager Scripts - Richard Hicks](https://github.com/richardhicks/endpointmanager)** - Proactive remediation scripts with a focus on networking, VPN, and Always On VPN scenarios.
- **[Proactive Remediation for Business - Florian Salzmann](https://scloud.work/proactive-remediation-for-business/)** - Opinionated framework and worked examples for running proactive remediations in production.
- **[Windows App Health Check Log Reader - Niall Brady & Paul Winstanley](https://www.niallbrady.com/2025/10/04/using-remediation-scripts-in-intune-to-grab-windows-365-health-check-logs/)** - Remediation that copies Windows app health check logs into IME logs for easier remote diagnostics.

## Backup, Restore & Documentation

Tenant backup, drift detection, migration, and auto-generated documentation.

- **[Intune Backup and Restore - John Seerden](https://github.com/jseerden/IntuneBackupAndRestore)** - PowerShell module querying Graph for cross-tenant backup and restore of Intune configuration.
- **[Automatic Microsoft 365 Documentation - Thomas Kurth](https://github.com/ThomasKur/M365Documentation)** - Automated engine generating readable Intune and Microsoft 365 configuration documentation.
- **[TenuVault - Ugur Koc](https://ugurlabs.com/tools/tenuvault)** - Backup solution offering scheduled backups, configuration drift detection, and one-click restores across tenants.
- **[TrustM365 - AntoPorter](https://github.com/AntoPorter/TrustM365)** - Self-hosted configuration drift monitoring that baselines a tenant and detects changes at the property level.

## Security & Hardening

Hardening baselines, LAPS, BitLocker, and security posture assessment.

- **[Pre-boot BitLocker Startup PIN - Oliver Kieselbach](https://oliverkieselbach.com/2019/08/02/how-to-enable-pre-boot-bitlocker-startup-pin-on-windows-with-intune/)** - Reference walkthrough for enabling pre-boot BitLocker startup PIN through Intune policy.
- **[DCToolbox - Daniel Chronlund](https://danielchronlund.com/2020/11/09/dctoolbox-powershell-module-for-microsoft-365-security-conditional-access-automation-and-more/)** - PowerShell module automating Microsoft 365 security and Conditional Access operations and documentation.
- **[Windows LAPS Self-Service Portal - Daniel Fraubaum](https://github.com/daniel-fraubaum/laps-self-service-portal)** - Azure Static Web Apps and Functions solution letting users retrieve the LAPS password for their own device with a full audit trail.
- **[Windows Hardening - R33Dfield](https://github.com/R33Dfield/WindowsHardening)** - Hardening scripts and baselines deployable through Intune for stricter Windows security posture.
- **[Harden Windows Security - HotCakeX](https://github.com/HotCakeX/Harden-Windows-Security)** - Extensively documented hardening module using officially supported Microsoft methods, with policies deployable via Intune.

## Automation & Assignments

CI/CD, assignment auditing, and workflow automation.

- **[Intune Script Viewer - Trevor Jones](https://smsagent.blog/2022/05/11/script-viewer-for-microsoft-endpoint-manager/)** - Script viewer and manager for Intune PowerShell scripts with search, filtering, and editing.
- **[IntuneCD - Tobias Almen](https://github.com/almenscorner/IntuneCD)** - Backs up, documents, and deploys Intune configuration from source control, making tenant config a reviewable pipeline.
- **[Intune Assignment Checker - Ugur Koc](https://github.com/ugurkocde/IntuneAssignmentChecker)** - Audits Intune assignments for users, groups, and devices, surfacing unassigned policies and empty groups in HTML reports.
- **[Intune Assistant - Sander Rozemuller](https://intuneassistant.cloud/)** - Web platform for assignment insight, configuration analysis, rollout assistance, and reporting across tenants.
- **[Intune Toolkit - Maxime Guillemin](https://github.com/MG-Cloudflow/Intune-Toolkit)** - PowerShell toolkit with a UI for managing policy assignments and backing up or restoring them.
- **[Feature Update Controller - MSEndpointMgr](https://github.com/MSEndpointMgr/FeatureUpdateController)** - Centralises control of Windows feature update rollout for Intune-managed devices instead of managing rings by hand.
- **[DUDE Manager - Simon Skotheimsvik](https://skotheimsvik.no/toolbox-rundown/#dude-manager)** - GUI to deploy and monitor the DUDE automation engine that syncs Intune device groups with Entra user groups.

## Utilities & Discovery

Generators, navigation helpers, and directories of further tooling.

- **[Intune Registry Builder - Daniel Fraubaum](https://headsinthecloud.blog/intuneregistrybuilder/)** - Browser tool to define registry changes and generate Intune-ready detection and remediation scripts or Win32 bundles.
- **[cmd.ms - Merill Fernando](https://cmd.ms)** - URL-based command line and browser extension that jumps straight to Azure, Entra, Intune, and Defender admin blades.
- **[Intune Drive Mapping Generator - Nicola Suter](https://intunedrivemapping.azurewebsites.net/)** - Web generator for drive-mapping policies targeting users and devices without hand-writing XML.
- **[Toolbox Rundown - Simon Skotheimsvik](https://skotheimsvik.no/toolbox-rundown/)** - Curated rundown of endpoint management tools, useful as a second discovery hub alongside this list.
- **[Intune Wall of Tools - IntuneQLinks](https://intuneqlinks.net/wall-of-tools)** - Community hub cataloguing Intune settings references, community content, and a broad tool directory.
- **[Awesome Intune - awesomeintune.com](https://www.awesomeintune.com/)** - Large searchable directory of free Intune tools and scripts with source-code risk scanning on listed projects.

---

## License

[![Creative Commons](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)  
This list is licensed under a Creative Commons Attribution 4.0 International License. The tools themselves are licensed by their respective authors.
