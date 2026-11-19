#
# PySNMP MIB module CISCO-DDP-IAPP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DDP-IAPP-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:06 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoPort, = mibBuilder.importSymbols("CISCO-TC", "CiscoPort")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
MacAddress, TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString", "TruthValue")
ciscoDdpIappMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 277))
ciscoDdpIappMIB.setRevisions(('2002-07-31 00:00', '2002-07-17 00:00', '2002-03-19 00:00', '2002-03-07 00:00', '2001-09-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDdpIappMIB.setRevisionsDescriptions(('Correct DEFVAL for cDdpIappMcastIpAddr.', 'Removed cDdpIappP802dot1XVersion, added\n                cDdpIappLastRogueApMacAddr, cDdpIappLastRogueApNotif,\n                and cDdpIappRogueApNotifEnabled objects. Changed\n                cDdpIappPort object to read-only access.', 'Changing the description for cDdpIappPort to be a\n                UDP port and Email contact address.', 'Changing DEFVALs for cDdpIappMcastIpAddr and \n                cDdpIappPort.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoDdpIappMIB.setLastUpdated('200207310000Z')
if mibBuilder.loadTexts: ciscoDdpIappMIB.setOrganization('Cisco System Inc.')
if mibBuilder.loadTexts: ciscoDdpIappMIB.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive,\n                        San Jose CA 95134-1706.\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-dot11@cisco.com')
if mibBuilder.loadTexts: ciscoDdpIappMIB.setDescription('This MIB module describes the management support for\n                the Inter-Access Point Protocol (IAPP).  IAPP is a \n                Cisco propriety Data Delivery Protocol (DDP), and the\n                protocol defines the function and frame formats for \n                communication between IEEE 802.11 Standard wireless \n                LAN stations, i.e. access point (AP), work-group \n                bridge, and repeater.  The IAPP supports wireless \n                station LAN attachment, client roaming, association\n                management, and diagnostic services.')
ciscoDdpIappMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 277, 0))
ciscoDdpIappMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 277, 1))
ciscoDdpIappMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 277, 2))
cDdpIappGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 277, 1, 1))
cDdpIappRogueApInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 277, 1, 2))
cDdpIappMcastIpAddrType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 277, 1, 1, 1), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cDdpIappMcastIpAddrType.setStatus('current')
if mibBuilder.loadTexts: cDdpIappMcastIpAddrType.setDescription('Represents the type of address stored in\n                cDdpIappMcastIpAddr.')
cDdpIappMcastIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 277, 1, 1, 2), InetAddress().clone(hexValue="e0000128")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cDdpIappMcastIpAddr.setStatus('current')
if mibBuilder.loadTexts: cDdpIappMcastIpAddr.setDescription('Multicast IP network address over which applicable \n                 IAPP packets are exchanged between stations.')
cDdpIappPort = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 277, 1, 1, 3), CiscoPort().clone(2887)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDdpIappPort.setStatus('current')
if mibBuilder.loadTexts: cDdpIappPort.setDescription('UPD port identifier through which applicable IAPP\n                 packets are exchanged between stations.')
cDdpIappRogueApNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 277, 1, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cDdpIappRogueApNotifEnabled.setStatus('current')
if mibBuilder.loadTexts: cDdpIappRogueApNotifEnabled.setDescription('Indicates whether rogue access point notifications\n                including cDdpIappLastRogueApNotif notification \n                will or will not be sent by the agent when a rogue\n                access point is detected.  If it is true(1), \n                notifications will be sent.  If it is false(2), \n                notifications will not be sent.')
cDdpIappLastRogueApMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 277, 1, 2, 1), MacAddress().clone(hexValue="000000000000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDdpIappLastRogueApMacAddr.setStatus('current')
if mibBuilder.loadTexts: cDdpIappLastRogueApMacAddr.setDescription('This is the MAC address of the last detected rogue\n                access point for this device.  The value is zero if \n                there has not been any rogue access point detected \n                since system reload.')
cDdpIappLastRogueApNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 277, 0, 1)).setObjects(("CISCO-DDP-IAPP-MIB", "cDdpIappLastRogueApMacAddr"))
if mibBuilder.loadTexts: cDdpIappLastRogueApNotif.setStatus('current')
if mibBuilder.loadTexts: cDdpIappLastRogueApNotif.setDescription('This notification will be sent when a rogue \n                access point is detected, that is the object value\n                of cDdpIappLastRogueApMacAddr had changed. The \n                cDdpIappLastRogueApMacAddr specify the latest \n                rogue access point MAC address.  The sending\n                of notifications can be enabled or disabled\n                via the cDdpIappRogueApNotifEnabled object.')
ciscoDdpIappMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 277, 2, 1))
ciscoDdpIappMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 277, 2, 2))
ciscoDdpIappCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 277, 2, 1, 1)).setObjects(("CISCO-DDP-IAPP-MIB", "ciscoDdpIappConfigGroup"), ("CISCO-DDP-IAPP-MIB", "ciscoDdpIappRogueApInfoGroup"), ("CISCO-DDP-IAPP-MIB", "ciscoDdpIappNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDdpIappCompliance = ciscoDdpIappCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoDdpIappCompliance.setDescription('The compliance statement for entities implementing\n                the CISCO-DDP-IAPP-MIB.')
ciscoDdpIappConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 277, 2, 2, 1)).setObjects(("CISCO-DDP-IAPP-MIB", "cDdpIappMcastIpAddrType"), ("CISCO-DDP-IAPP-MIB", "cDdpIappMcastIpAddr"), ("CISCO-DDP-IAPP-MIB", "cDdpIappPort"), ("CISCO-DDP-IAPP-MIB", "cDdpIappRogueApNotifEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDdpIappConfigGroup = ciscoDdpIappConfigGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoDdpIappConfigGroup.setDescription('Configurations to support operation of the IAPP \n                protocols and subsystem.')
ciscoDdpIappRogueApInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 277, 2, 2, 2)).setObjects(("CISCO-DDP-IAPP-MIB", "cDdpIappLastRogueApMacAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDdpIappRogueApInfoGroup = ciscoDdpIappRogueApInfoGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoDdpIappRogueApInfoGroup.setDescription('Rogue AP information from the operation of the \n                IAPP subsystem.')
ciscoDdpIappNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 277, 2, 2, 3)).setObjects(("CISCO-DDP-IAPP-MIB", "cDdpIappLastRogueApNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDdpIappNotificationGroup = ciscoDdpIappNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoDdpIappNotificationGroup.setDescription('This is the notification group for the\n                CISCO-DDP-IAPP-MIB.')
mibBuilder.exportSymbols("CISCO-DDP-IAPP-MIB", ciscoDdpIappMIBConformance=ciscoDdpIappMIBConformance, cDdpIappRogueApInfo=cDdpIappRogueApInfo, ciscoDdpIappCompliance=ciscoDdpIappCompliance, cDdpIappGlobalConfig=cDdpIappGlobalConfig, cDdpIappMcastIpAddrType=cDdpIappMcastIpAddrType, cDdpIappPort=cDdpIappPort, ciscoDdpIappNotificationGroup=ciscoDdpIappNotificationGroup, cDdpIappRogueApNotifEnabled=cDdpIappRogueApNotifEnabled, cDdpIappMcastIpAddr=cDdpIappMcastIpAddr, ciscoDdpIappMIBGroups=ciscoDdpIappMIBGroups, ciscoDdpIappMIBObjects=ciscoDdpIappMIBObjects, ciscoDdpIappRogueApInfoGroup=ciscoDdpIappRogueApInfoGroup, ciscoDdpIappMIBCompliances=ciscoDdpIappMIBCompliances, PYSNMP_MODULE_ID=ciscoDdpIappMIB, ciscoDdpIappConfigGroup=ciscoDdpIappConfigGroup, ciscoDdpIappMIB=ciscoDdpIappMIB, ciscoDdpIappMIBNotifications=ciscoDdpIappMIBNotifications, cDdpIappLastRogueApNotif=cDdpIappLastRogueApNotif, cDdpIappLastRogueApMacAddr=cDdpIappLastRogueApMacAddr)
