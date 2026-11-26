#
# PySNMP MIB module CISCOSB-ERRDISABLE-RECOVERY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCOSB-ERRDISABLE-RECOVERY-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:57 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
rlErrdisableRecovery = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128))
rlErrdisableRecovery.setRevisions(('2007-11-07 00:00',))
if mibBuilder.loadTexts: rlErrdisableRecovery.setLastUpdated('200711070000Z')
if mibBuilder.loadTexts: rlErrdisableRecovery.setOrganization('Cisco Systems, Inc.')
class RlErrdisableRecoveryCauseType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("loopback-detection", 1), ("port-security", 2), ("dot1x-src-address", 3), ("acl-deny", 4), ("stp-bpdu-guard", 5), ("stp-loopback-guard", 6), ("pcb-overheat", 7), ("udld", 8), ("storm-control", 9), ("link-flapping", 10))

rlErrdisableRecoveryInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 86400))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlErrdisableRecoveryInterval.setStatus('current')
rlErrdisableRecoveryCauseTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 2), )
if mibBuilder.loadTexts: rlErrdisableRecoveryCauseTable.setStatus('current')
rlErrdisableRecoveryCauseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 2, 1), ).setIndexNames((0, "CISCOSB-ERRDISABLE-RECOVERY-MIB", "rlErrdisableRecoveryCause"))
if mibBuilder.loadTexts: rlErrdisableRecoveryCauseEntry.setStatus('current')
rlErrdisableRecoveryCause = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 2, 1, 1), RlErrdisableRecoveryCauseType())
if mibBuilder.loadTexts: rlErrdisableRecoveryCause.setStatus('current')
rlErrdisableRecoveryEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 2, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlErrdisableRecoveryEnable.setStatus('current')
rlErrdisableRecoveryIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 3), )
if mibBuilder.loadTexts: rlErrdisableRecoveryIfTable.setStatus('current')
rlErrdisableRecoveryIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlErrdisableRecoveryIfEntry.setStatus('current')
rlErrdisableRecoveryIfReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 3, 1, 1), RlErrdisableRecoveryCauseType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlErrdisableRecoveryIfReason.setStatus('current')
rlErrdisableRecoveryIfEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 3, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlErrdisableRecoveryIfEnable.setStatus('current')
rlErrdisableRecoveryIfTimeToRecover = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 3, 1, 3), Integer32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlErrdisableRecoveryIfTimeToRecover.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-ERRDISABLE-RECOVERY-MIB", rlErrdisableRecoveryInterval=rlErrdisableRecoveryInterval, PYSNMP_MODULE_ID=rlErrdisableRecovery, rlErrdisableRecoveryCauseEntry=rlErrdisableRecoveryCauseEntry, rlErrdisableRecoveryCauseTable=rlErrdisableRecoveryCauseTable, rlErrdisableRecoveryCause=rlErrdisableRecoveryCause, rlErrdisableRecoveryIfTable=rlErrdisableRecoveryIfTable, rlErrdisableRecovery=rlErrdisableRecovery, rlErrdisableRecoveryIfReason=rlErrdisableRecoveryIfReason, rlErrdisableRecoveryIfEnable=rlErrdisableRecoveryIfEnable, rlErrdisableRecoveryIfEntry=rlErrdisableRecoveryIfEntry, rlErrdisableRecoveryEnable=rlErrdisableRecoveryEnable, RlErrdisableRecoveryCauseType=RlErrdisableRecoveryCauseType, rlErrdisableRecoveryIfTimeToRecover=rlErrdisableRecoveryIfTimeToRecover)
