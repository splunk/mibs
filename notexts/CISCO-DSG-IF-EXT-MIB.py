#
# PySNMP MIB module CISCO-DSG-IF-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DSG-IF-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
dsgIfDownstreamEntry, dsgIfClassifierEntry = mibBuilder.importSymbols("DSG-IF-MIB", "dsgIfDownstreamEntry", "dsgIfClassifierEntry")
InetAddressDNS, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressDNS")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Counter32")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoDsgIfExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 777))
ciscoDsgIfExtMIB.setRevisions(('2011-08-15 00:00',))
if mibBuilder.loadTexts: ciscoDsgIfExtMIB.setLastUpdated('201109090000Z')
if mibBuilder.loadTexts: ciscoDsgIfExtMIB.setOrganization('Cisco Systems, Inc.')
ciscoDsgIfExtMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 777, 0))
ciscoDsgIfExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 777, 1))
ciscoDsgIfExtMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 777, 2))
cdsgIfExtClassifierTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 777, 1, 1), )
if mibBuilder.loadTexts: cdsgIfExtClassifierTable.setStatus('current')
cdsgIfExtClassifierEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 777, 1, 1, 1), )
dsgIfClassifierEntry.registerAugmentions(("CISCO-DSG-IF-EXT-MIB", "cdsgIfExtClassifierEntry"))
cdsgIfExtClassifierEntry.setIndexNames(*dsgIfClassifierEntry.getIndexNames())
if mibBuilder.loadTexts: cdsgIfExtClassifierEntry.setStatus('current')
cdsgIfExtClassSrcHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 777, 1, 1, 1, 1), InetAddressDNS()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdsgIfExtClassSrcHostName.setStatus('current')
cdsgIfExtClassDestHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 777, 1, 1, 1, 2), InetAddressDNS()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdsgIfExtClassDestHostName.setStatus('current')
cdsgIfExtDownstreamTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 777, 1, 2), )
if mibBuilder.loadTexts: cdsgIfExtDownstreamTable.setStatus('current')
cdsgIfExtDownstreamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 777, 1, 2, 1), )
dsgIfDownstreamEntry.registerAugmentions(("CISCO-DSG-IF-EXT-MIB", "cdsgIfExtDownstreamEntry"))
cdsgIfExtDownstreamEntry.setIndexNames(*dsgIfDownstreamEntry.getIndexNames())
if mibBuilder.loadTexts: cdsgIfExtDownstreamEntry.setStatus('current')
cdsgIfExtDownDsgDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 777, 1, 2, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdsgIfExtDownDsgDisable.setStatus('current')
ciscoDsgIfExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 777, 2, 1))
ciscoDsgIfExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 777, 2, 2))
ciscoDsgIfExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 777, 2, 1, 1)).setObjects(("CISCO-DSG-IF-EXT-MIB", "cdsgIfExtHostGroup"), ("CISCO-DSG-IF-EXT-MIB", "cdsgIfExtDownControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDsgIfExtMIBCompliance = ciscoDsgIfExtMIBCompliance.setStatus('current')
cdsgIfExtHostGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 777, 2, 2, 1)).setObjects(("CISCO-DSG-IF-EXT-MIB", "cdsgIfExtClassSrcHostName"), ("CISCO-DSG-IF-EXT-MIB", "cdsgIfExtClassDestHostName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsgIfExtHostGroup = cdsgIfExtHostGroup.setStatus('current')
cdsgIfExtDownControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 777, 2, 2, 2)).setObjects(("CISCO-DSG-IF-EXT-MIB", "cdsgIfExtDownDsgDisable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsgIfExtDownControlGroup = cdsgIfExtDownControlGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-DSG-IF-EXT-MIB", cdsgIfExtDownDsgDisable=cdsgIfExtDownDsgDisable, ciscoDsgIfExtMIBCompliances=ciscoDsgIfExtMIBCompliances, cdsgIfExtHostGroup=cdsgIfExtHostGroup, cdsgIfExtClassifierEntry=cdsgIfExtClassifierEntry, ciscoDsgIfExtMIBNotifs=ciscoDsgIfExtMIBNotifs, ciscoDsgIfExtMIBConform=ciscoDsgIfExtMIBConform, ciscoDsgIfExtMIBGroups=ciscoDsgIfExtMIBGroups, cdsgIfExtClassifierTable=cdsgIfExtClassifierTable, cdsgIfExtDownstreamTable=cdsgIfExtDownstreamTable, ciscoDsgIfExtMIB=ciscoDsgIfExtMIB, cdsgIfExtClassSrcHostName=cdsgIfExtClassSrcHostName, cdsgIfExtClassDestHostName=cdsgIfExtClassDestHostName, cdsgIfExtDownstreamEntry=cdsgIfExtDownstreamEntry, ciscoDsgIfExtMIBCompliance=ciscoDsgIfExtMIBCompliance, cdsgIfExtDownControlGroup=cdsgIfExtDownControlGroup, PYSNMP_MODULE_ID=ciscoDsgIfExtMIB, ciscoDsgIfExtMIBObjects=ciscoDsgIfExtMIBObjects)
