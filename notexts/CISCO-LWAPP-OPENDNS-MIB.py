#
# PySNMP MIB module CISCO-LWAPP-OPENDNS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-LWAPP-OPENDNS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:24 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
cLWlanIndex, = mibBuilder.importSymbols("CISCO-LWAPP-WLAN-MIB", "cLWlanIndex")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
TextualConvention, DisplayString, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue", "RowStatus")
ciscoLwappOpendnsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 837))
ciscoLwappOpendnsMIB.setRevisions(('2018-07-03 00:00', '2017-02-10 00:00',))
if mibBuilder.loadTexts: ciscoLwappOpendnsMIB.setLastUpdated('201807030000Z')
if mibBuilder.loadTexts: ciscoLwappOpendnsMIB.setOrganization('Cisco Systems Inc.')
ciscoLwappOpendnsMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 837, 0))
ciscoLwappOpendnsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 837, 1))
ciscoLwappOpendnsMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 837, 2))
ciscoLwappOpendnsTag = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1))
ciscoLwappOpendnsConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 2))
claOpendnsEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 2, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: claOpendnsEnable.setStatus('current')
claOpendnsForceEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 2, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: claOpendnsForceEnable.setStatus('current')
claOpendnsApiToken = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 2, 3), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: claOpendnsApiToken.setStatus('current')
claOpendnsProfileTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1, 1), )
if mibBuilder.loadTexts: claOpendnsProfileTable.setStatus('current')
claOpendnsProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-OPENDNS-MIB", "claOpendnsProfileName"))
if mibBuilder.loadTexts: claOpendnsProfileEntry.setStatus('current')
claOpendnsProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1, 1, 1, 1), SnmpAdminString())
if mibBuilder.loadTexts: claOpendnsProfileName.setStatus('current')
claOpendnsProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: claOpendnsProfileRowStatus.setStatus('current')
claOpendnsProfileStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("notInuse", 1), ("inProgress", 2), ("success", 3), ("failed", 4), ("inuse", 5))).clone('notInuse')).setMaxAccess("readonly")
if mibBuilder.loadTexts: claOpendnsProfileStatus.setStatus('current')
claOpendnsProfileIdentity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: claOpendnsProfileIdentity.setStatus('current')
claOpendnsWlanTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1, 2), )
if mibBuilder.loadTexts: claOpendnsWlanTable.setStatus('current')
claOpendnsWlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"))
if mibBuilder.loadTexts: claOpendnsWlanEntry.setStatus('current')
claOpendnsWlanProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1, 2, 1, 1), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: claOpendnsWlanProfileName.setStatus('current')
claOpendnsWlanMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ignore", 1), ("force", 2), ("copy", 3))).clone('force')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: claOpendnsWlanMode.setStatus('current')
claOpendnsWlanProfileStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1, 2, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: claOpendnsWlanProfileStatus.setStatus('current')
claOpendnsWlanDhcpOpt6 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 837, 1, 1, 2, 1, 4), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: claOpendnsWlanDhcpOpt6.setStatus('current')
ciscoLwappOpendnsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 837, 2, 1))
ciscoLwappOpendnsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 837, 2, 2))
ciscoLwappOpendnsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 837, 2, 1, 1)).setObjects(("CISCO-LWAPP-OPENDNS-MIB", "ciscoLwappOpendnsTagGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappOpendnsMIBCompliance = ciscoLwappOpendnsMIBCompliance.setStatus('deprecated')
ciscoLwappOpendnsMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 837, 2, 1, 2)).setObjects(("CISCO-LWAPP-OPENDNS-MIB", "ciscoLwappOpendnsTagGroup"), ("CISCO-LWAPP-OPENDNS-MIB", "ciscoLwappOpendnsConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappOpendnsMIBComplianceRev1 = ciscoLwappOpendnsMIBComplianceRev1.setStatus('deprecated')
ciscoLwappOpendnsMIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 837, 2, 1, 3)).setObjects(("CISCO-LWAPP-OPENDNS-MIB", "ciscoLwappOpendnsTagGroup"), ("CISCO-LWAPP-OPENDNS-MIB", "ciscoLwappOpendnsConfigGroup"), ("CISCO-LWAPP-OPENDNS-MIB", "ciscoLwappOpendnsTagGroupVer2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappOpendnsMIBComplianceRev2 = ciscoLwappOpendnsMIBComplianceRev2.setStatus('current')
ciscoLwappOpendnsTagGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 837, 2, 2, 1)).setObjects(("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsProfileRowStatus"), ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsWlanProfileName"), ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsWlanMode"), ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsWlanProfileStatus"), ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsProfileStatus"), ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsProfileIdentity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappOpendnsTagGroup = ciscoLwappOpendnsTagGroup.setStatus('deprecated')
ciscoLwappOpendnsConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 837, 2, 2, 2)).setObjects(("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsEnable"), ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsForceEnable"), ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsApiToken"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappOpendnsConfigGroup = ciscoLwappOpendnsConfigGroup.setStatus('current')
ciscoLwappOpendnsTagGroupVer2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 837, 2, 2, 3)).setObjects(("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsProfileRowStatus"), ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsWlanProfileName"), ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsWlanMode"), ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsWlanProfileStatus"), ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsProfileStatus"), ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsProfileIdentity"), ("CISCO-LWAPP-OPENDNS-MIB", "claOpendnsWlanDhcpOpt6"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappOpendnsTagGroupVer2 = ciscoLwappOpendnsTagGroupVer2.setStatus('current')
mibBuilder.exportSymbols("CISCO-LWAPP-OPENDNS-MIB", claOpendnsWlanEntry=claOpendnsWlanEntry, ciscoLwappOpendnsMIBNotifs=ciscoLwappOpendnsMIBNotifs, ciscoLwappOpendnsMIBGroups=ciscoLwappOpendnsMIBGroups, ciscoLwappOpendnsConfig=ciscoLwappOpendnsConfig, claOpendnsProfileName=claOpendnsProfileName, ciscoLwappOpendnsMIBCompliance=ciscoLwappOpendnsMIBCompliance, claOpendnsProfileTable=claOpendnsProfileTable, ciscoLwappOpendnsMIBConform=ciscoLwappOpendnsMIBConform, claOpendnsWlanDhcpOpt6=claOpendnsWlanDhcpOpt6, ciscoLwappOpendnsTag=ciscoLwappOpendnsTag, ciscoLwappOpendnsMIBComplianceRev2=ciscoLwappOpendnsMIBComplianceRev2, claOpendnsProfileEntry=claOpendnsProfileEntry, ciscoLwappOpendnsMIB=ciscoLwappOpendnsMIB, claOpendnsWlanTable=claOpendnsWlanTable, claOpendnsProfileRowStatus=claOpendnsProfileRowStatus, ciscoLwappOpendnsMIBCompliances=ciscoLwappOpendnsMIBCompliances, claOpendnsEnable=claOpendnsEnable, claOpendnsProfileIdentity=claOpendnsProfileIdentity, ciscoLwappOpendnsTagGroupVer2=ciscoLwappOpendnsTagGroupVer2, ciscoLwappOpendnsConfigGroup=ciscoLwappOpendnsConfigGroup, ciscoLwappOpendnsTagGroup=ciscoLwappOpendnsTagGroup, ciscoLwappOpendnsMIBComplianceRev1=ciscoLwappOpendnsMIBComplianceRev1, ciscoLwappOpendnsMIBObjects=ciscoLwappOpendnsMIBObjects, claOpendnsApiToken=claOpendnsApiToken, claOpendnsWlanMode=claOpendnsWlanMode, claOpendnsProfileStatus=claOpendnsProfileStatus, claOpendnsWlanProfileName=claOpendnsWlanProfileName, claOpendnsForceEnable=claOpendnsForceEnable, claOpendnsWlanProfileStatus=claOpendnsWlanProfileStatus, PYSNMP_MODULE_ID=ciscoLwappOpendnsMIB)
