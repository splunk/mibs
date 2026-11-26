#
# PySNMP MIB module CISCO-BRIDGE-DOMAIN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-BRIDGE-DOMAIN-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
StorageType, TruthValue, TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "StorageType", "TruthValue", "TextualConvention", "DisplayString", "RowStatus")
ciscoBridgeDomainMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 642))
ciscoBridgeDomainMIB.setRevisions(('2007-12-29 00:00', '2007-12-04 00:00',))
if mibBuilder.loadTexts: ciscoBridgeDomainMIB.setLastUpdated('200712290000Z')
if mibBuilder.loadTexts: ciscoBridgeDomainMIB.setOrganization('Cisco Systems, Inc.')
ciscoBdMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 642, 0))
ciscoBdMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 642, 1))
ciscoBdMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 642, 2))
cbdSystemInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 642, 1, 1))
cbdMemberInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 642, 1, 2))
class CbdType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("ether", 2), ("atmVc", 3), ("frVc", 4))

cbdMembersConfigured = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 642, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbdMembersConfigured.setStatus('current')
cbdMemberInfoTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 642, 1, 2, 1), )
if mibBuilder.loadTexts: cbdMemberInfoTable.setStatus('current')
cbdMemberInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 642, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-BRIDGE-DOMAIN-MIB", "cbdSIIndex"))
if mibBuilder.loadTexts: cbdMemberInfoEntry.setStatus('current')
cbdSIIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 642, 1, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cbdSIIndex.setStatus('current')
cbdMemberType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 642, 1, 2, 1, 1, 2), CbdType().clone('other')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cbdMemberType.setStatus('current')
cbdMemberOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 642, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("up", 2), ("down", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbdMemberOperState.setStatus('current')
cbdMemberAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 642, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("up", 2), ("down", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cbdMemberAdminState.setStatus('current')
cbdMemberSplitHorizon = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 642, 1, 2, 1, 1, 5), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cbdMemberSplitHorizon.setStatus('current')
cbdMemberSplitHorizonNum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 642, 1, 2, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cbdMemberSplitHorizonNum.setStatus('current')
cbdMemberStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 642, 1, 2, 1, 1, 7), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cbdMemberStorageType.setStatus('current')
cbdMemberStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 642, 1, 2, 1, 1, 8), RowStatus().clone('active')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cbdMemberStatus.setStatus('current')
cbdMembercMac = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 642, 1, 2, 1, 1, 9), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cbdMembercMac.setStatus('current')
ciscoBdNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 642, 0, 0))
ciscoBdMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 642, 2, 1))
ciscoBdMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 642, 2, 2))
ciscoBdMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 642, 2, 1, 1)).setObjects(("CISCO-BRIDGE-DOMAIN-MIB", "cbdSystemInfoGroup"), ("CISCO-BRIDGE-DOMAIN-MIB", "cbdMemberInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBdMIBComplianceRev1 = ciscoBdMIBComplianceRev1.setStatus('current')
cbdSystemInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 642, 2, 2, 1)).setObjects(("CISCO-BRIDGE-DOMAIN-MIB", "cbdMembersConfigured"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbdSystemInfoGroup = cbdSystemInfoGroup.setStatus('current')
cbdMemberInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 642, 2, 2, 2)).setObjects(("CISCO-BRIDGE-DOMAIN-MIB", "cbdMemberType"), ("CISCO-BRIDGE-DOMAIN-MIB", "cbdMemberOperState"), ("CISCO-BRIDGE-DOMAIN-MIB", "cbdMemberAdminState"), ("CISCO-BRIDGE-DOMAIN-MIB", "cbdMemberSplitHorizon"), ("CISCO-BRIDGE-DOMAIN-MIB", "cbdMemberSplitHorizonNum"), ("CISCO-BRIDGE-DOMAIN-MIB", "cbdMemberStorageType"), ("CISCO-BRIDGE-DOMAIN-MIB", "cbdMemberStatus"), ("CISCO-BRIDGE-DOMAIN-MIB", "cbdMembercMac"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbdMemberInfoGroup = cbdMemberInfoGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-BRIDGE-DOMAIN-MIB", cbdMemberSplitHorizonNum=cbdMemberSplitHorizonNum, cbdMemberInfoTable=cbdMemberInfoTable, cbdMemberInfo=cbdMemberInfo, ciscoBdMIBCompliances=ciscoBdMIBCompliances, ciscoBdMIBComplianceRev1=ciscoBdMIBComplianceRev1, cbdSystemInfo=cbdSystemInfo, cbdMemberOperState=cbdMemberOperState, cbdMemberInfoEntry=cbdMemberInfoEntry, cbdMemberType=cbdMemberType, ciscoBridgeDomainMIB=ciscoBridgeDomainMIB, ciscoBdMIBNotifications=ciscoBdMIBNotifications, cbdSystemInfoGroup=cbdSystemInfoGroup, PYSNMP_MODULE_ID=ciscoBridgeDomainMIB, cbdMemberInfoGroup=cbdMemberInfoGroup, cbdMembercMac=cbdMembercMac, cbdMemberStorageType=cbdMemberStorageType, ciscoBdMIBGroups=ciscoBdMIBGroups, ciscoBdMIBObjects=ciscoBdMIBObjects, ciscoBdNotificationPrefix=ciscoBdNotificationPrefix, cbdMembersConfigured=cbdMembersConfigured, CbdType=CbdType, cbdMemberStatus=cbdMemberStatus, cbdMemberAdminState=cbdMemberAdminState, cbdMemberSplitHorizon=cbdMemberSplitHorizon, ciscoBdMIBConformance=ciscoBdMIBConformance, cbdSIIndex=cbdSIIndex)
