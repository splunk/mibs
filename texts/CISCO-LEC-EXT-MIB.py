#
# PySNMP MIB module CISCO-LEC-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-LEC-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:46 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
VlanIndex, = mibBuilder.importSymbols("CISCO-VTP-MIB", "VlanIndex")
lecConfigEntry, = mibBuilder.importSymbols("LAN-EMULATION-CLIENT-MIB", "lecConfigEntry")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, TimeTicks, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoLecExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 77))
ciscoLecExtMIB.setRevisions(('1997-05-09 12:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLecExtMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoLecExtMIB.setLastUpdated('9705091230Z')
if mibBuilder.loadTexts: ciscoLecExtMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoLecExtMIB.setContactInfo('       Cisco Systems\n                           Customer Service\n\n                   Postal: 170 W Tasman Drive\n                           San Jose, CA  95134\n                           USA\n\n                      Tel: +1 800 553-NETS\n\n                   E-mail: cs-atm@cisco.com')
if mibBuilder.loadTexts: ciscoLecExtMIB.setDescription("This MIB module is a Cisco extension to the ATM\n                Forum's LANE Client MIB.")
ciscoLecExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 77, 1))
cLecExtVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 77, 1, 1))
cLecToVlanTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 77, 1, 1, 1), )
if mibBuilder.loadTexts: cLecToVlanTable.setStatus('current')
if mibBuilder.loadTexts: cLecToVlanTable.setDescription('An extension to the lecConfig table in the\n                LAN-EMULATION-CLIENT-MIB that identifies which VLAN a\n                LEC is associated with.')
cLecToVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 77, 1, 1, 1, 1), )
lecConfigEntry.registerAugmentions(("CISCO-LEC-EXT-MIB", "cLecToVlanEntry"))
cLecToVlanEntry.setIndexNames(*lecConfigEntry.getIndexNames())
if mibBuilder.loadTexts: cLecToVlanEntry.setStatus('current')
if mibBuilder.loadTexts: cLecToVlanEntry.setDescription(' Each entry in this table shows the correlation\n                between a LAN Emulation client and the VLAN that it\n                extends.')
cLecToVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 77, 1, 1, 1, 1, 1), VlanIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLecToVlanId.setStatus('current')
if mibBuilder.loadTexts: cLecToVlanId.setDescription(' The VLAN ID of the VLAN to which the specified LEC\n                is attributed.')
ciscoLecExtMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 77, 2))
ciscoLecExtMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 77, 2, 0))
ciscoLecExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 77, 3))
ciscoLecExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 77, 3, 1))
ciscoLecExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 77, 3, 2))
ciscoLecExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 77, 3, 1, 1)).setObjects(("CISCO-LEC-EXT-MIB", "ciscoLecExtVlanMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLecExtMIBCompliance = ciscoLecExtMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoLecExtMIBCompliance.setDescription('This module should be implemented by all Cisco\n                 devices supporting ATM LAN Emulation Clients.')
ciscoLecExtVlanMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 77, 3, 2, 1)).setObjects(("CISCO-LEC-EXT-MIB", "cLecToVlanId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLecExtVlanMIBGroup = ciscoLecExtVlanMIBGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoLecExtVlanMIBGroup.setDescription('A collection of objects related to identifying\n                a LANE Client associated VLAN information.')
mibBuilder.exportSymbols("CISCO-LEC-EXT-MIB", ciscoLecExtMIB=ciscoLecExtMIB, cLecToVlanTable=cLecToVlanTable, cLecToVlanEntry=cLecToVlanEntry, ciscoLecExtMIBConformance=ciscoLecExtMIBConformance, cLecToVlanId=cLecToVlanId, ciscoLecExtMIBGroups=ciscoLecExtMIBGroups, ciscoLecExtVlanMIBGroup=ciscoLecExtVlanMIBGroup, ciscoLecExtMIBCompliance=ciscoLecExtMIBCompliance, ciscoLecExtMIBNotifications=ciscoLecExtMIBNotifications, ciscoLecExtMIBCompliances=ciscoLecExtMIBCompliances, cLecExtVlan=cLecExtVlan, PYSNMP_MODULE_ID=ciscoLecExtMIB, ciscoLecExtMIBObjects=ciscoLecExtMIBObjects, ciscoLecExtMIBNotificationPrefix=ciscoLecExtMIBNotificationPrefix)
