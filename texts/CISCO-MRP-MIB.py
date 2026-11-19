#
# PySNMP MIB module CISCO-MRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-MRP-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:13 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMrpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 850))
ciscoMrpMIB.setRevisions(('2017-09-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMrpMIB.setRevisionsDescriptions(('Latest version of this MIB module.',))
if mibBuilder.loadTexts: ciscoMrpMIB.setLastUpdated('201709120000Z')
if mibBuilder.loadTexts: ciscoMrpMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMrpMIB.setContactInfo('Cisco Systems\n            Customer Service\n\n\n            Postal: 170 W Tasman Drive\n\n            San Jose, CA  95134\n\n            USA\n\n\n            Tel: +1 800 553-NETS\n\n\n            E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoMrpMIB.setDescription('The CISCO-MRP-MIB is used to monitor the Media Redundancy\n        Protocol (MRP) domains and notifying their state change. MRP is\n        a recovery protocol based on a ring topology, and the redundant\n        interconnection of MRP rings/domains.')
ciscoMrpMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 850, 0))
ciscoMrpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 850, 1))
ciscoMrpMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 850, 2))
ciscoMrpDomainTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 850, 1, 1), )
if mibBuilder.loadTexts: ciscoMrpDomainTable.setStatus('current')
if mibBuilder.loadTexts: ciscoMrpDomainTable.setDescription('Every entry in this table contains information about a Media\n        Redundancy Protocol (MRP) domain.')
ciscoMrpDomainEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 850, 1, 1, 1), ).setIndexNames((0, "CISCO-MRP-MIB", "ciscoMrpDomainIndex"))
if mibBuilder.loadTexts: ciscoMrpDomainEntry.setStatus('current')
if mibBuilder.loadTexts: ciscoMrpDomainEntry.setDescription('An entry in the mrpDomainTable.')
ciscoMrpDomainIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 850, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: ciscoMrpDomainIndex.setStatus('current')
if mibBuilder.loadTexts: ciscoMrpDomainIndex.setDescription('The index of the entry')
ciscoMrpDomainID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 850, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoMrpDomainID.setStatus('current')
if mibBuilder.loadTexts: ciscoMrpDomainID.setDescription('Universally unique identifier belongs to the MRP domain which\n        represents a ring. The IEC 61158-5-10 defines the structure of\n        the UUID as a data type numeric identifier 1025.')
ciscoMrpDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 850, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoMrpDomainName.setStatus('current')
if mibBuilder.loadTexts: ciscoMrpDomainName.setDescription('A logical name for the MRP domain to ease the management of MRP\n        domains.')
ciscoMrpDomainState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 850, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoMrpDomainState.setStatus('current')
if mibBuilder.loadTexts: ciscoMrpDomainState.setDescription('Operational status of the MRP entity.\n        undefined(0)  Value is not valid. All higher bits are invalid\n        and shall be reset.\n        ringOpen(1)  MRP ring redundancy lost. All higher bits are\n        invalid and shall be reset.\n        ringclose(2)  MRP ring redundancy achieved. All higher bits are\n        invalid and shall be reset.')
ciscoMrpRingOpen = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 850, 0, 1)).setObjects(("CISCO-MRP-MIB", "ciscoMrpDomainID"), ("CISCO-MRP-MIB", "ciscoMrpDomainName"), ("CISCO-MRP-MIB", "ciscoMrpDomainState"))
if mibBuilder.loadTexts: ciscoMrpRingOpen.setStatus('current')
if mibBuilder.loadTexts: ciscoMrpRingOpen.setDescription('A ciscoMrpRingOpen trap signifies that a specific MRP ring is\n        open.')
ciscoMrpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 850, 2, 1))
ciscoMrpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 850, 2, 2))
ciscoMrpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 850, 2, 1, 1)).setObjects(("CISCO-MRP-MIB", "ciscoMrpMIBMainObjectGroup"), ("CISCO-MRP-MIB", "ciscoMrpMIBNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMrpMIBCompliance = ciscoMrpMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoMrpMIBCompliance.setDescription('Cisco MRP MIB compliance object.')
ciscoMrpMIBMainObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 850, 2, 2, 1)).setObjects(("CISCO-MRP-MIB", "ciscoMrpDomainID"), ("CISCO-MRP-MIB", "ciscoMrpDomainName"), ("CISCO-MRP-MIB", "ciscoMrpDomainState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMrpMIBMainObjectGroup = ciscoMrpMIBMainObjectGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoMrpMIBMainObjectGroup.setDescription('A collection of objects required for monitoring of MRP domain.')
ciscoMrpMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 850, 2, 2, 2)).setObjects(("CISCO-MRP-MIB", "ciscoMrpRingOpen"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMrpMIBNotificationGroup = ciscoMrpMIBNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoMrpMIBNotificationGroup.setDescription('A notification which indicates specific ring open.')
mibBuilder.exportSymbols("CISCO-MRP-MIB", ciscoMrpMIBMainObjectGroup=ciscoMrpMIBMainObjectGroup, ciscoMrpMIBObjects=ciscoMrpMIBObjects, PYSNMP_MODULE_ID=ciscoMrpMIB, ciscoMrpDomainIndex=ciscoMrpDomainIndex, ciscoMrpDomainID=ciscoMrpDomainID, ciscoMrpMIBNotificationGroup=ciscoMrpMIBNotificationGroup, ciscoMrpMIBGroups=ciscoMrpMIBGroups, ciscoMrpRingOpen=ciscoMrpRingOpen, ciscoMrpMIBNotifs=ciscoMrpMIBNotifs, ciscoMrpMIBCompliance=ciscoMrpMIBCompliance, ciscoMrpDomainTable=ciscoMrpDomainTable, ciscoMrpDomainEntry=ciscoMrpDomainEntry, ciscoMrpMIB=ciscoMrpMIB, ciscoMrpDomainName=ciscoMrpDomainName, ciscoMrpDomainState=ciscoMrpDomainState, ciscoMrpMIBConform=ciscoMrpMIBConform, ciscoMrpMIBCompliances=ciscoMrpMIBCompliances)
