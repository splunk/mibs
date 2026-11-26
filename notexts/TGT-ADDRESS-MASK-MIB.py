#
# PySNMP MIB module TGT-ADDRESS-MASK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/audiocodes/TGT-ADDRESS-MASK-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:05:35 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
snmpTargetAddrEntry, = mibBuilder.importSymbols("SNMP-TARGET-MIB", "snmpTargetAddrEntry")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
IpAddress, Unsigned32, Counter32, MibIdentifier, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, Counter64, Integer32, TimeTicks, ModuleIdentity, Bits, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Unsigned32", "Counter32", "MibIdentifier", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "Counter64", "Integer32", "TimeTicks", "ModuleIdentity", "Bits", "NotificationType", "Gauge32")
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
mibBuilder.exportSymbols("TGT-ADDRESS-MASK-MIB", snmpResearch=snmpResearch, tgtAddressMaskMIB=tgtAddressMaskMIB, tgtAddressMask=tgtAddressMask, tgtAddressMaskTable=tgtAddressMaskTable, tgtAddressMaskObjects=tgtAddressMaskObjects, tgtAddressMaskConformance=tgtAddressMaskConformance, PYSNMP_MODULE_ID=tgtAddressMaskMIB, snmpResearchMIBs=snmpResearchMIBs, tgtAddressMaskEntry=tgtAddressMaskEntry)
