#
# PySNMP MIB module CISCO-DDP-IAPP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DDP-IAPP-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoPort, = mibBuilder.importSymbols("CISCO-TC", "CiscoPort")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
TextualConvention, DisplayString, TruthValue, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue", "MacAddress")
ciscoDdpIappMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 277))
ciscoDdpIappMIB.setRevisions(('2002-07-31 00:00', '2002-07-17 00:00', '2002-03-19 00:00', '2002-03-07 00:00', '2001-09-28 00:00',))
if mibBuilder.loadTexts: ciscoDdpIappMIB.setLastUpdated('200207310000Z')
if mibBuilder.loadTexts: ciscoDdpIappMIB.setOrganization('Cisco System Inc.')
ciscoDdpIappMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 277, 0))
ciscoDdpIappMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 277, 1))
ciscoDdpIappMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 277, 2))
cDdpIappGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 277, 1, 1))
cDdpIappRogueApInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 277, 1, 2))
cDdpIappMcastIpAddrType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 277, 1, 1, 1), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cDdpIappMcastIpAddrType.setStatus('current')
cDdpIappMcastIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 277, 1, 1, 2), InetAddress().clone(hexValue="e0000128")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cDdpIappMcastIpAddr.setStatus('current')
cDdpIappPort = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 277, 1, 1, 3), CiscoPort().clone(2887)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDdpIappPort.setStatus('current')
cDdpIappRogueApNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 277, 1, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cDdpIappRogueApNotifEnabled.setStatus('current')
cDdpIappLastRogueApMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 277, 1, 2, 1), MacAddress().clone(hexValue="000000000000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDdpIappLastRogueApMacAddr.setStatus('current')
cDdpIappLastRogueApNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 277, 0, 1)).setObjects(("CISCO-DDP-IAPP-MIB", "cDdpIappLastRogueApMacAddr"))
if mibBuilder.loadTexts: cDdpIappLastRogueApNotif.setStatus('current')
ciscoDdpIappMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 277, 2, 1))
ciscoDdpIappMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 277, 2, 2))
ciscoDdpIappCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 277, 2, 1, 1)).setObjects(("CISCO-DDP-IAPP-MIB", "ciscoDdpIappConfigGroup"), ("CISCO-DDP-IAPP-MIB", "ciscoDdpIappRogueApInfoGroup"), ("CISCO-DDP-IAPP-MIB", "ciscoDdpIappNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDdpIappCompliance = ciscoDdpIappCompliance.setStatus('current')
ciscoDdpIappConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 277, 2, 2, 1)).setObjects(("CISCO-DDP-IAPP-MIB", "cDdpIappMcastIpAddrType"), ("CISCO-DDP-IAPP-MIB", "cDdpIappMcastIpAddr"), ("CISCO-DDP-IAPP-MIB", "cDdpIappPort"), ("CISCO-DDP-IAPP-MIB", "cDdpIappRogueApNotifEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDdpIappConfigGroup = ciscoDdpIappConfigGroup.setStatus('current')
ciscoDdpIappRogueApInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 277, 2, 2, 2)).setObjects(("CISCO-DDP-IAPP-MIB", "cDdpIappLastRogueApMacAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDdpIappRogueApInfoGroup = ciscoDdpIappRogueApInfoGroup.setStatus('current')
ciscoDdpIappNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 277, 2, 2, 3)).setObjects(("CISCO-DDP-IAPP-MIB", "cDdpIappLastRogueApNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDdpIappNotificationGroup = ciscoDdpIappNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-DDP-IAPP-MIB", ciscoDdpIappMIBNotifications=ciscoDdpIappMIBNotifications, cDdpIappPort=cDdpIappPort, ciscoDdpIappMIBGroups=ciscoDdpIappMIBGroups, ciscoDdpIappMIBCompliances=ciscoDdpIappMIBCompliances, cDdpIappLastRogueApNotif=cDdpIappLastRogueApNotif, ciscoDdpIappMIB=ciscoDdpIappMIB, PYSNMP_MODULE_ID=ciscoDdpIappMIB, ciscoDdpIappMIBConformance=ciscoDdpIappMIBConformance, ciscoDdpIappMIBObjects=ciscoDdpIappMIBObjects, cDdpIappMcastIpAddrType=cDdpIappMcastIpAddrType, cDdpIappLastRogueApMacAddr=cDdpIappLastRogueApMacAddr, ciscoDdpIappCompliance=ciscoDdpIappCompliance, cDdpIappRogueApInfo=cDdpIappRogueApInfo, cDdpIappRogueApNotifEnabled=cDdpIappRogueApNotifEnabled, cDdpIappGlobalConfig=cDdpIappGlobalConfig, ciscoDdpIappNotificationGroup=ciscoDdpIappNotificationGroup, ciscoDdpIappConfigGroup=ciscoDdpIappConfigGroup, ciscoDdpIappRogueApInfoGroup=ciscoDdpIappRogueApInfoGroup, cDdpIappMcastIpAddr=cDdpIappMcastIpAddr)
