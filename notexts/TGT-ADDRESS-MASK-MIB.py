#
# PySNMP MIB module TGT-ADDRESS-MASK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/audiocodes/TGT-ADDRESS-MASK-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:31:03 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
snmpTargetAddrEntry, = mibBuilder.importSymbols("SNMP-TARGET-MIB", "snmpTargetAddrEntry")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, ModuleIdentity, Counter32, MibIdentifier, enterprises, Integer32, Unsigned32, ObjectIdentity, Bits, NotificationType, iso, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "ModuleIdentity", "Counter32", "MibIdentifier", "enterprises", "Integer32", "Unsigned32", "ObjectIdentity", "Bits", "NotificationType", "iso", "Gauge32", "Counter64")
TAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TAddress", "TextualConvention", "DisplayString")
snmpResearch = MibIdentifier((1, 3, 6, 1, 4, 1, 99))
snmpResearchMIBs = MibIdentifier((1, 3, 6, 1, 4, 1, 99, 12))
tgtAddressMaskMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 99, 12, 36))
if mibBuilder.loadTexts: tgtAddressMaskMIB.setLastUpdated('9801160000Z')
if mibBuilder.loadTexts: tgtAddressMaskMIB.setOrganization('SNMP Research, Inc.')
tgtAddressMaskObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 99, 12, 36, 1))
tgtAddressMaskConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 99, 12, 36, 3))
tgtAddressMaskTable = MibTable((1, 3, 6, 1, 4, 1, 99, 12, 36, 1, 1), )
if mibBuilder.loadTexts: tgtAddressMaskTable.setStatus('current')
tgtAddressMaskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 99, 12, 36, 1, 1, 1), )
snmpTargetAddrEntry.registerAugmentions(("TGT-ADDRESS-MASK-MIB", "tgtAddressMaskEntry"))
tgtAddressMaskEntry.setIndexNames(*snmpTargetAddrEntry.getIndexNames())
if mibBuilder.loadTexts: tgtAddressMaskEntry.setStatus('current')
tgtAddressMask = MibTableColumn((1, 3, 6, 1, 4, 1, 99, 12, 36, 1, 1, 1, 1), TAddress().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tgtAddressMask.setStatus('current')
mibBuilder.exportSymbols("TGT-ADDRESS-MASK-MIB", tgtAddressMaskTable=tgtAddressMaskTable, tgtAddressMask=tgtAddressMask, PYSNMP_MODULE_ID=tgtAddressMaskMIB, snmpResearchMIBs=snmpResearchMIBs, tgtAddressMaskConformance=tgtAddressMaskConformance, tgtAddressMaskEntry=tgtAddressMaskEntry, snmpResearch=snmpResearch, tgtAddressMaskMIB=tgtAddressMaskMIB, tgtAddressMaskObjects=tgtAddressMaskObjects)
