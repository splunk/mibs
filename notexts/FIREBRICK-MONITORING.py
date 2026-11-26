#
# PySNMP MIB module FIREBRICK-MONITORING (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/firebrick/FIREBRICK-MONITORING
# Produced by pysmi-1.1.12 at Thu Nov 26 06:09:34 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
firebrickNewStyle, = mibBuilder.importSymbols("FIREBRICK-MIB", "firebrickNewStyle")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter64, IpAddress, Bits, NotificationType, ModuleIdentity, Integer32, iso, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, enterprises, ObjectIdentity, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "Bits", "NotificationType", "ModuleIdentity", "Integer32", "iso", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "enterprises", "ObjectIdentity", "Unsigned32", "TimeTicks")
TimeStamp, TextualConvention, TimeInterval, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TextualConvention", "TimeInterval", "DisplayString", "TruthValue")
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
mibBuilder.exportSymbols("FIREBRICK-MONITORING", fbMonitoringMib=fbMonitoringMib, fbMonReadingTable=fbMonReadingTable, fbMonReadingName=fbMonReadingName, fbMonReadingValue=fbMonReadingValue, fbMonReadingEntry=fbMonReadingEntry, fbMonReadingIndex=fbMonReadingIndex, PYSNMP_MODULE_ID=fbMonitoringMib, fbMonReadingType=fbMonReadingType)
