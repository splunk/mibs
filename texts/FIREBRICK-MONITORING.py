#
# PySNMP MIB module FIREBRICK-MONITORING (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/firebrick/FIREBRICK-MONITORING
# Produced by pysmi-1.1.12 at Thu Nov 19 14:36:31 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
firebrickNewStyle, = mibBuilder.importSymbols("FIREBRICK-MIB", "firebrickNewStyle")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
enterprises, TimeTicks, Bits, ModuleIdentity, ObjectIdentity, Unsigned32, MibIdentifier, Counter64, IpAddress, NotificationType, Counter32, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "TimeTicks", "Bits", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "MibIdentifier", "Counter64", "IpAddress", "NotificationType", "Counter32", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
DisplayString, TimeStamp, TextualConvention, TimeInterval, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "TextualConvention", "TimeInterval", "TruthValue")
fbMonitoringMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 24693, 100, 1))
fbMonitoringMib.setRevisions(('2020-06-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fbMonitoringMib.setRevisionsDescriptions(('Initial version of this MIB module',))
if mibBuilder.loadTexts: fbMonitoringMib.setLastUpdated('202006170000Z')
if mibBuilder.loadTexts: fbMonitoringMib.setOrganization('Andrews & Arnold Limited')
if mibBuilder.loadTexts: fbMonitoringMib.setContactInfo('Andrews & Arnold\n        Unit 1&2, Enterprise Court\n        Bracknell, Berkshire, RG12 1QS\n        United Kingdom\n\n        Tel: +44 3333 400 999\n        Email: support@aa.net.uk')
if mibBuilder.loadTexts: fbMonitoringMib.setDescription('This is a MIB Module for monitoring the Firebrick-specific structures\n        for general system features.')
fbMonReadingTable = MibTable((1, 3, 6, 1, 4, 1, 24693, 100, 1, 1), )
if mibBuilder.loadTexts: fbMonReadingTable.setStatus('current')
if mibBuilder.loadTexts: fbMonReadingTable.setDescription('The list of readings for this Firebrick')
fbMonReadingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 24693, 100, 1, 1, 1), ).setIndexNames((0, "FIREBRICK-MONITORING", "fbMonReadingIndex"))
if mibBuilder.loadTexts: fbMonReadingEntry.setStatus('current')
if mibBuilder.loadTexts: fbMonReadingEntry.setDescription('An entry in the FB readings table')
fbMonReadingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 24693, 100, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: fbMonReadingIndex.setStatus('current')
if mibBuilder.loadTexts: fbMonReadingIndex.setDescription('The index for the readings table')
fbMonReadingType = MibTableColumn((1, 3, 6, 1, 4, 1, 24693, 100, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fbMonReadingType.setStatus('current')
if mibBuilder.loadTexts: fbMonReadingType.setDescription('The type of this reading')
fbMonReadingName = MibTableColumn((1, 3, 6, 1, 4, 1, 24693, 100, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fbMonReadingName.setStatus('current')
if mibBuilder.loadTexts: fbMonReadingName.setDescription('The name of this reading')
fbMonReadingValue = MibTableColumn((1, 3, 6, 1, 4, 1, 24693, 100, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fbMonReadingValue.setStatus('current')
if mibBuilder.loadTexts: fbMonReadingValue.setDescription('The value of this reading')
mibBuilder.exportSymbols("FIREBRICK-MONITORING", fbMonReadingIndex=fbMonReadingIndex, fbMonitoringMib=fbMonitoringMib, fbMonReadingType=fbMonReadingType, fbMonReadingValue=fbMonReadingValue, fbMonReadingEntry=fbMonReadingEntry, fbMonReadingName=fbMonReadingName, PYSNMP_MODULE_ID=fbMonitoringMib, fbMonReadingTable=fbMonReadingTable)
