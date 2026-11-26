#
# PySNMP MIB module CISCOSB-CDB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCOSB-CDB-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
rlCDB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 94))
rlCDB.setRevisions(('2007-01-02 00:00',))
if mibBuilder.loadTexts: rlCDB.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlCDB.setOrganization('Cisco Systems, Inc.')
rlStartupCDBChanged = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 94, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStartupCDBChanged.setStatus('current')
rlManualReboot = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 94, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlManualReboot.setStatus('current')
rlStartupCDBEmpty = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 94, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStartupCDBEmpty.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-CDB-MIB", rlStartupCDBEmpty=rlStartupCDBEmpty, PYSNMP_MODULE_ID=rlCDB, rlManualReboot=rlManualReboot, rlCDB=rlCDB, rlStartupCDBChanged=rlStartupCDBChanged)
