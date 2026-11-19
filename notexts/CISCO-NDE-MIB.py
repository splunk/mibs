#
# PySNMP MIB module CISCO-NDE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-NDE-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:44 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Gauge32, ModuleIdentity, Integer32, Bits, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Integer32", "Bits", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "Counter32")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoNDEMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 226))
ciscoNDEMIB.setRevisions(('2006-03-01 00:00', '2005-12-06 00:00', '2001-08-08 00:00',))
if mibBuilder.loadTexts: ciscoNDEMIB.setLastUpdated('200603010000Z')
if mibBuilder.loadTexts: ciscoNDEMIB.setOrganization('Cisco Systems, Inc.')
ciscoNDEMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 226, 1))
cndeCollectorConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 226, 1, 1))
cndeMaxCollectors = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 226, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cndeMaxCollectors.setStatus('current')
cndeCollectorTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 226, 1, 1, 2), )
if mibBuilder.loadTexts: cndeCollectorTable.setStatus('current')
cndeCollectorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 226, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-NDE-MIB", "cndeCollectorAddressType"), (0, "CISCO-NDE-MIB", "cndeCollectorAddress"), (0, "CISCO-NDE-MIB", "cndeCollectorPort"))
if mibBuilder.loadTexts: cndeCollectorEntry.setStatus('current')
cndeCollectorAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 226, 1, 1, 2, 1, 1), InetAddressType())
if mibBuilder.loadTexts: cndeCollectorAddressType.setStatus('current')
cndeCollectorAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 226, 1, 1, 2, 1, 2), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: cndeCollectorAddress.setStatus('current')
cndeCollectorPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 226, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: cndeCollectorPort.setStatus('current')
cndeCollectorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 226, 1, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cndeCollectorStatus.setStatus('current')
cndeMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 226, 2))
cndeMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 226, 0))
cndeMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 226, 3))
cndeMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 226, 3, 1))
cndeMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 226, 3, 2))
cndeMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 226, 3, 1, 1)).setObjects(("CISCO-NDE-MIB", "cndeCollectorConfigurationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cndeMIBCompliance = cndeMIBCompliance.setStatus('current')
cndeCollectorConfigurationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 226, 3, 2, 1)).setObjects(("CISCO-NDE-MIB", "cndeMaxCollectors"), ("CISCO-NDE-MIB", "cndeCollectorStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cndeCollectorConfigurationGroup = cndeCollectorConfigurationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-NDE-MIB", cndeCollectorTable=cndeCollectorTable, cndeCollectorAddressType=cndeCollectorAddressType, cndeCollectorConfigurationGroup=cndeCollectorConfigurationGroup, cndeMIBCompliance=cndeMIBCompliance, cndeCollectorAddress=cndeCollectorAddress, cndeMIBNotifications=cndeMIBNotifications, PYSNMP_MODULE_ID=ciscoNDEMIB, cndeMIBGroups=cndeMIBGroups, cndeMIBConformance=cndeMIBConformance, cndeMIBNotifs=cndeMIBNotifs, cndeMaxCollectors=cndeMaxCollectors, ciscoNDEMIB=ciscoNDEMIB, cndeCollectorConfiguration=cndeCollectorConfiguration, ciscoNDEMIBObjects=ciscoNDEMIBObjects, cndeCollectorPort=cndeCollectorPort, cndeMIBCompliances=cndeMIBCompliances, cndeCollectorStatus=cndeCollectorStatus, cndeCollectorEntry=cndeCollectorEntry)
