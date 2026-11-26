#
# PySNMP MIB module FIREBRICK-RUNSTATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/firebrick/FIREBRICK-RUNSTATS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:09:34 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
firebrickNewStyle, = mibBuilder.importSymbols("FIREBRICK-MIB", "firebrickNewStyle")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter64, IpAddress, Bits, Integer32, ModuleIdentity, NotificationType, iso, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, enterprises, ObjectIdentity, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "Bits", "Integer32", "ModuleIdentity", "NotificationType", "iso", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "enterprises", "ObjectIdentity", "Unsigned32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
fbRunMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 24693, 100, 3))
fbRunMib.setRevisions(('2020-06-17 00:00',))
if mibBuilder.loadTexts: fbRunMib.setLastUpdated('202006170000Z')
if mibBuilder.loadTexts: fbRunMib.setOrganization('Andrews & Arnold Limited')
fbRunStatsTable = MibTable((1, 3, 6, 1, 4, 1, 24693, 100, 3, 1), )
if mibBuilder.loadTexts: fbRunStatsTable.setStatus('current')
fbRunStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 24693, 100, 3, 1, 1), ).setIndexNames((0, "FIREBRICK-RUNSTATS-MIB", "fbRunCore"))
if mibBuilder.loadTexts: fbRunStatsEntry.setStatus('current')
fbRunCore = MibTableColumn((1, 3, 6, 1, 4, 1, 24693, 100, 3, 1, 1, 2), Integer32())
if mibBuilder.loadTexts: fbRunCore.setStatus('current')
fbRunBuffers = MibTableColumn((1, 3, 6, 1, 4, 1, 24693, 100, 3, 1, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fbRunBuffers.setStatus('current')
mibBuilder.exportSymbols("FIREBRICK-RUNSTATS-MIB", fbRunStatsTable=fbRunStatsTable, fbRunStatsEntry=fbRunStatsEntry, fbRunBuffers=fbRunBuffers, fbRunCore=fbRunCore, PYSNMP_MODULE_ID=fbRunMib, fbRunMib=fbRunMib)
