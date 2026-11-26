#
# PySNMP MIB module CISCO-FC-MULTICAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-FC-MULTICAST-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
DomainIdOrZero, = mibBuilder.importSymbols("CISCO-ST-TC", "DomainIdOrZero")
vsanIndex, = mibBuilder.importSymbols("CISCO-VSAN-MIB", "vsanIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoFcMulticastMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 435))
ciscoFcMulticastMIB.setRevisions(('2004-10-07 00:00',))
if mibBuilder.loadTexts: ciscoFcMulticastMIB.setLastUpdated('200410070000Z')
if mibBuilder.loadTexts: ciscoFcMulticastMIB.setOrganization('Cisco Systems Inc. ')
ciscoFcMulticastNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 435, 0))
ciscoFcMulticastMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 435, 1))
ciscoFcMulticaseConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 435, 2))
cfmConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 435, 1, 1))
class CfmMulticastRootMode(TextualConvention, Integer32):
    reference = 'Refer to FC-SW-2 REV 5.4 for information on principal switch and lowest domain id switch.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("principalSwitch", 1), ("lowestDomainSwitch", 2))

cfmMulticastRootTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 435, 1, 1, 1), )
if mibBuilder.loadTexts: cfmMulticastRootTable.setStatus('current')
cfmMulticastRootEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 435, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"))
if mibBuilder.loadTexts: cfmMulticastRootEntry.setStatus('current')
cfmMulticastRootConfigMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 435, 1, 1, 1, 1, 1), CfmMulticastRootMode().clone('principalSwitch')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmMulticastRootConfigMode.setStatus('current')
cfmMulticastRootOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 435, 1, 1, 1, 1, 2), CfmMulticastRootMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmMulticastRootOperMode.setStatus('current')
cfmMulticastRootDomainId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 435, 1, 1, 1, 1, 3), DomainIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmMulticastRootDomainId.setStatus('current')
cfmMulticastRootRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 435, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmMulticastRootRowStatus.setStatus('current')
ciscoFcMulticastMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 435, 2, 1))
ciscoFcMulticastMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 435, 2, 2))
ciscoFcMulticastMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 435, 2, 1, 1)).setObjects(("CISCO-FC-MULTICAST-MIB", "cfmConfigurationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFcMulticastMIBCompliance = ciscoFcMulticastMIBCompliance.setStatus('current')
cfmConfigurationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 435, 2, 2, 1)).setObjects(("CISCO-FC-MULTICAST-MIB", "cfmMulticastRootConfigMode"), ("CISCO-FC-MULTICAST-MIB", "cfmMulticastRootOperMode"), ("CISCO-FC-MULTICAST-MIB", "cfmMulticastRootDomainId"), ("CISCO-FC-MULTICAST-MIB", "cfmMulticastRootRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmConfigurationGroup = cfmConfigurationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-FC-MULTICAST-MIB", cfmConfigurationGroup=cfmConfigurationGroup, cfmMulticastRootOperMode=cfmMulticastRootOperMode, CfmMulticastRootMode=CfmMulticastRootMode, ciscoFcMulticastMIBGroups=ciscoFcMulticastMIBGroups, cfmMulticastRootTable=cfmMulticastRootTable, ciscoFcMulticastMIBCompliance=ciscoFcMulticastMIBCompliance, ciscoFcMulticastMIBObjects=ciscoFcMulticastMIBObjects, ciscoFcMulticaseConformance=ciscoFcMulticaseConformance, cfmConfiguration=cfmConfiguration, cfmMulticastRootEntry=cfmMulticastRootEntry, PYSNMP_MODULE_ID=ciscoFcMulticastMIB, ciscoFcMulticastMIBCompliances=ciscoFcMulticastMIBCompliances, cfmMulticastRootRowStatus=cfmMulticastRootRowStatus, cfmMulticastRootConfigMode=cfmMulticastRootConfigMode, ciscoFcMulticastMIB=ciscoFcMulticastMIB, ciscoFcMulticastNotifications=ciscoFcMulticastNotifications, cfmMulticastRootDomainId=cfmMulticastRootDomainId)
