#
# PySNMP MIB module CISCOSB-SCT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCOSB-SCT-MIB
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
rlSctMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 203))
if mibBuilder.loadTexts: rlSctMib.setLastUpdated('201008161234Z')
if mibBuilder.loadTexts: rlSctMib.setOrganization('Cisco Systems, Inc.')
rlSctCpuRateEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 203, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSctCpuRateEnabled.setStatus('current')
rlSctCpuRate = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 203, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSctCpuRate.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-SCT-MIB", PYSNMP_MODULE_ID=rlSctMib, rlSctCpuRate=rlSctCpuRate, rlSctCpuRateEnabled=rlSctCpuRateEnabled, rlSctMib=rlSctMib)
