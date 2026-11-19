#
# PySNMP MIB module CISCOSB-CDB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCOSB-CDB-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:07 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
rlCDB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 94))
rlCDB.setRevisions(('2007-01-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlCDB.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlCDB.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlCDB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: rlCDB.setContactInfo('Postal: 170 West Tasman Drive\n                San Jose , CA 95134-1706\n                USA\n\n                \n                Website:  Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: rlCDB.setDescription('This private MIB module defines CDB private MIBs.')
rlStartupCDBChanged = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 94, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStartupCDBChanged.setStatus('current')
if mibBuilder.loadTexts: rlStartupCDBChanged.setDescription("Indicates whether the startup CDB has changed between the router's\n         last two reboots")
rlManualReboot = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 94, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlManualReboot.setStatus('current')
if mibBuilder.loadTexts: rlManualReboot.setDescription('Indicates whether the device was shutdown orderly before reboot or\n         not (i.e. power failure)')
rlStartupCDBEmpty = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 94, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStartupCDBEmpty.setStatus('current')
if mibBuilder.loadTexts: rlStartupCDBEmpty.setDescription('Indicates whether the startup-cdb is empty, meaning: does not include\n         any user configuration.')
mibBuilder.exportSymbols("CISCOSB-CDB-MIB", rlCDB=rlCDB, PYSNMP_MODULE_ID=rlCDB, rlStartupCDBEmpty=rlStartupCDBEmpty, rlManualReboot=rlManualReboot, rlStartupCDBChanged=rlStartupCDBChanged)
