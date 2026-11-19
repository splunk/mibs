#
# PySNMP MIB module CISCO-IETF-VPLS-BGP-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IETF-VPLS-BGP-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
cvplsPwBindIndex, cvplsConfigIndex = mibBuilder.importSymbols("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsPwBindIndex", "cvplsConfigIndex")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
TextualConvention, StorageType, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "StorageType", "RowStatus", "DisplayString")
ciscoIetfVplsBgpExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 140))
ciscoIetfVplsBgpExtMIB.setRevisions(('2008-10-24 00:00',))
if mibBuilder.loadTexts: ciscoIetfVplsBgpExtMIB.setLastUpdated('200810240000Z')
if mibBuilder.loadTexts: ciscoIetfVplsBgpExtMIB.setOrganization('Cisco Systems, Inc.')
class CiVplsBgpExtRouteDistinguisher(TextualConvention, OctetString):
    reference = '[RFC4364]'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class CiVplsBgpExtRouteTarget(TextualConvention, OctetString):
    reference = '[RFC4364]'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class CiVplsBgpExtRouteTargetType(TextualConvention, Integer32):
    reference = '[RFC 4364]'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("import", 1), ("export", 2), ("both", 3))

class CiVplsBgpExtVEID(TextualConvention, Unsigned32):
    status = 'current'

ciscoIetfVplsBgpExtMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 140, 0))
ciscoIetfVplsBgpExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 140, 1))
ciscoIetfVplsBgpExtMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 140, 2))
ciVplsBgpExtConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 1), )
if mibBuilder.loadTexts: ciVplsBgpExtConfigTable.setStatus('current')
ciVplsBgpExtConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 1, 1), ).setIndexNames((0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex"))
if mibBuilder.loadTexts: ciVplsBgpExtConfigEntry.setStatus('current')
ciVplsBgpExtConfigRouteDistinguisher = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 1, 1, 1), CiVplsBgpExtRouteDistinguisher()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciVplsBgpExtConfigRouteDistinguisher.setStatus('current')
ciVplsBgpExtConfigVERangeSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciVplsBgpExtConfigVERangeSize.setStatus('current')
civplsBgpExtRTTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 2), )
if mibBuilder.loadTexts: civplsBgpExtRTTable.setStatus('current')
civplsBgpExtRTEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 2, 1), ).setIndexNames((0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex"), (0, "CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtRTType"), (0, "CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtRT"))
if mibBuilder.loadTexts: civplsBgpExtRTEntry.setStatus('current')
ciVplsBgpExtRTType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 2, 1, 1), CiVplsBgpExtRouteTargetType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciVplsBgpExtRTType.setStatus('current')
ciVplsBgpExtRT = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 2, 1, 2), CiVplsBgpExtRouteTarget().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciVplsBgpExtRT.setStatus('current')
ciVplsBgpExtRTStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 2, 1, 3), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciVplsBgpExtRTStorageType.setStatus('current')
ciVplsBgpExtRTRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciVplsBgpExtRTRowStatus.setStatus('current')
ciVplsBgpExtVETable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 3), )
if mibBuilder.loadTexts: ciVplsBgpExtVETable.setStatus('current')
ciVplsBgpExtVEEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 3, 1), ).setIndexNames((0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex"), (0, "CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtVEId"))
if mibBuilder.loadTexts: ciVplsBgpExtVEEntry.setStatus('current')
ciVplsBgpExtVEId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 3, 1, 1), CiVplsBgpExtVEID())
if mibBuilder.loadTexts: ciVplsBgpExtVEId.setStatus('current')
ciVplsBgpExtVEName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 3, 1, 2), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciVplsBgpExtVEName.setStatus('current')
ciVplsBgpExtVEPreference = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 3, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciVplsBgpExtVEPreference.setStatus('current')
ciVplsBgpExtVEStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 3, 1, 5), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciVplsBgpExtVEStorageType.setStatus('current')
ciVplsBgpExtVERowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciVplsBgpExtVERowStatus.setStatus('current')
ciVplsBgpExtPwBindTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 4), )
if mibBuilder.loadTexts: ciVplsBgpExtPwBindTable.setStatus('current')
ciVplsBgpExtPwBindEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 4, 1), ).setIndexNames((0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex"), (0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsPwBindIndex"))
if mibBuilder.loadTexts: ciVplsBgpExtPwBindEntry.setStatus('current')
ciVplsBgpExtPwBindLocalVEId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 4, 1, 1), CiVplsBgpExtVEID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciVplsBgpExtPwBindLocalVEId.setStatus('current')
ciVplsBgpExtPwBindRemoteVEId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 4, 1, 2), CiVplsBgpExtVEID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciVplsBgpExtPwBindRemoteVEId.setStatus('current')
ciscoIetfVplsBgpExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 140, 2, 1))
ciscoIetfVplsBgpExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 140, 2, 2))
ciscoIetfVplsBgpExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 140, 2, 1, 1)).setObjects(("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtConfigGroup"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtRTGroup"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtVEGroup"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtPwBindGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfVplsBgpExtMIBCompliance = ciscoIetfVplsBgpExtMIBCompliance.setStatus('current')
ciVplsBgpExtConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 140, 2, 2, 1)).setObjects(("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtConfigRouteDistinguisher"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtConfigVERangeSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciVplsBgpExtConfigGroup = ciVplsBgpExtConfigGroup.setStatus('current')
ciVplsBgpExtRTGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 140, 2, 2, 2)).setObjects(("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtRTType"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtRT"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtRTStorageType"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtRTRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciVplsBgpExtRTGroup = ciVplsBgpExtRTGroup.setStatus('current')
ciVplsBgpExtVEGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 140, 2, 2, 3)).setObjects(("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtVEName"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtVEPreference"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtVERowStatus"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtVEStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciVplsBgpExtVEGroup = ciVplsBgpExtVEGroup.setStatus('current')
ciVplsBgpExtPwBindGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 140, 2, 2, 4)).setObjects(("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtPwBindLocalVEId"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtPwBindRemoteVEId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciVplsBgpExtPwBindGroup = ciVplsBgpExtPwBindGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-VPLS-BGP-EXT-MIB", ciVplsBgpExtRT=ciVplsBgpExtRT, ciVplsBgpExtConfigEntry=ciVplsBgpExtConfigEntry, ciVplsBgpExtPwBindEntry=ciVplsBgpExtPwBindEntry, ciVplsBgpExtRTRowStatus=ciVplsBgpExtRTRowStatus, CiVplsBgpExtRouteTargetType=CiVplsBgpExtRouteTargetType, ciVplsBgpExtVEStorageType=ciVplsBgpExtVEStorageType, ciVplsBgpExtConfigVERangeSize=ciVplsBgpExtConfigVERangeSize, ciVplsBgpExtRTType=ciVplsBgpExtRTType, ciVplsBgpExtVEGroup=ciVplsBgpExtVEGroup, PYSNMP_MODULE_ID=ciscoIetfVplsBgpExtMIB, ciVplsBgpExtVEEntry=ciVplsBgpExtVEEntry, CiVplsBgpExtRouteTarget=CiVplsBgpExtRouteTarget, ciVplsBgpExtConfigGroup=ciVplsBgpExtConfigGroup, ciVplsBgpExtConfigTable=ciVplsBgpExtConfigTable, ciVplsBgpExtConfigRouteDistinguisher=ciVplsBgpExtConfigRouteDistinguisher, ciscoIetfVplsBgpExtMIBCompliance=ciscoIetfVplsBgpExtMIBCompliance, ciscoIetfVplsBgpExtMIBNotifs=ciscoIetfVplsBgpExtMIBNotifs, ciscoIetfVplsBgpExtMIBConform=ciscoIetfVplsBgpExtMIBConform, civplsBgpExtRTTable=civplsBgpExtRTTable, ciVplsBgpExtVEName=ciVplsBgpExtVEName, ciscoIetfVplsBgpExtMIBGroups=ciscoIetfVplsBgpExtMIBGroups, ciVplsBgpExtRTStorageType=ciVplsBgpExtRTStorageType, ciVplsBgpExtPwBindRemoteVEId=ciVplsBgpExtPwBindRemoteVEId, ciVplsBgpExtRTGroup=ciVplsBgpExtRTGroup, ciVplsBgpExtPwBindLocalVEId=ciVplsBgpExtPwBindLocalVEId, civplsBgpExtRTEntry=civplsBgpExtRTEntry, ciVplsBgpExtVETable=ciVplsBgpExtVETable, ciVplsBgpExtPwBindGroup=ciVplsBgpExtPwBindGroup, ciVplsBgpExtVEId=ciVplsBgpExtVEId, ciscoIetfVplsBgpExtMIBCompliances=ciscoIetfVplsBgpExtMIBCompliances, ciVplsBgpExtVERowStatus=ciVplsBgpExtVERowStatus, ciVplsBgpExtPwBindTable=ciVplsBgpExtPwBindTable, ciscoIetfVplsBgpExtMIBObjects=ciscoIetfVplsBgpExtMIBObjects, ciVplsBgpExtVEPreference=ciVplsBgpExtVEPreference, ciscoIetfVplsBgpExtMIB=ciscoIetfVplsBgpExtMIB, CiVplsBgpExtRouteDistinguisher=CiVplsBgpExtRouteDistinguisher, CiVplsBgpExtVEID=CiVplsBgpExtVEID)
