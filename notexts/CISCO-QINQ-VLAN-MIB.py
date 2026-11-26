#
# PySNMP MIB module CISCO-QINQ-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-QINQ-VLAN-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:01 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoQinqVlanMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 445))
ciscoQinqVlanMIB.setRevisions(('2004-11-29 00:00',))
if mibBuilder.loadTexts: ciscoQinqVlanMIB.setLastUpdated('200411290000Z')
if mibBuilder.loadTexts: ciscoQinqVlanMIB.setOrganization('Cisco Systems, Inc.')
ciscoQinqVlanMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 445, 0))
ciscoQinqVlanMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 445, 1))
ciscoQinqVlanMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 445, 2))
cqvTermination = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1))
cqvTranslation = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2))
class CqvVlanIdOrZero(TextualConvention, Unsigned32):
    reference = 'RFC-2674, Bridge MIB Extensions, August 1999, Q-BRIDGE-MIB, E. Bell.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4094)

class CqvEncapsulationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("isl", 1), ("dot1Q", 2))

cqvTerminationTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1, 1), )
if mibBuilder.loadTexts: cqvTerminationTable.setStatus('current')
cqvTerminationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-QINQ-VLAN-MIB", "cqvTerminationPeVlanId"), (0, "CISCO-QINQ-VLAN-MIB", "cqvTerminationCeVlanId"))
if mibBuilder.loadTexts: cqvTerminationEntry.setStatus('current')
cqvTerminationPeVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1, 1, 1, 1), VlanId())
if mibBuilder.loadTexts: cqvTerminationPeVlanId.setStatus('current')
cqvTerminationCeVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1, 1, 1, 2), VlanId())
if mibBuilder.loadTexts: cqvTerminationCeVlanId.setStatus('current')
cqvTerminationPeEncap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1, 1, 1, 3), CqvEncapsulationType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cqvTerminationPeEncap.setStatus('current')
cqvTerminationRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cqvTerminationRowStatus.setStatus('current')
cqvTranslationTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1), )
if mibBuilder.loadTexts: cqvTranslationTable.setStatus('current')
cqvTranslationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-QINQ-VLAN-MIB", "cqvTranslationInternalPeVlanId"), (0, "CISCO-QINQ-VLAN-MIB", "cqvTranslationInternalCeVlanId"))
if mibBuilder.loadTexts: cqvTranslationEntry.setStatus('current')
cqvTranslationInternalPeVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 1), CqvVlanIdOrZero())
if mibBuilder.loadTexts: cqvTranslationInternalPeVlanId.setStatus('current')
cqvTranslationInternalCeVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 2), CqvVlanIdOrZero())
if mibBuilder.loadTexts: cqvTranslationInternalCeVlanId.setStatus('current')
cqvTranslationTrunkPeVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 3), CqvVlanIdOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cqvTranslationTrunkPeVlanId.setStatus('current')
cqvTranslationTrunkCeVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 4), CqvVlanIdOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cqvTranslationTrunkCeVlanId.setStatus('current')
cqvTranslationType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("doubleToSingle", 1), ("doubleToDouble", 2), ("doubleToDoubleOutOfRange", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cqvTranslationType.setStatus('current')
cqvTranslationCosPBits = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("copyFromOuterTag", 1), ("copyFromInnerTag", 2))).clone('copyFromOuterTag')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cqvTranslationCosPBits.setStatus('current')
cqvTranslationRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cqvTranslationRowStatus.setStatus('current')
ciscoQinqVlanMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 445, 2, 1))
ciscoQinqVlanMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 445, 2, 2))
ciscoQinQVlanMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 445, 2, 1, 1)).setObjects(("CISCO-QINQ-VLAN-MIB", "ciscoQinqVlanTerminationGroup"), ("CISCO-QINQ-VLAN-MIB", "ciscoQinqVlanTranslationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQinQVlanMIBCompliance = ciscoQinQVlanMIBCompliance.setStatus('current')
ciscoQinqVlanTerminationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 445, 2, 2, 1)).setObjects(("CISCO-QINQ-VLAN-MIB", "cqvTerminationPeEncap"), ("CISCO-QINQ-VLAN-MIB", "cqvTerminationRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQinqVlanTerminationGroup = ciscoQinqVlanTerminationGroup.setStatus('current')
ciscoQinqVlanTranslationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 445, 2, 2, 2)).setObjects(("CISCO-QINQ-VLAN-MIB", "cqvTranslationTrunkPeVlanId"), ("CISCO-QINQ-VLAN-MIB", "cqvTranslationTrunkCeVlanId"), ("CISCO-QINQ-VLAN-MIB", "cqvTranslationType"), ("CISCO-QINQ-VLAN-MIB", "cqvTranslationCosPBits"), ("CISCO-QINQ-VLAN-MIB", "cqvTranslationRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQinqVlanTranslationGroup = ciscoQinqVlanTranslationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-QINQ-VLAN-MIB", ciscoQinQVlanMIBCompliance=ciscoQinQVlanMIBCompliance, cqvTerminationPeEncap=cqvTerminationPeEncap, cqvTranslationTable=cqvTranslationTable, cqvTranslationInternalCeVlanId=cqvTranslationInternalCeVlanId, cqvTerminationTable=cqvTerminationTable, ciscoQinqVlanMIBNotifs=ciscoQinqVlanMIBNotifs, cqvTranslation=cqvTranslation, CqvVlanIdOrZero=CqvVlanIdOrZero, cqvTerminationEntry=cqvTerminationEntry, cqvTranslationTrunkCeVlanId=cqvTranslationTrunkCeVlanId, ciscoQinqVlanMIBObjects=ciscoQinqVlanMIBObjects, ciscoQinqVlanMIBGroups=ciscoQinqVlanMIBGroups, cqvTranslationType=cqvTranslationType, cqvTranslationCosPBits=cqvTranslationCosPBits, cqvTerminationPeVlanId=cqvTerminationPeVlanId, cqvTranslationEntry=cqvTranslationEntry, ciscoQinqVlanMIB=ciscoQinqVlanMIB, cqvTermination=cqvTermination, CqvEncapsulationType=CqvEncapsulationType, cqvTranslationTrunkPeVlanId=cqvTranslationTrunkPeVlanId, ciscoQinqVlanTerminationGroup=ciscoQinqVlanTerminationGroup, cqvTranslationInternalPeVlanId=cqvTranslationInternalPeVlanId, ciscoQinqVlanMIBCompliances=ciscoQinqVlanMIBCompliances, cqvTerminationRowStatus=cqvTerminationRowStatus, ciscoQinqVlanTranslationGroup=ciscoQinqVlanTranslationGroup, cqvTerminationCeVlanId=cqvTerminationCeVlanId, PYSNMP_MODULE_ID=ciscoQinqVlanMIB, cqvTranslationRowStatus=cqvTranslationRowStatus, ciscoQinqVlanMIBConform=ciscoQinqVlanMIBConform)
