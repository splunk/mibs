#
# PySNMP MIB module FIREBRICK-RUNSTATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/firebrick/FIREBRICK-RUNSTATS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:34:54 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
firebrickNewStyle, = mibBuilder.importSymbols("FIREBRICK-MIB", "firebrickNewStyle")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, enterprises, Integer32, iso, Bits, Unsigned32, MibIdentifier, ModuleIdentity, IpAddress, Counter32, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "enterprises", "Integer32", "iso", "Bits", "Unsigned32", "MibIdentifier", "ModuleIdentity", "IpAddress", "Counter32", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
fbRunMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 24693, 100, 3))
fbRunMib.setRevisions(('2020-06-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fbRunMib.setRevisionsDescriptions(('Initial version of this MIB module',))
if mibBuilder.loadTexts: fbRunMib.setLastUpdated('202006170000Z')
if mibBuilder.loadTexts: fbRunMib.setOrganization('Andrews & Arnold Limited')
if mibBuilder.loadTexts: fbRunMib.setContactInfo('Andrews & Arnold\n        Unit 1&2, Enterprise Court\n        Bracknell, Berkshire, RG12 1QS\n        United Kingdom\n\n        Tel: +44 3333 400 999\n        Email: support@aa.net.uk')
if mibBuilder.loadTexts: fbRunMib.setDescription('This is a MIB Module for monitoring Firebrick CPU usage.')
fbRunStatsTable = MibTable((1, 3, 6, 1, 4, 1, 24693, 100, 3, 1), )
if mibBuilder.loadTexts: fbRunStatsTable.setStatus('current')
if mibBuilder.loadTexts: fbRunStatsTable.setDescription('The table of runtime stats for this Firebrick')
fbRunStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 24693, 100, 3, 1, 1), ).setIndexNames((0, "FIREBRICK-RUNSTATS-MIB", "fbRunCore"))
if mibBuilder.loadTexts: fbRunStatsEntry.setStatus('current')
if mibBuilder.loadTexts: fbRunStatsEntry.setDescription('An entry in the CPU usage table')
fbRunCore = MibTableColumn((1, 3, 6, 1, 4, 1, 24693, 100, 3, 1, 1, 2), Integer32())
if mibBuilder.loadTexts: fbRunCore.setStatus('current')
if mibBuilder.loadTexts: fbRunCore.setDescription('The CPU core number covered by this table entry.\n\t The numbering starts at 1, so CPU0 (CORE) is 1 and CPU1 (NET) is 2.')
fbRunBuffers = MibTableColumn((1, 3, 6, 1, 4, 1, 24693, 100, 3, 1, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fbRunBuffers.setStatus('current')
if mibBuilder.loadTexts: fbRunBuffers.setDescription('The count of buffers which are currently free on this CPU core.')
mibBuilder.exportSymbols("FIREBRICK-RUNSTATS-MIB", PYSNMP_MODULE_ID=fbRunMib, fbRunStatsEntry=fbRunStatsEntry, fbRunStatsTable=fbRunStatsTable, fbRunBuffers=fbRunBuffers, fbRunMib=fbRunMib, fbRunCore=fbRunCore)
