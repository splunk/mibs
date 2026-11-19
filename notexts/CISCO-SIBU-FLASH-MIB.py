#
# PySNMP MIB module CISCO-SIBU-FLASH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SIBU-FLASH-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:44 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSibuFlashMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 45))
ciscoSibuFlashMIB.setRevisions(('1998-10-23 00:00',))
if mibBuilder.loadTexts: ciscoSibuFlashMIB.setLastUpdated('9810230000Z')
if mibBuilder.loadTexts: ciscoSibuFlashMIB.setOrganization('Cisco Systems Inc.')
ciscoSibuFlashMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 45, 1))
csfUpgrade = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1))
csfUpgradeFirmwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: csfUpgradeFirmwareVersion.setStatus('current')
csfUpgradeFlashSize = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('kbytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: csfUpgradeFlashSize.setStatus('current')
csfUpgradeTFTPServerAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 3), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csfUpgradeTFTPServerAddress.setStatus('current')
csfUpgradeTFTPLoadFilename = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csfUpgradeTFTPLoadFilename.setStatus('current')
csfUpgradeTFTPInitiate = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("upgrade", 1), ("noUpgrade", 2))).clone('noUpgrade')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csfUpgradeTFTPInitiate.setStatus('current')
csfUpgradeFlashMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("permanent", 1), ("temporary", 2))).clone('permanent')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csfUpgradeFlashMode.setStatus('current')
csfUpgradeFirmwareStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("inProgress", 2), ("succeeded", 3), ("failed", 4))).clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: csfUpgradeFirmwareStatus.setStatus('current')
ciscoSibuFlashMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 45, 2))
ciscoSibuFlashMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 45, 2, 0))
ciscoSibuFlashMIBComformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 45, 3))
ciscoSibuFlashMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 45, 3, 1))
ciscoSibuFlashMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 45, 3, 2))
ciscoSibuFlashCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 45, 3, 1, 1)).setObjects(("CISCO-SIBU-FLASH-MIB", "ciscoSibuFlashMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSibuFlashCompliance = ciscoSibuFlashCompliance.setStatus('current')
ciscoSibuFlashMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 45, 3, 2, 1)).setObjects(("CISCO-SIBU-FLASH-MIB", "csfUpgradeFirmwareVersion"), ("CISCO-SIBU-FLASH-MIB", "csfUpgradeFlashSize"), ("CISCO-SIBU-FLASH-MIB", "csfUpgradeTFTPServerAddress"), ("CISCO-SIBU-FLASH-MIB", "csfUpgradeTFTPLoadFilename"), ("CISCO-SIBU-FLASH-MIB", "csfUpgradeTFTPInitiate"), ("CISCO-SIBU-FLASH-MIB", "csfUpgradeFlashMode"), ("CISCO-SIBU-FLASH-MIB", "csfUpgradeFirmwareStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSibuFlashMIBGroup = ciscoSibuFlashMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SIBU-FLASH-MIB", ciscoSibuFlashMIB=ciscoSibuFlashMIB, ciscoSibuFlashMIBObjects=ciscoSibuFlashMIBObjects, PYSNMP_MODULE_ID=ciscoSibuFlashMIB, ciscoSibuFlashMIBGroup=ciscoSibuFlashMIBGroup, ciscoSibuFlashMIBComformance=ciscoSibuFlashMIBComformance, csfUpgrade=csfUpgrade, ciscoSibuFlashMIBCompliances=ciscoSibuFlashMIBCompliances, ciscoSibuFlashMIBNotificationsPrefix=ciscoSibuFlashMIBNotificationsPrefix, ciscoSibuFlashCompliance=ciscoSibuFlashCompliance, csfUpgradeTFTPInitiate=csfUpgradeTFTPInitiate, ciscoSibuFlashMIBNotifications=ciscoSibuFlashMIBNotifications, csfUpgradeFirmwareVersion=csfUpgradeFirmwareVersion, csfUpgradeFlashSize=csfUpgradeFlashSize, ciscoSibuFlashMIBGroups=ciscoSibuFlashMIBGroups, csfUpgradeTFTPLoadFilename=csfUpgradeTFTPLoadFilename, csfUpgradeTFTPServerAddress=csfUpgradeTFTPServerAddress, csfUpgradeFlashMode=csfUpgradeFlashMode, csfUpgradeFirmwareStatus=csfUpgradeFirmwareStatus)
