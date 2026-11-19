#
# PySNMP MIB module WLSX-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arubaos/WLSX-STATS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:30:53 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
wlsxEnterpriseMibModules, = mibBuilder.importSymbols("ARUBA-MIB", "wlsxEnterpriseMibModules")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, Unsigned32, Bits, Gauge32, TimeTicks, ModuleIdentity, snmpModules, MibIdentifier, Integer32, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "Unsigned32", "Bits", "Gauge32", "TimeTicks", "ModuleIdentity", "snmpModules", "MibIdentifier", "Integer32", "ObjectIdentity", "NotificationType")
DisplayString, TimeInterval, TDomain, MacAddress, RowStatus, StorageType, TestAndIncr, PhysAddress, TextualConvention, TruthValue, TAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeInterval", "TDomain", "MacAddress", "RowStatus", "StorageType", "TestAndIncr", "PhysAddress", "TextualConvention", "TruthValue", "TAddress")
wlsxStatsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15))
wlsxStatsMIB.setRevisions(('2020-08-14 17:45',))
if mibBuilder.loadTexts: wlsxStatsMIB.setLastUpdated('202008141745Z')
if mibBuilder.loadTexts: wlsxStatsMIB.setOrganization('Aruba, a Hewlett Packard Enterprise company')
wlsxStatsOpGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15, 1))
wlsxStatsRequestTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15, 1, 1), )
if mibBuilder.loadTexts: wlsxStatsRequestTable.setStatus('current')
wlsxStatsRequestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15, 1, 1, 1), ).setIndexNames((0, "WLSX-STATS-MIB", "wlsxStatsIndex"))
if mibBuilder.loadTexts: wlsxStatsRequestEntry.setStatus('current')
wlsxStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: wlsxStatsIndex.setStatus('current')
wlsxStatsReqType = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15, 1, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wlsxStatsReqType.setStatus('current')
wlsxStatsInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15, 1, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wlsxStatsInterval.setStatus('current')
wlsxStatsCookie = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15, 1, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wlsxStatsCookie.setStatus('current')
mibBuilder.exportSymbols("WLSX-STATS-MIB", wlsxStatsIndex=wlsxStatsIndex, wlsxStatsCookie=wlsxStatsCookie, PYSNMP_MODULE_ID=wlsxStatsMIB, wlsxStatsRequestEntry=wlsxStatsRequestEntry, wlsxStatsInterval=wlsxStatsInterval, wlsxStatsOpGroup=wlsxStatsOpGroup, wlsxStatsMIB=wlsxStatsMIB, wlsxStatsReqType=wlsxStatsReqType, wlsxStatsRequestTable=wlsxStatsRequestTable)
