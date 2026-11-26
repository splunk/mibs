#
# PySNMP MIB module CISCO-DSG-IF-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DSG-IF-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:57 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
dsgIfClassifierEntry, dsgIfDownstreamEntry = mibBuilder.importSymbols("DSG-IF-MIB", "dsgIfClassifierEntry", "dsgIfDownstreamEntry")
InetAddressDNS, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressDNS")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
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
mibBuilder.exportSymbols("CISCO-DSG-IF-EXT-MIB", ciscoDsgIfExtMIBConform=ciscoDsgIfExtMIBConform, cdsgIfExtDownDsgDisable=cdsgIfExtDownDsgDisable, PYSNMP_MODULE_ID=ciscoDsgIfExtMIB, cdsgIfExtClassSrcHostName=cdsgIfExtClassSrcHostName, cdsgIfExtDownstreamTable=cdsgIfExtDownstreamTable, ciscoDsgIfExtMIBCompliance=ciscoDsgIfExtMIBCompliance, cdsgIfExtClassifierEntry=cdsgIfExtClassifierEntry, ciscoDsgIfExtMIBCompliances=ciscoDsgIfExtMIBCompliances, cdsgIfExtDownstreamEntry=cdsgIfExtDownstreamEntry, ciscoDsgIfExtMIBObjects=ciscoDsgIfExtMIBObjects, cdsgIfExtHostGroup=cdsgIfExtHostGroup, ciscoDsgIfExtMIBNotifs=ciscoDsgIfExtMIBNotifs, ciscoDsgIfExtMIBGroups=ciscoDsgIfExtMIBGroups, ciscoDsgIfExtMIB=ciscoDsgIfExtMIB, cdsgIfExtClassifierTable=cdsgIfExtClassifierTable, cdsgIfExtClassDestHostName=cdsgIfExtClassDestHostName, cdsgIfExtDownControlGroup=cdsgIfExtDownControlGroup)
