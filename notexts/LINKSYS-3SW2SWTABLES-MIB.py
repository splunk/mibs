#
# PySNMP MIB module LINKSYS-3SW2SWTABLES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/linksys/LINKSYS-3SW2SWTABLES-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:11:59 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("LINKSYS-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, ModuleIdentity, Bits, ObjectIdentity, iso, Unsigned32, Counter32, IpAddress, TimeTicks, MibIdentifier, NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "Bits", "ObjectIdentity", "iso", "Unsigned32", "Counter32", "IpAddress", "TimeTicks", "MibIdentifier", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rl3sw2swTables = ModuleIdentity((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 63))
rl3sw2swTables.setRevisions(('2007-01-02 00:00',))
if mibBuilder.loadTexts: rl3sw2swTables.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rl3sw2swTables.setOrganization(' Linksys LLC.')
rl3sw2swTablesPollingInterval = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 63, 1), Integer32().clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rl3sw2swTablesPollingInterval.setStatus('current')
mibBuilder.exportSymbols("LINKSYS-3SW2SWTABLES-MIB", rl3sw2swTablesPollingInterval=rl3sw2swTablesPollingInterval, PYSNMP_MODULE_ID=rl3sw2swTables, rl3sw2swTables=rl3sw2swTables)
