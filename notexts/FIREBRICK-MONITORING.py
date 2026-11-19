#
# PySNMP MIB module FIREBRICK-MONITORING (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/firebrick/FIREBRICK-MONITORING
# Produced by pysmi-1.1.12 at Thu Nov 19 08:34:53 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
firebrickNewStyle, = mibBuilder.importSymbols("FIREBRICK-MIB", "firebrickNewStyle")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ObjectIdentity, NotificationType, Unsigned32, Integer32, Counter32, enterprises, iso, TimeTicks, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "NotificationType", "Unsigned32", "Integer32", "Counter32", "enterprises", "iso", "TimeTicks", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "Counter64", "ModuleIdentity")
TruthValue, DisplayString, TimeStamp, TimeInterval, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TimeStamp", "TimeInterval", "TextualConvention")
fbMonitoringMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 24693, 100, 1))
fbMonitoringMib.setRevisions(('2020-06-17 00:00',))
if mibBuilder.loadTexts: fbMonitoringMib.setLastUpdated('202006170000Z')
if mibBuilder.loadTexts: fbMonitoringMib.setOrganization('Andrews & Arnold Limited')
fbMonReadingTable = MibTable((1, 3, 6, 1, 4, 1, 24693, 100, 1, 1), )
if mibBuilder.loadTexts: fbMonReadingTable.setStatus('current')
fbMonReadingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 24693, 100, 1, 1, 1), ).setIndexNames((0, "FIREBRICK-MONITORING", "fbMonReadingIndex"))
if mibBuilder.loadTexts: fbMonReadingEntry.setStatus('current')
fbMonReadingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 24693, 100, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: fbMonReadingIndex.setStatus('current')
fbMonReadingType = MibTableColumn((1, 3, 6, 1, 4, 1, 24693, 100, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fbMonReadingType.setStatus('current')
fbMonReadingName = MibTableColumn((1, 3, 6, 1, 4, 1, 24693, 100, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fbMonReadingName.setStatus('current')
fbMonReadingValue = MibTableColumn((1, 3, 6, 1, 4, 1, 24693, 100, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fbMonReadingValue.setStatus('current')
mibBuilder.exportSymbols("FIREBRICK-MONITORING", fbMonReadingTable=fbMonReadingTable, fbMonReadingEntry=fbMonReadingEntry, fbMonReadingType=fbMonReadingType, fbMonReadingName=fbMonReadingName, fbMonReadingIndex=fbMonReadingIndex, fbMonReadingValue=fbMonReadingValue, PYSNMP_MODULE_ID=fbMonitoringMib, fbMonitoringMib=fbMonitoringMib)
