#
# PySNMP MIB module CISCO-LPTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-LPTS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoLptsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 812))
ciscoLptsMIB.setRevisions(('2013-09-03 00:00',))
if mibBuilder.loadTexts: ciscoLptsMIB.setLastUpdated('201309030000Z')
if mibBuilder.loadTexts: ciscoLptsMIB.setOrganization('Cisco Systems, Inc.')
class ClFlowType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("static", 1), ("global", 2), ("local", 3))

ciscoLptsMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 812, 0))
ciscoLptsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 812, 1))
ciscoLptsMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 812, 2))
clGlobalFlowTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 1), )
if mibBuilder.loadTexts: clGlobalFlowTable.setStatus('current')
clGlobalFlowEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 1, 1), ).setIndexNames((0, "CISCO-LPTS-MIB", "clGlobalFlowIndex"))
if mibBuilder.loadTexts: clGlobalFlowEntry.setStatus('current')
clGlobalFlowIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: clGlobalFlowIndex.setStatus('current')
clGlobalFlowType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clGlobalFlowType.setStatus('current')
clGlobalType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 1, 1, 3), ClFlowType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clGlobalType.setStatus('current')
clGlobalCurrentRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 1, 1, 4), Unsigned32()).setUnits('PPS').setMaxAccess("readwrite")
if mibBuilder.loadTexts: clGlobalCurrentRate.setStatus('current')
clLocalFlowTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 2), )
if mibBuilder.loadTexts: clLocalFlowTable.setStatus('current')
clLocalFlowEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 2, 1), ).setIndexNames((0, "CISCO-LPTS-MIB", "clGlobalFlowIndex"), (0, "CISCO-LPTS-MIB", "clLocalNodeID"))
if mibBuilder.loadTexts: clLocalFlowEntry.setStatus('current')
clLocalNodeID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: clLocalNodeID.setStatus('current')
clLocalType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 2, 1, 2), ClFlowType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clLocalType.setStatus('current')
clLocalCurrentRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 2, 1, 3), Unsigned32()).setUnits('PPS').setMaxAccess("readonly")
if mibBuilder.loadTexts: clLocalCurrentRate.setStatus('current')
clLocalAccepted = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clLocalAccepted.setStatus('current')
clLocalDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clLocalDropped.setStatus('current')
clLocalTosValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 812, 1, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clLocalTosValue.setStatus('current')
ciscoLptsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 812, 2, 1))
ciscoLptsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 812, 2, 2))
ciscoLptsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 812, 2, 1, 1)).setObjects(("CISCO-LPTS-MIB", "clLocalFlowGroup"), ("CISCO-LPTS-MIB", "clGlobalFlowGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLptsMIBCompliance = ciscoLptsMIBCompliance.setStatus('current')
clGlobalFlowGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 812, 2, 2, 1)).setObjects(("CISCO-LPTS-MIB", "clGlobalFlowType"), ("CISCO-LPTS-MIB", "clGlobalCurrentRate"), ("CISCO-LPTS-MIB", "clGlobalType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clGlobalFlowGroup = clGlobalFlowGroup.setStatus('current')
clLocalFlowGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 812, 2, 2, 2)).setObjects(("CISCO-LPTS-MIB", "clLocalCurrentRate"), ("CISCO-LPTS-MIB", "clLocalAccepted"), ("CISCO-LPTS-MIB", "clLocalDropped"), ("CISCO-LPTS-MIB", "clLocalType"), ("CISCO-LPTS-MIB", "clLocalTosValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clLocalFlowGroup = clLocalFlowGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-LPTS-MIB", clGlobalCurrentRate=clGlobalCurrentRate, ciscoLptsMIBObjects=ciscoLptsMIBObjects, clGlobalType=clGlobalType, clLocalFlowGroup=clLocalFlowGroup, ciscoLptsMIBConform=ciscoLptsMIBConform, clGlobalFlowTable=clGlobalFlowTable, clGlobalFlowType=clGlobalFlowType, clGlobalFlowGroup=clGlobalFlowGroup, ciscoLptsMIBGroups=ciscoLptsMIBGroups, ciscoLptsMIBCompliances=ciscoLptsMIBCompliances, clLocalAccepted=clLocalAccepted, clLocalFlowEntry=clLocalFlowEntry, clLocalDropped=clLocalDropped, ciscoLptsMIBNotifs=ciscoLptsMIBNotifs, PYSNMP_MODULE_ID=ciscoLptsMIB, ciscoLptsMIBCompliance=ciscoLptsMIBCompliance, clLocalTosValue=clLocalTosValue, clLocalType=clLocalType, clGlobalFlowIndex=clGlobalFlowIndex, ClFlowType=ClFlowType, clLocalFlowTable=clLocalFlowTable, clLocalCurrentRate=clLocalCurrentRate, clLocalNodeID=clLocalNodeID, clGlobalFlowEntry=clGlobalFlowEntry, ciscoLptsMIB=ciscoLptsMIB)
