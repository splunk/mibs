#
# PySNMP MIB module CISCO-ENTITY-PROVISIONING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ENTITY-PROVISIONING-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention, AutonomousType = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "AutonomousType")
ciscoEntityProvMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 139))
if mibBuilder.loadTexts: ciscoEntityProvMIB.setLastUpdated('9907082052Z')
if mibBuilder.loadTexts: ciscoEntityProvMIB.setOrganization('Cisco Systems, Inc.')
ciscoEntityProvMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 139, 1))
ceProvContainerTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 139, 1, 1), )
if mibBuilder.loadTexts: ceProvContainerTable.setStatus('current')
ceProvContainerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 139, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: ceProvContainerEntry.setStatus('current')
ceProvContainerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 139, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unequipped", 1), ("provisioned", 2), ("mismatched", 3), ("invalid", 4), ("equipped", 5), ("failed", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceProvContainerStatus.setStatus('current')
ceProvContainerEquipped = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 139, 1, 1, 1, 2), AutonomousType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceProvContainerEquipped.setStatus('current')
ceProvContainerDetected = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 139, 1, 1, 1, 3), AutonomousType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceProvContainerDetected.setStatus('current')
ceProvMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 139, 2))
ceProvMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 139, 2, 0))
ceProvMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 139, 3))
ceProvMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 139, 3, 1))
ceProvMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 139, 3, 2))
ceProvMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 139, 3, 1, 1)).setObjects(("CISCO-ENTITY-PROVISIONING-MIB", "ceProvContainerGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceProvMIBCompliance = ceProvMIBCompliance.setStatus('current')
ceProvContainerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 139, 3, 2, 1)).setObjects(("CISCO-ENTITY-PROVISIONING-MIB", "ceProvContainerStatus"), ("CISCO-ENTITY-PROVISIONING-MIB", "ceProvContainerEquipped"), ("CISCO-ENTITY-PROVISIONING-MIB", "ceProvContainerDetected"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceProvContainerGroup = ceProvContainerGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ENTITY-PROVISIONING-MIB", PYSNMP_MODULE_ID=ciscoEntityProvMIB, ciscoEntityProvMIB=ciscoEntityProvMIB, ceProvContainerEquipped=ceProvContainerEquipped, ceProvMIBCompliances=ceProvMIBCompliances, ceProvMIBGroups=ceProvMIBGroups, ceProvMIBCompliance=ceProvMIBCompliance, ceProvContainerTable=ceProvContainerTable, ceProvMIBNotificationsPrefix=ceProvMIBNotificationsPrefix, ceProvMIBNotifications=ceProvMIBNotifications, ciscoEntityProvMIBObjects=ciscoEntityProvMIBObjects, ceProvContainerEntry=ceProvContainerEntry, ceProvMIBConformance=ceProvMIBConformance, ceProvContainerDetected=ceProvContainerDetected, ceProvContainerStatus=ceProvContainerStatus, ceProvContainerGroup=ceProvContainerGroup)
