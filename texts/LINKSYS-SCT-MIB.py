#
# PySNMP MIB module LINKSYS-SCT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/linksys/LINKSYS-SCT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:12:02 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("LINKSYS-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Integer32, Gauge32, Unsigned32, NotificationType, Bits, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, MibIdentifier, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "Gauge32", "Unsigned32", "NotificationType", "Bits", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "MibIdentifier", "IpAddress", "ObjectIdentity")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
rlSctMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 203))
if mibBuilder.loadTexts: rlSctMib.setLastUpdated('201008161234Z')
if mibBuilder.loadTexts: rlSctMib.setOrganization('Linksys LLC.')
if mibBuilder.loadTexts: rlSctMib.setContactInfo('www.linksys.com/business/support')
if mibBuilder.loadTexts: rlSctMib.setDescription('The private MIB module definition for SCT MIB.')
rlSctCpuRateEnabled = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 203, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSctCpuRateEnabled.setStatus('current')
if mibBuilder.loadTexts: rlSctCpuRateEnabled.setDescription('Indication whether the counter CPU rate is enabled')
rlSctCpuRate = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 203, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSctCpuRate.setStatus('current')
if mibBuilder.loadTexts: rlSctCpuRate.setDescription('the amount of packets per second the CPU is handling.')
mibBuilder.exportSymbols("LINKSYS-SCT-MIB", PYSNMP_MODULE_ID=rlSctMib, rlSctCpuRate=rlSctCpuRate, rlSctCpuRateEnabled=rlSctCpuRateEnabled, rlSctMib=rlSctMib)
