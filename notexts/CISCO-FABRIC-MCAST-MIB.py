#
# PySNMP MIB module CISCO-FABRIC-MCAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-FABRIC-MCAST-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entLogicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entLogicalIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoFabricMcastMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 255))
ciscoFabricMcastMIB.setRevisions(('2002-08-20 00:00',))
if mibBuilder.loadTexts: ciscoFabricMcastMIB.setLastUpdated('200208200000Z')
if mibBuilder.loadTexts: ciscoFabricMcastMIB.setOrganization('Cisco Systems, Inc.')
ciscoFabricMcastMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 255, 0))
ciscoFabricMcastMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 255, 1))
ciscoFabricMcastMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 255, 2))
cfmGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 1))
cfmPool = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 2))
cfmLr = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 3))
class CfmPoolIndex(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

cfmGenInfoTotalFgids = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 1, 1), Gauge32()).setUnits('fgid').setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmGenInfoTotalFgids.setStatus('current')
cfmGenInfoInuseFgids = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 1, 2), Gauge32()).setUnits('fgid').setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmGenInfoInuseFgids.setStatus('current')
cfmGenInfoHighWaterInuseFgids = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 1, 3), Gauge32()).setUnits('fgid').setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmGenInfoHighWaterInuseFgids.setStatus('current')
cfmPoolTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 2, 1), )
if mibBuilder.loadTexts: cfmPoolTable.setStatus('current')
cfmPoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-FABRIC-MCAST-MIB", "cfmPoolId"))
if mibBuilder.loadTexts: cfmPoolEntry.setStatus('current')
cfmPoolId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 2, 1, 1, 1), CfmPoolIndex())
if mibBuilder.loadTexts: cfmPoolId.setStatus('current')
cfmPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 2, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmPoolName.setStatus('current')
cfmPoolType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("shared", 1), ("dedicated", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmPoolType.setStatus('current')
cfmPoolTotalFgids = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 2, 1, 1, 4), Gauge32()).setUnits('fgid').setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmPoolTotalFgids.setStatus('current')
cfmPoolInuseFgids = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 2, 1, 1, 5), Gauge32()).setUnits('fgid').setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmPoolInuseFgids.setStatus('current')
cfmPoolHighWaterInuseFgids = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 2, 1, 1, 6), Gauge32()).setUnits('fgid').setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmPoolHighWaterInuseFgids.setStatus('current')
cfmLrTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 3, 1), )
if mibBuilder.loadTexts: cfmLrTable.setStatus('current')
cfmLrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 3, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entLogicalIndex"))
if mibBuilder.loadTexts: cfmLrEntry.setStatus('current')
cfmLrInuseFgids = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 3, 1, 1, 1), Gauge32()).setUnits('fgid').setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmLrInuseFgids.setStatus('current')
cfmLrHighWaterInuseFgids = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 3, 1, 1, 2), Gauge32()).setUnits('fgid').setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmLrHighWaterInuseFgids.setStatus('current')
cfmMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 255, 2, 1))
cfmMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 255, 2, 2))
cfmMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 255, 2, 1, 1)).setObjects(("CISCO-FABRIC-MCAST-MIB", "cfmGenInfoGroup"), ("CISCO-FABRIC-MCAST-MIB", "cfmPoolGroup"), ("CISCO-FABRIC-MCAST-MIB", "cfmLrGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmMIBCompliance = cfmMIBCompliance.setStatus('current')
cfmGenInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 255, 2, 2, 1)).setObjects(("CISCO-FABRIC-MCAST-MIB", "cfmGenInfoTotalFgids"), ("CISCO-FABRIC-MCAST-MIB", "cfmGenInfoInuseFgids"), ("CISCO-FABRIC-MCAST-MIB", "cfmGenInfoHighWaterInuseFgids"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmGenInfoGroup = cfmGenInfoGroup.setStatus('current')
cfmPoolGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 255, 2, 2, 2)).setObjects(("CISCO-FABRIC-MCAST-MIB", "cfmPoolName"), ("CISCO-FABRIC-MCAST-MIB", "cfmPoolType"), ("CISCO-FABRIC-MCAST-MIB", "cfmPoolTotalFgids"), ("CISCO-FABRIC-MCAST-MIB", "cfmPoolInuseFgids"), ("CISCO-FABRIC-MCAST-MIB", "cfmPoolHighWaterInuseFgids"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmPoolGroup = cfmPoolGroup.setStatus('current')
cfmLrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 255, 2, 2, 3)).setObjects(("CISCO-FABRIC-MCAST-MIB", "cfmLrInuseFgids"), ("CISCO-FABRIC-MCAST-MIB", "cfmLrHighWaterInuseFgids"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmLrGroup = cfmLrGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-FABRIC-MCAST-MIB", cfmPoolName=cfmPoolName, PYSNMP_MODULE_ID=ciscoFabricMcastMIB, cfmGenInfoInuseFgids=cfmGenInfoInuseFgids, ciscoFabricMcastMIBConform=ciscoFabricMcastMIBConform, CfmPoolIndex=CfmPoolIndex, cfmGenInfoHighWaterInuseFgids=cfmGenInfoHighWaterInuseFgids, cfmPoolTotalFgids=cfmPoolTotalFgids, cfmLrHighWaterInuseFgids=cfmLrHighWaterInuseFgids, cfmPoolTable=cfmPoolTable, cfmPoolId=cfmPoolId, cfmGeneral=cfmGeneral, cfmGenInfoTotalFgids=cfmGenInfoTotalFgids, cfmGenInfoGroup=cfmGenInfoGroup, cfmPoolType=cfmPoolType, cfmPool=cfmPool, cfmMIBGroups=cfmMIBGroups, cfmPoolInuseFgids=cfmPoolInuseFgids, ciscoFabricMcastMIBObjects=ciscoFabricMcastMIBObjects, cfmLrInuseFgids=cfmLrInuseFgids, cfmLrTable=cfmLrTable, cfmPoolEntry=cfmPoolEntry, ciscoFabricMcastMIB=ciscoFabricMcastMIB, cfmLr=cfmLr, cfmMIBCompliances=cfmMIBCompliances, cfmPoolGroup=cfmPoolGroup, cfmLrEntry=cfmLrEntry, ciscoFabricMcastMIBNotifs=ciscoFabricMcastMIBNotifs, cfmMIBCompliance=cfmMIBCompliance, cfmPoolHighWaterInuseFgids=cfmPoolHighWaterInuseFgids, cfmLrGroup=cfmLrGroup)
