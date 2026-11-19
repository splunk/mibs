#
# PySNMP MIB module CISCO-ATM-SWITCH-CUG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ATM-SWITCH-CUG-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("CISCO-ATM-SWITCH-CUG-MIB", Unsigned32=Unsigned32, PYSNMP_MODULE_ID=csCugMIB, csCugIfEntry=csCugIfEntry, csCugDenySameGroupFromUser=csCugDenySameGroupFromUser, csCugIndex=csCugIndex, csCugMIBConformance=csCugMIBConformance, csCugEntry=csCugEntry, csCugInterlockCodeRowStatus=csCugInterlockCodeRowStatus, csCugRowStatus=csCugRowStatus, csCugMIBCompliances=csCugMIBCompliances, csCugIfPermitUnknownCugsToUser=csCugIfPermitUnknownCugsToUser, csCugIfAccessEnable=csCugIfAccessEnable, csCugInterlockCodeAliasName=csCugInterlockCodeAliasName, csCugInterlockCodeEntry=csCugInterlockCodeEntry, CsCugInterlockCode=CsCugInterlockCode, csCugMIBGroups=csCugMIBGroups, csCugMIBGroup=csCugMIBGroup, csCugMIBObjects=csCugMIBObjects, csCugIfRowStatus=csCugIfRowStatus, csCugMIBCompliance=csCugMIBCompliance, csCugInterlockCode=csCugInterlockCode, csCugMIB=csCugMIB, csCugTable=csCugTable, csCugIfTable=csCugIfTable, csCugIfPermitUnknownCugsFromUser=csCugIfPermitUnknownCugsFromUser, csCugPreferential=csCugPreferential, csCugInterlockCodeTable=csCugInterlockCodeTable, csCugDenySameGroupToUser=csCugDenySameGroupToUser)
