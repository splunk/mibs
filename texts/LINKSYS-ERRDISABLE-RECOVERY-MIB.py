#
# PySNMP MIB module LINKSYS-ERRDISABLE-RECOVERY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/linksys/LINKSYS-ERRDISABLE-RECOVERY-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:37:19 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
rnd, = mibBuilder.importSymbols("LINKSYS-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, MibIdentifier, Bits, Counter32, Gauge32, IpAddress, Unsigned32, ModuleIdentity, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "Bits", "Counter32", "Gauge32", "IpAddress", "Unsigned32", "ModuleIdentity", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "ObjectIdentity")
TruthValue, DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention", "RowStatus")
rlErrdisableRecovery = ModuleIdentity((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 128))
rlErrdisableRecovery.setRevisions(('2007-11-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlErrdisableRecovery.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: rlErrdisableRecovery.setLastUpdated('200711070000Z')
if mibBuilder.loadTexts: rlErrdisableRecovery.setOrganization('Linksys LLC.')
if mibBuilder.loadTexts: rlErrdisableRecovery.setContactInfo('www.linksys.com/business/support')
if mibBuilder.loadTexts: rlErrdisableRecovery.setDescription('The private MIB module definition for Errdisable Recovery MIB.')
class RlErrdisableRecoveryCauseType(TextualConvention, Integer32):
    description = 'Errdisable Recovery Cause Type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("loopback-detection", 1), ("port-security", 2), ("dot1x-src-address", 3), ("acl-deny", 4), ("stp-bpdu-guard", 5), ("stp-loopback-guard", 6), ("pcb-overheat", 7), ("udld", 8))

rlErrdisableRecoveryInterval = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 128, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 86400))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlErrdisableRecoveryInterval.setStatus('current')
if mibBuilder.loadTexts: rlErrdisableRecoveryInterval.setDescription('Timeout interval in seconds for automatic activation of an interface after shutdown.')
rlErrdisableRecoveryCauseTable = MibTable((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 128, 2), )
if mibBuilder.loadTexts: rlErrdisableRecoveryCauseTable.setStatus('current')
if mibBuilder.loadTexts: rlErrdisableRecoveryCauseTable.setDescription('The table is used to enable or disable auto-recovery for specific\n       application causes port suspend. The table includes entries for all applications.')
rlErrdisableRecoveryCauseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 128, 2, 1), ).setIndexNames((0, "LINKSYS-ERRDISABLE-RECOVERY-MIB", "rlErrdisableRecoveryCause"))
if mibBuilder.loadTexts: rlErrdisableRecoveryCauseEntry.setStatus('current')
if mibBuilder.loadTexts: rlErrdisableRecoveryCauseEntry.setDescription('An entry (conceptual row) in the rlErrdisableRecoveryCauseEntry.')
rlErrdisableRecoveryCause = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 128, 2, 1, 1), RlErrdisableRecoveryCauseType())
if mibBuilder.loadTexts: rlErrdisableRecoveryCause.setStatus('current')
if mibBuilder.loadTexts: rlErrdisableRecoveryCause.setDescription('Type of recovery cause.')
rlErrdisableRecoveryEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 128, 2, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlErrdisableRecoveryEnable.setStatus('current')
if mibBuilder.loadTexts: rlErrdisableRecoveryEnable.setDescription('Enable/Disable automatic recovery.')
rlErrdisableRecoveryIfTable = MibTable((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 128, 3), )
if mibBuilder.loadTexts: rlErrdisableRecoveryIfTable.setStatus('current')
if mibBuilder.loadTexts: rlErrdisableRecoveryIfTable.setDescription('The table is used for show the reason of shutdown the port in errdisable state.\n       The table includes only suspended interfaces.')
rlErrdisableRecoveryIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 128, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlErrdisableRecoveryIfEntry.setStatus('current')
if mibBuilder.loadTexts: rlErrdisableRecoveryIfEntry.setDescription('An entry (conceptual row) in the rlErrdisableRecoveryIfEntry.')
rlErrdisableRecoveryIfReason = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 128, 3, 1, 1), RlErrdisableRecoveryCauseType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlErrdisableRecoveryIfReason.setStatus('current')
if mibBuilder.loadTexts: rlErrdisableRecoveryIfReason.setDescription(' The reason of shutdown the port in errdisable state.')
rlErrdisableRecoveryIfEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 128, 3, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlErrdisableRecoveryIfEnable.setStatus('current')
if mibBuilder.loadTexts: rlErrdisableRecoveryIfEnable.setDescription('Enable/Disable automatic recovery status.')
mibBuilder.exportSymbols("LINKSYS-ERRDISABLE-RECOVERY-MIB", RlErrdisableRecoveryCauseType=RlErrdisableRecoveryCauseType, rlErrdisableRecoveryCause=rlErrdisableRecoveryCause, rlErrdisableRecoveryIfTable=rlErrdisableRecoveryIfTable, PYSNMP_MODULE_ID=rlErrdisableRecovery, rlErrdisableRecoveryCauseEntry=rlErrdisableRecoveryCauseEntry, rlErrdisableRecoveryIfEntry=rlErrdisableRecoveryIfEntry, rlErrdisableRecoveryIfReason=rlErrdisableRecoveryIfReason, rlErrdisableRecoveryInterval=rlErrdisableRecoveryInterval, rlErrdisableRecovery=rlErrdisableRecovery, rlErrdisableRecoveryIfEnable=rlErrdisableRecoveryIfEnable, rlErrdisableRecoveryCauseTable=rlErrdisableRecoveryCauseTable, rlErrdisableRecoveryEnable=rlErrdisableRecoveryEnable)
