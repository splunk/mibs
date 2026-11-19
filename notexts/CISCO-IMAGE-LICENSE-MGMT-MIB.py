#
# PySNMP MIB module CISCO-IMAGE-LICENSE-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IMAGE-LICENSE-MGMT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoImageLicenseMgmtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 640))
ciscoImageLicenseMgmtMIB.setRevisions(('2007-10-16 00:00',))
if mibBuilder.loadTexts: ciscoImageLicenseMgmtMIB.setLastUpdated('200710160000Z')
if mibBuilder.loadTexts: ciscoImageLicenseMgmtMIB.setOrganization('Cisco Systems Inc.')
ciscoImageLicenseMgmtMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 640, 0))
ciscoImageLicenseMgmtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 640, 1))
ciscoImageLicenseMgmtMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 640, 2))
class BootImageLevel(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class LicenseNameList(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

cilmBootImageLevelTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1), )
if mibBuilder.loadTexts: cilmBootImageLevelTable.setStatus('current')
cilmBootImageLevelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmModuleName"))
if mibBuilder.loadTexts: cilmBootImageLevelEntry.setStatus('current')
cilmModuleName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1, 1, 1), SnmpAdminString())
if mibBuilder.loadTexts: cilmModuleName.setStatus('current')
cilmCurrentImageLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1, 1, 2), BootImageLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cilmCurrentImageLevel.setStatus('current')
cilmConfiguredBootImageLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1, 1, 3), BootImageLevel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cilmConfiguredBootImageLevel.setStatus('current')
cilmNextBootImageLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1, 1, 4), BootImageLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cilmNextBootImageLevel.setStatus('current')
cilmCurrentLicenseStoreIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cilmCurrentLicenseStoreIndex.setStatus('current')
cilmCurrentLicenseIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cilmCurrentLicenseIndex.setStatus('current')
cilmNextBootLicenseStoreIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cilmNextBootLicenseStoreIndex.setStatus('current')
cilmNextBootLicenseIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cilmNextBootLicenseIndex.setStatus('current')
cilmImageLevelToLicenseMapTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 2), )
if mibBuilder.loadTexts: cilmImageLevelToLicenseMapTable.setStatus('current')
cilmImageLevelToLicenseMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmModuleName"), (0, "CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmImageLicenseMapIndex"))
if mibBuilder.loadTexts: cilmImageLevelToLicenseMapEntry.setStatus('current')
cilmImageLicenseMapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cilmImageLicenseMapIndex.setStatus('current')
cilmImageLicenseImageLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 2, 1, 2), BootImageLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cilmImageLicenseImageLevel.setStatus('current')
cilmImageLicenseName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 2, 1, 3), LicenseNameList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cilmImageLicenseName.setStatus('current')
cilmImageLicensePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cilmImageLicensePriority.setStatus('current')
cilmEULAAccepted = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cilmEULAAccepted.setStatus('current')
cilmNotifCntl = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 4))
cilmImageLevelChangedNotif = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 4, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cilmImageLevelChangedNotif.setStatus('current')
cilmBootImageLevelChanged = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 640, 0, 1)).setObjects(("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmCurrentImageLevel"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmConfiguredBootImageLevel"))
if mibBuilder.loadTexts: cilmBootImageLevelChanged.setStatus('current')
cilmModuleCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 640, 2, 1))
cilmModuleGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 640, 2, 2))
cilmModuleCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 640, 2, 1, 1)).setObjects(("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmAdminGroup"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmNotifGroup"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmOperGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cilmModuleCompliance = cilmModuleCompliance.setStatus('current')
cilmAdminGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 640, 2, 2, 1)).setObjects(("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmCurrentImageLevel"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmConfiguredBootImageLevel"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmNextBootImageLevel"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmCurrentLicenseStoreIndex"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmCurrentLicenseIndex"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmNextBootLicenseStoreIndex"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmNextBootLicenseIndex"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmEULAAccepted"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmImageLevelChangedNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cilmAdminGroup = cilmAdminGroup.setStatus('current')
cilmOperGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 640, 2, 2, 2)).setObjects(("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmImageLicenseImageLevel"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmImageLicenseName"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmImageLicensePriority"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cilmOperGroup = cilmOperGroup.setStatus('current')
cilmNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 640, 2, 2, 3)).setObjects(("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmBootImageLevelChanged"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cilmNotifGroup = cilmNotifGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IMAGE-LICENSE-MGMT-MIB", cilmImageLicenseMapIndex=cilmImageLicenseMapIndex, cilmAdminGroup=cilmAdminGroup, cilmModuleCompliance=cilmModuleCompliance, cilmNextBootImageLevel=cilmNextBootImageLevel, cilmImageLevelToLicenseMapTable=cilmImageLevelToLicenseMapTable, ciscoImageLicenseMgmtMIB=ciscoImageLicenseMgmtMIB, cilmModuleGroups=cilmModuleGroups, cilmBootImageLevelChanged=cilmBootImageLevelChanged, cilmCurrentLicenseStoreIndex=cilmCurrentLicenseStoreIndex, cilmCurrentLicenseIndex=cilmCurrentLicenseIndex, ciscoImageLicenseMgmtMIBObjects=ciscoImageLicenseMgmtMIBObjects, ciscoImageLicenseMgmtMIBNotifs=ciscoImageLicenseMgmtMIBNotifs, cilmModuleCompliances=cilmModuleCompliances, cilmNextBootLicenseStoreIndex=cilmNextBootLicenseStoreIndex, cilmBootImageLevelTable=cilmBootImageLevelTable, cilmEULAAccepted=cilmEULAAccepted, BootImageLevel=BootImageLevel, cilmImageLicensePriority=cilmImageLicensePriority, cilmCurrentImageLevel=cilmCurrentImageLevel, cilmImageLevelToLicenseMapEntry=cilmImageLevelToLicenseMapEntry, cilmConfiguredBootImageLevel=cilmConfiguredBootImageLevel, cilmImageLevelChangedNotif=cilmImageLevelChangedNotif, cilmBootImageLevelEntry=cilmBootImageLevelEntry, cilmModuleName=cilmModuleName, cilmNotifCntl=cilmNotifCntl, cilmNotifGroup=cilmNotifGroup, ciscoImageLicenseMgmtMIBConform=ciscoImageLicenseMgmtMIBConform, LicenseNameList=LicenseNameList, PYSNMP_MODULE_ID=ciscoImageLicenseMgmtMIB, cilmImageLicenseImageLevel=cilmImageLicenseImageLevel, cilmNextBootLicenseIndex=cilmNextBootLicenseIndex, cilmOperGroup=cilmOperGroup, cilmImageLicenseName=cilmImageLicenseName)
