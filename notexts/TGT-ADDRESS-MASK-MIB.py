#
# PySNMP MIB module TGT-ADDRESS-MASK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/audiocodes/TGT-ADDRESS-MASK-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:33:48 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
snmpTargetAddrEntry, = mibBuilder.importSymbols("SNMP-TARGET-MIB", "snmpTargetAddrEntry")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Unsigned32, ObjectIdentity, TimeTicks, Bits, Gauge32, ModuleIdentity, MibIdentifier, iso, enterprises, Counter64, IpAddress, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ObjectIdentity", "TimeTicks", "Bits", "Gauge32", "ModuleIdentity", "MibIdentifier", "iso", "enterprises", "Counter64", "IpAddress", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32")
TextualConvention, TAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TAddress", "DisplayString")
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
mibBuilder.exportSymbols("TGT-ADDRESS-MASK-MIB", tgtAddressMaskMIB=tgtAddressMaskMIB, tgtAddressMaskEntry=tgtAddressMaskEntry, tgtAddressMaskTable=tgtAddressMaskTable, PYSNMP_MODULE_ID=tgtAddressMaskMIB, snmpResearchMIBs=snmpResearchMIBs, tgtAddressMaskConformance=tgtAddressMaskConformance, snmpResearch=snmpResearch, tgtAddressMaskObjects=tgtAddressMaskObjects, tgtAddressMask=tgtAddressMask)
