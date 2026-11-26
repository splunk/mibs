#
# PySNMP MIB module CISCO-L2L3-INTERFACE-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-L2L3-INTERFACE-CONFIG-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:44 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, TimeTicks, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoL2L3IfConfigMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 151))
ciscoL2L3IfConfigMIB.setRevisions(('2000-05-10 19:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoL2L3IfConfigMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoL2L3IfConfigMIB.setLastUpdated('200005101900Z')
if mibBuilder.loadTexts: ciscoL2L3IfConfigMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoL2L3IfConfigMIB.setContactInfo('Cisco Systems\n        Customer Service\n\n        Postal: 170 W Tasman Drive\n                San Jose, CA  95134\n                USA\n\n        Tel: +1 800 553-NETS\n\n        E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoL2L3IfConfigMIB.setDescription('Interface switchport mode configuration management MIB.\n\n        This MIB is used to monitor and control \n        configuration of interface switchport and routed mode.')
ciscoL2L3IfConfigMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 151, 1))
cL2L3IfConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 151, 1, 1))
class CL2L3InterfaceMode(TextualConvention, Integer32):
    description = "The operational mode of the interface.\n\n        For administrative and operational states, valid values are: \n        routed(1), switchport(2).\n        \n        routed(1): Routed mode interfaces direct traffic using \n        layer 3 protocols.\n\n        switchport(2):  Switchport-mode interfaces direct traffic using \n        layer 2 protocols.  A switchport-mode interface can be in\n        access mode, or trunk mode, or multi-mode.\n\n        Switchport interface operating mode can be configured manually,\n        or negotiated by Dynamic Trunking Protocol (DTP) or Dynamic \n        Inter-Switch Link (DISL).\n\n        Access-mode interfaces carry one VLAN's traffic.  Access-mode\n        interface parameters are configured in CISCO-VLAN-MEMBERSHIP-MIB.\n\n        Trunk-mode interfaces carry one or more VLANs.  VLAN-related \n        trunk-mode interface parameters are configured in CISCO-VTP-MIB.\n\n        Multi-mode interfaces carry one VLAN to each alias of a \n        single connected end-station.  VLAN-related multi-mode \n        interface parameters are configured in CISCO-VTP-MIB.\n        "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("routed", 1), ("switchport", 2))

cL2L3IfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 151, 1, 1, 1), )
if mibBuilder.loadTexts: cL2L3IfTable.setStatus('current')
if mibBuilder.loadTexts: cL2L3IfTable.setDescription('The table shows the administratively requested and\n        actual operating configuration for switchport interfaces.')
cL2L3IfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 151, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cL2L3IfEntry.setStatus('current')
if mibBuilder.loadTexts: cL2L3IfEntry.setDescription('An entry represents the configuration and operation of a\n        switchport interface.\n\n        Entries are created and deleted automatically in tandem \n        with the corresponding ifEntries.')
cL2L3IfModeAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 151, 1, 1, 1, 1, 1), CL2L3InterfaceMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cL2L3IfModeAdmin.setStatus('current')
if mibBuilder.loadTexts: cL2L3IfModeAdmin.setDescription('The administratively desired interface mode.')
cL2L3IfModeOper = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 151, 1, 1, 1, 1, 2), CL2L3InterfaceMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cL2L3IfModeOper.setStatus('current')
if mibBuilder.loadTexts: cL2L3IfModeOper.setDescription('The operational interface mode.')
ciscoL2L3IfConfigMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 151, 3))
ciscoL2L3IfConfigMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 151, 3, 1))
ciscoL2L3IfConfigMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 151, 3, 2))
ciscoL2L3IfConfigMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 151, 3, 1, 1)).setObjects(("CISCO-L2L3-INTERFACE-CONFIG-MIB", "ciscoL2L3IfConfigMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2L3IfConfigMIBCompliance = ciscoL2L3IfConfigMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoL2L3IfConfigMIBCompliance.setDescription('The compliance statement for entities which implement\n         the Cisco L2L3 Interface Configuration Management MIB')
ciscoL2L3IfConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 151, 3, 2, 1)).setObjects(("CISCO-L2L3-INTERFACE-CONFIG-MIB", "cL2L3IfModeAdmin"), ("CISCO-L2L3-INTERFACE-CONFIG-MIB", "cL2L3IfModeOper"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2L3IfConfigMIBGroup = ciscoL2L3IfConfigMIBGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoL2L3IfConfigMIBGroup.setDescription('Interface L2 & L3 mode objects')
mibBuilder.exportSymbols("CISCO-L2L3-INTERFACE-CONFIG-MIB", CL2L3InterfaceMode=CL2L3InterfaceMode, cL2L3IfConfig=cL2L3IfConfig, cL2L3IfModeOper=cL2L3IfModeOper, cL2L3IfTable=cL2L3IfTable, ciscoL2L3IfConfigMIBGroups=ciscoL2L3IfConfigMIBGroups, ciscoL2L3IfConfigMIBCompliances=ciscoL2L3IfConfigMIBCompliances, ciscoL2L3IfConfigMIBObjects=ciscoL2L3IfConfigMIBObjects, cL2L3IfModeAdmin=cL2L3IfModeAdmin, ciscoL2L3IfConfigMIBGroup=ciscoL2L3IfConfigMIBGroup, ciscoL2L3IfConfigMIB=ciscoL2L3IfConfigMIB, PYSNMP_MODULE_ID=ciscoL2L3IfConfigMIB, cL2L3IfEntry=cL2L3IfEntry, ciscoL2L3IfConfigMIBConformance=ciscoL2L3IfConfigMIBConformance, ciscoL2L3IfConfigMIBCompliance=ciscoL2L3IfConfigMIBCompliance)
