#
# PySNMP MIB module CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:13 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoWanPersistentXgcpEventsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 18))
ciscoWanPersistentXgcpEventsMIB.setRevisions(('2003-10-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWanPersistentXgcpEventsMIB.setRevisionsDescriptions(('Update descriptions in the MIB.\n                ',))
if mibBuilder.loadTexts: ciscoWanPersistentXgcpEventsMIB.setLastUpdated('200310200000Z')
if mibBuilder.loadTexts: ciscoWanPersistentXgcpEventsMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanPersistentXgcpEventsMIB.setContactInfo('       Cisco Systems\n                    Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA 95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-voice@cisco.com')
if mibBuilder.loadTexts: ciscoWanPersistentXgcpEventsMIB.setDescription('The MIB module for managing CA(Call Agent) events.\n            ')
ciscoWanPersistentXgcpEventsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 18, 1))
persistentXgcpEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1))
persistentXgcpEventsTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1, 1), )
if mibBuilder.loadTexts: persistentXgcpEventsTable.setStatus('current')
if mibBuilder.loadTexts: persistentXgcpEventsTable.setDescription('The persistentXgcpEventsTable contains\n            configuration information about xGCP events\n            which involve a persistent notification request.\n           ')
persistentXgcpEventsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB", "persistentXgcpEventNum"))
if mibBuilder.loadTexts: persistentXgcpEventsEntry.setStatus('current')
if mibBuilder.loadTexts: persistentXgcpEventsEntry.setDescription("An entry in the persistentXgcpEventsTable. Each\n         entry consists of persistentXgcpEventNum - Index\n         to the persistentXgcpEventsTable. \n\n         persistentXgcpEventName - Name of the xGCP\n         event that needs persistent notification\n         to the call agent for example 't/hd'.\n\n         persistentXgcpEventRowStatus -This indicates\n         whether an xGCP event is added in this entry\n         or not.\n\n         This table is not created implicitly. The user\n         can add xGCP event or delete an xGCP event.\n        ")
persistentXgcpEventNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: persistentXgcpEventNum.setStatus('current')
if mibBuilder.loadTexts: persistentXgcpEventNum.setDescription('This object is a index to persistentXgcpEventsTable.\n        ')
persistentXgcpEventName = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: persistentXgcpEventName.setStatus('current')
if mibBuilder.loadTexts: persistentXgcpEventName.setDescription("This object holds the name of the event\n         for example 't/hd' or 't/hu'.\n        ")
persistentXgcpEventRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: persistentXgcpEventRowStatus.setStatus('current')
if mibBuilder.loadTexts: persistentXgcpEventRowStatus.setDescription("This object allows to add or delete an entry. \n            Modifying an entry is not allowed.\n\n            An entry may be created using the 'createAndGo' option.\n            When the row is successfully created, the RowStatus would\n            be set to 'active' by the agent. An entry may be deleted\n            by setting the RowStatus to 'destroy'. Other options\n            such as `CreateAndWait', 'notInService', 'notReady' will\n            not be used.\n\n            For creating an entry the persistentXgcpEventNum and \n            persistentXgcpEventName must be provided.\n  \n            This object tells call control whether or not a particular \n            xGCP event is added or not, based on this the call control \n            module will decide  whether or not to notify (NTFY) call \n            agent when a particular xGCP event is received,\n            without waiting for CA to request for that event.\n           ")
persistentXgcpEventsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 18, 2))
persistentXgcpEventsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 18, 2, 1))
persistentXgcpEventsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 18, 2, 2))
persistentXgcpEventsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 18, 2, 1, 1)).setObjects(("CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB", "persistentXgcpEventsMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    persistentXgcpEventsMIBCompliance = persistentXgcpEventsMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: persistentXgcpEventsMIBCompliance.setDescription(' The complaince statement for persistent Xgcp events\n              which implement persistentXgcpEvents MIB.')
persistentXgcpEventsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 18, 2, 2, 1)).setObjects(("CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB", "persistentXgcpEventName"), ("CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB", "persistentXgcpEventRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    persistentXgcpEventsMIBGroup = persistentXgcpEventsMIBGroup.setStatus('current')
if mibBuilder.loadTexts: persistentXgcpEventsMIBGroup.setDescription('This group contains objects related to\n             configuration of persistent xGCP events.\n            ')
mibBuilder.exportSymbols("CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB", persistentXgcpEventNum=persistentXgcpEventNum, persistentXgcpEventsMIBCompliance=persistentXgcpEventsMIBCompliance, persistentXgcpEventsMIBGroup=persistentXgcpEventsMIBGroup, ciscoWanPersistentXgcpEventsMIB=ciscoWanPersistentXgcpEventsMIB, persistentXgcpEventName=persistentXgcpEventName, persistentXgcpEventRowStatus=persistentXgcpEventRowStatus, PYSNMP_MODULE_ID=ciscoWanPersistentXgcpEventsMIB, persistentXgcpEventsTable=persistentXgcpEventsTable, persistentXgcpEvents=persistentXgcpEvents, persistentXgcpEventsMIBCompliances=persistentXgcpEventsMIBCompliances, ciscoWanPersistentXgcpEventsMIBObjects=ciscoWanPersistentXgcpEventsMIBObjects, persistentXgcpEventsEntry=persistentXgcpEventsEntry, persistentXgcpEventsMIBConformance=persistentXgcpEventsMIBConformance, persistentXgcpEventsMIBGroups=persistentXgcpEventsMIBGroups)
