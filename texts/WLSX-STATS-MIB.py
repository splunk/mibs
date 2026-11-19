#
# PySNMP MIB module WLSX-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arubaos/WLSX-STATS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:30:55 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
wlsxEnterpriseMibModules, = mibBuilder.importSymbols("ARUBA-MIB", "wlsxEnterpriseMibModules")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, Counter64, snmpModules, Counter32, IpAddress, Gauge32, MibIdentifier, ObjectIdentity, TimeTicks, ModuleIdentity, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "Counter64", "snmpModules", "Counter32", "IpAddress", "Gauge32", "MibIdentifier", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "Bits", "Unsigned32")
TextualConvention, PhysAddress, RowStatus, TestAndIncr, TimeInterval, StorageType, MacAddress, TDomain, TruthValue, DisplayString, TAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "PhysAddress", "RowStatus", "TestAndIncr", "TimeInterval", "StorageType", "MacAddress", "TDomain", "TruthValue", "DisplayString", "TAddress")
wlsxStatsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15))
wlsxStatsMIB.setRevisions(('2020-08-14 17:45',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: wlsxStatsMIB.setRevisionsDescriptions(('The initial revision.',))
if mibBuilder.loadTexts: wlsxStatsMIB.setLastUpdated('202008141745Z')
if mibBuilder.loadTexts: wlsxStatsMIB.setOrganization('Aruba, a Hewlett Packard Enterprise company')
if mibBuilder.loadTexts: wlsxStatsMIB.setContactInfo('Postal:    3333 Scott Blvd,\n                        Santa Clara, CA 95054\n            E-mail:     aruba-ext-eng-reg@hpe.com\n            Phone:      408 227 4500\n            Fax:        408 752 0626')
if mibBuilder.loadTexts: wlsxStatsMIB.setDescription('This MIB module defines MIB objects which provide\n            information about the Statistics in the \n\t\t\tAruba controller.')
wlsxStatsOpGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15, 1))
wlsxStatsRequestTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15, 1, 1), )
if mibBuilder.loadTexts: wlsxStatsRequestTable.setStatus('current')
if mibBuilder.loadTexts: wlsxStatsRequestTable.setDescription('\n\t\t')
wlsxStatsRequestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15, 1, 1, 1), ).setIndexNames((0, "WLSX-STATS-MIB", "wlsxStatsIndex"))
if mibBuilder.loadTexts: wlsxStatsRequestEntry.setStatus('current')
if mibBuilder.loadTexts: wlsxStatsRequestEntry.setDescription('')
wlsxStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: wlsxStatsIndex.setStatus('current')
if mibBuilder.loadTexts: wlsxStatsIndex.setDescription('\n\t\t\t\tStats Index\n\t\t\t')
wlsxStatsReqType = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15, 1, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wlsxStatsReqType.setStatus('current')
if mibBuilder.loadTexts: wlsxStatsReqType.setDescription('\n\t\t\t\tRequest Type\n\t\t\t')
wlsxStatsInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15, 1, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wlsxStatsInterval.setStatus('current')
if mibBuilder.loadTexts: wlsxStatsInterval.setDescription('\n\t\t\t\tStats Interval\n\t\t\t')
wlsxStatsCookie = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15, 1, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wlsxStatsCookie.setStatus('current')
if mibBuilder.loadTexts: wlsxStatsCookie.setDescription('\n\t\t\t\tCookie for the config sync operation\n\t\t\t')
mibBuilder.exportSymbols("WLSX-STATS-MIB", wlsxStatsCookie=wlsxStatsCookie, wlsxStatsInterval=wlsxStatsInterval, wlsxStatsRequestTable=wlsxStatsRequestTable, wlsxStatsMIB=wlsxStatsMIB, wlsxStatsRequestEntry=wlsxStatsRequestEntry, wlsxStatsReqType=wlsxStatsReqType, PYSNMP_MODULE_ID=wlsxStatsMIB, wlsxStatsIndex=wlsxStatsIndex, wlsxStatsOpGroup=wlsxStatsOpGroup)
