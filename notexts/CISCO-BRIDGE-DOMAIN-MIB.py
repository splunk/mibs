#
# PySNMP MIB module CISCO-BRIDGE-DOMAIN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-BRIDGE-DOMAIN-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:44 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Gauge32, ModuleIdentity, Integer32, Bits, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Integer32", "Bits", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "Counter32")
DisplayString, StorageType, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "StorageType", "RowStatus", "TextualConvention", "TruthValue")
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
mibBuilder.exportSymbols("CISCO-BRIDGE-DOMAIN-MIB", ciscoBdMIBConformance=ciscoBdMIBConformance, ciscoBdNotificationPrefix=ciscoBdNotificationPrefix, ciscoBdMIBCompliances=ciscoBdMIBCompliances, cbdMemberOperState=cbdMemberOperState, PYSNMP_MODULE_ID=ciscoBridgeDomainMIB, CbdType=CbdType, cbdMemberType=cbdMemberType, cbdSystemInfo=cbdSystemInfo, cbdMemberInfo=cbdMemberInfo, cbdMembersConfigured=cbdMembersConfigured, cbdSystemInfoGroup=cbdSystemInfoGroup, ciscoBdMIBObjects=ciscoBdMIBObjects, ciscoBdMIBComplianceRev1=ciscoBdMIBComplianceRev1, cbdMemberStorageType=cbdMemberStorageType, cbdMembercMac=cbdMembercMac, cbdMemberInfoEntry=cbdMemberInfoEntry, cbdSIIndex=cbdSIIndex, cbdMemberInfoTable=cbdMemberInfoTable, cbdMemberInfoGroup=cbdMemberInfoGroup, cbdMemberAdminState=cbdMemberAdminState, ciscoBdMIBGroups=ciscoBdMIBGroups, cbdMemberSplitHorizonNum=cbdMemberSplitHorizonNum, ciscoBdMIBNotifications=ciscoBdMIBNotifications, cbdMemberSplitHorizon=cbdMemberSplitHorizon, cbdMemberStatus=cbdMemberStatus, ciscoBridgeDomainMIB=ciscoBridgeDomainMIB)
