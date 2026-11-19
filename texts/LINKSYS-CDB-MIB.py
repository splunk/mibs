#
# PySNMP MIB module LINKSYS-CDB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/linksys/LINKSYS-CDB-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:37:19 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("LINKSYS-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, MibIdentifier, Bits, Counter32, Gauge32, IpAddress, Unsigned32, ModuleIdentity, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "Bits", "Counter32", "Gauge32", "IpAddress", "Unsigned32", "ModuleIdentity", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "ObjectIdentity")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
rlCDB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 94))
rlCDB.setRevisions(('2007-01-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlCDB.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlCDB.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlCDB.setOrganization('\n                              Linksys LLC.')
if mibBuilder.loadTexts: rlCDB.setContactInfo('www.linksys.com/business/support')
if mibBuilder.loadTexts: rlCDB.setDescription('This private MIB module defines CDB private MIBs.')
rlStartupCDBChanged = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 94, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStartupCDBChanged.setStatus('current')
if mibBuilder.loadTexts: rlStartupCDBChanged.setDescription("Indicates whether the startup CDB has changed between the router's\n         last two reboots")
rlManualReboot = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 94, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlManualReboot.setStatus('current')
if mibBuilder.loadTexts: rlManualReboot.setDescription('Indicates whether the device was shutdown orderly before reboot or\n         not (i.e. power failure)')
mibBuilder.exportSymbols("LINKSYS-CDB-MIB", rlStartupCDBChanged=rlStartupCDBChanged, rlCDB=rlCDB, rlManualReboot=rlManualReboot, PYSNMP_MODULE_ID=rlCDB)
