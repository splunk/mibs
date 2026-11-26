#
# PySNMP MIB module CISCOSB-SCT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCOSB-SCT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:46 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
rlSctMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 203))
if mibBuilder.loadTexts: rlSctMib.setLastUpdated('201008161234Z')
if mibBuilder.loadTexts: rlSctMib.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: rlSctMib.setContactInfo('Postal: 170 West Tasman Drive\n        San Jose , CA 95134-1706\n        USA\n\n        \n        Website:  Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: rlSctMib.setDescription('The private MIB module definition for SCT MIB.')
rlSctCpuRateEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 203, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSctCpuRateEnabled.setStatus('current')
if mibBuilder.loadTexts: rlSctCpuRateEnabled.setDescription('Indication whether the counter CPU rate is enabled')
rlSctCpuRate = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 203, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSctCpuRate.setStatus('current')
if mibBuilder.loadTexts: rlSctCpuRate.setDescription('the amount of packets per second the CPU is handling.')
mibBuilder.exportSymbols("CISCOSB-SCT-MIB", rlSctCpuRate=rlSctCpuRate, rlSctCpuRateEnabled=rlSctCpuRateEnabled, rlSctMib=rlSctMib, PYSNMP_MODULE_ID=rlSctMib)
