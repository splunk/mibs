#
# PySNMP MIB module CISCO-ATM-SWITCH-CUG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ATM-SWITCH-CUG-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
csCugMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 89))
if mibBuilder.loadTexts: csCugMIB.setLastUpdated('9707070000Z')
if mibBuilder.loadTexts: csCugMIB.setOrganization('Cisco Systems, Inc.')
class CsCugInterlockCode(TextualConvention, OctetString):
    reference = 'Atm Forum Contribution 96-1347.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(24, 24), )
class Unsigned32(TextualConvention, Gauge32):
    status = 'current'

csCugMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 89, 1))
csCugInterlockCodeTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 1), )
if mibBuilder.loadTexts: csCugInterlockCodeTable.setStatus('current')
csCugInterlockCodeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 1, 1), ).setIndexNames((0, "CISCO-ATM-SWITCH-CUG-MIB", "csCugInterlockCode"))
if mibBuilder.loadTexts: csCugInterlockCodeEntry.setStatus('current')
csCugInterlockCode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 1, 1, 1), CsCugInterlockCode())
if mibBuilder.loadTexts: csCugInterlockCode.setStatus('current')
csCugInterlockCodeAliasName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 30))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csCugInterlockCodeAliasName.setStatus('current')
csCugInterlockCodeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csCugInterlockCodeRowStatus.setStatus('current')
csCugIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 2), )
if mibBuilder.loadTexts: csCugIfTable.setStatus('current')
csCugIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: csCugIfEntry.setStatus('current')
csCugIfAccessEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 2, 1, 1), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csCugIfAccessEnable.setStatus('current')
csCugIfPermitUnknownCugsToUser = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 2, 1, 2), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csCugIfPermitUnknownCugsToUser.setStatus('current')
csCugIfPermitUnknownCugsFromUser = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("deny", 1), ("permitPerCall", 2), ("permitPermanently", 3))).clone('deny')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csCugIfPermitUnknownCugsFromUser.setStatus('current')
csCugIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csCugIfRowStatus.setStatus('current')
csCugTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 3), )
if mibBuilder.loadTexts: csCugTable.setStatus('current')
csCugEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-ATM-SWITCH-CUG-MIB", "csCugInterlockCode"))
if mibBuilder.loadTexts: csCugEntry.setStatus('current')
csCugIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csCugIndex.setStatus('current')
csCugPreferential = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 3, 1, 2), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csCugPreferential.setStatus('current')
csCugDenySameGroupToUser = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 3, 1, 3), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csCugDenySameGroupToUser.setStatus('current')
csCugDenySameGroupFromUser = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 3, 1, 4), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csCugDenySameGroupFromUser.setStatus('current')
csCugRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 89, 1, 3, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csCugRowStatus.setStatus('current')
csCugMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 89, 3))
csCugMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 89, 3, 1))
csCugMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 89, 3, 2))
csCugMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 89, 3, 1, 1)).setObjects(("CISCO-ATM-SWITCH-CUG-MIB", "csCugMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csCugMIBCompliance = csCugMIBCompliance.setStatus('current')
csCugMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 89, 3, 2, 1)).setObjects(("CISCO-ATM-SWITCH-CUG-MIB", "csCugInterlockCodeAliasName"), ("CISCO-ATM-SWITCH-CUG-MIB", "csCugInterlockCodeRowStatus"), ("CISCO-ATM-SWITCH-CUG-MIB", "csCugIfAccessEnable"), ("CISCO-ATM-SWITCH-CUG-MIB", "csCugIfPermitUnknownCugsToUser"), ("CISCO-ATM-SWITCH-CUG-MIB", "csCugIfPermitUnknownCugsFromUser"), ("CISCO-ATM-SWITCH-CUG-MIB", "csCugIfRowStatus"), ("CISCO-ATM-SWITCH-CUG-MIB", "csCugIndex"), ("CISCO-ATM-SWITCH-CUG-MIB", "csCugPreferential"), ("CISCO-ATM-SWITCH-CUG-MIB", "csCugDenySameGroupToUser"), ("CISCO-ATM-SWITCH-CUG-MIB", "csCugDenySameGroupFromUser"), ("CISCO-ATM-SWITCH-CUG-MIB", "csCugRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csCugMIBGroup = csCugMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ATM-SWITCH-CUG-MIB", csCugInterlockCodeAliasName=csCugInterlockCodeAliasName, csCugDenySameGroupToUser=csCugDenySameGroupToUser, csCugIfPermitUnknownCugsToUser=csCugIfPermitUnknownCugsToUser, csCugInterlockCodeRowStatus=csCugInterlockCodeRowStatus, csCugTable=csCugTable, csCugMIBConformance=csCugMIBConformance, csCugInterlockCodeTable=csCugInterlockCodeTable, csCugEntry=csCugEntry, csCugInterlockCodeEntry=csCugInterlockCodeEntry, Unsigned32=Unsigned32, csCugMIBCompliances=csCugMIBCompliances, csCugRowStatus=csCugRowStatus, csCugMIBObjects=csCugMIBObjects, csCugIndex=csCugIndex, csCugIfTable=csCugIfTable, csCugPreferential=csCugPreferential, CsCugInterlockCode=CsCugInterlockCode, csCugMIBGroups=csCugMIBGroups, csCugIfEntry=csCugIfEntry, csCugDenySameGroupFromUser=csCugDenySameGroupFromUser, csCugInterlockCode=csCugInterlockCode, csCugMIB=csCugMIB, PYSNMP_MODULE_ID=csCugMIB, csCugMIBCompliance=csCugMIBCompliance, csCugIfPermitUnknownCugsFromUser=csCugIfPermitUnknownCugsFromUser, csCugMIBGroup=csCugMIBGroup, csCugIfRowStatus=csCugIfRowStatus, csCugIfAccessEnable=csCugIfAccessEnable)
