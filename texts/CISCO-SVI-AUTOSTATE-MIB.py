#
# PySNMP MIB module CISCO-SVI-AUTOSTATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SVI-AUTOSTATE-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:44 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, TimeTicks, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
ciscoSVIAutostateMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 376))
ciscoSVIAutostateMIB.setRevisions(('2004-04-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSVIAutostateMIB.setRevisionsDescriptions(('Initial revision of this MIB module.',))
if mibBuilder.loadTexts: ciscoSVIAutostateMIB.setLastUpdated('200404060000Z')
if mibBuilder.loadTexts: ciscoSVIAutostateMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSVIAutostateMIB.setContactInfo('        Cisco Systems\n                 Customer Service\n\n         Postal: 170 W Tasman Drive\n                 San Jose, CA 95134\n                 USA\n\n            Tel: +1 800 553-NETS\n\n         E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSVIAutostateMIB.setDescription('The MIB module is for configuration of the switch virtual\n         interface (SVI) autostate feature. Autostate feature\n         is a mechanism to calculate the state of a SVI dynamically\n         when some condition occurs such as a failure of \n         a participating interface in that SVI.')
ciscoSVIAutostateMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 376, 0))
ciscoSVIAutostateMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 376, 1))
ciscoSVIAutostateMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 376, 2))
csaGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 1))
csaInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 2))
csaFeatureEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csaFeatureEnable.setStatus('current')
if mibBuilder.loadTexts: csaFeatureEnable.setDescription("This object indicates whether the autostate feature is\n         enabled. If it is set to 'false', the feature is disabled\n         in the device and the value of csaInterfaceMode does not\n         take effect.")
csaTrackedVlansLow = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csaTrackedVlansLow.setStatus('current')
if mibBuilder.loadTexts: csaTrackedVlansLow.setDescription("A string of octets containing one bit per VLAN for \n         VLANs with VlanIndex value of 0 to 2047. The first\n         octet corresponds to VLANs with VlanIndex values\n         of 0 through 7; the second octet to VLANs 8 through\n         15; etc.  The most significant bit of each octet\n         corresponds to the lowest value VlanIndex in that octet.\n\n         For each VLAN, if it is tracked by the SVI autostate\n         feature then the bit corresponding to that VLAN is set\n         to '1'. A tracked VLAN, whose all interfaces having their\n         cdsInterfaceMode object value of 'track' and not in \n         forwarding state, will go down.")
csaTrackedVlansHigh = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csaTrackedVlansHigh.setStatus('current')
if mibBuilder.loadTexts: csaTrackedVlansHigh.setDescription("A string of octets containing one bit per VLAN for \n         VLANs with VlanIndex value of 2048 to 4095. The first\n         octet corresponds to VLANs with VlanIndex values\n         of 2048 through 2055; the second octet to VLANs 2056\n         through 2063; etc.  The most significant bit of each\n         octet corresponds to the lowest value VlanIndex in that\n         octet.\n\n         For each VLAN, if it is tracked by the SVI autostate\n         feature then the bit corresponding to that VLAN is set\n         to '1'. A tracked VLAN, whose all interfaces having their\n         cdsInterfaceMode object value of 'track' and not in   \n         forwarding state, will go down.")
csaIfConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 2, 1), )
if mibBuilder.loadTexts: csaIfConfigTable.setStatus('current')
if mibBuilder.loadTexts: csaIfConfigTable.setDescription('This table contains information and configuration\n         of interface mode regarding the SVI autostate\n         feature.')
csaIfConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: csaIfConfigEntry.setStatus('current')
if mibBuilder.loadTexts: csaIfConfigEntry.setDescription('There will be an entry for each interface that supports \n          SVI autostate feature. A row instance contains the\n          configured mode at each interface for Autostate purpose.')
csaInterfaceMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("exclude", 2), ("track", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csaInterfaceMode.setStatus('current')
if mibBuilder.loadTexts: csaInterfaceMode.setDescription("This object indicates the interface mode regarding\n         SVI autostate feature. This object only takes effect if\n         the value of csaFeatureEnable object is 'true'.\n\n         'normal' indicates that when SVI autostate feature is\n         enabled, this interface will participate normally\n         in the autostate calculation of the SVI which it\n         associates.\n\n         'exclude' indicates that when SVI autostate feature is\n         enabled, this interface will be excluded from the autostate\n         calculation of the SVI which it associates.\n\n         'track' indicates that when SVI autostate feature is\n         enabled, this interface will be tracked in the autostate\n         calculation of the tracked SVI which it associates. If all\n         tracked interfaces of this SVI go down, the corresponding\n         SVI goes down.")
csaMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 376, 2, 1))
csaMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 376, 2, 2))
csaMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 376, 2, 1, 1)).setObjects(("CISCO-SVI-AUTOSTATE-MIB", "ciscoSVIAutostateGroup"), ("CISCO-SVI-AUTOSTATE-MIB", "ciscoSVITrackedVlanGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csaMIBCompliance = csaMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: csaMIBCompliance.setDescription('The compliance statement for the CISCO-SVI-AUTOSTATE-MIB')
ciscoSVIAutostateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 376, 2, 2, 1)).setObjects(("CISCO-SVI-AUTOSTATE-MIB", "csaFeatureEnable"), ("CISCO-SVI-AUTOSTATE-MIB", "csaInterfaceMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSVIAutostateGroup = ciscoSVIAutostateGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoSVIAutostateGroup.setDescription('A collection of objects which are used to configure as\n         well as show information regarding the SVI autostate \n         feature.')
ciscoSVITrackedVlanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 376, 2, 2, 2)).setObjects(("CISCO-SVI-AUTOSTATE-MIB", "csaTrackedVlansLow"), ("CISCO-SVI-AUTOSTATE-MIB", "csaTrackedVlansHigh"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSVITrackedVlanGroup = ciscoSVITrackedVlanGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoSVITrackedVlanGroup.setDescription('A collection of objects which are used to configure as\n         well as show information regarding VLANs tracked by the\n         SVI autostate feature.')
mibBuilder.exportSymbols("CISCO-SVI-AUTOSTATE-MIB", csaFeatureEnable=csaFeatureEnable, ciscoSVIAutostateGroup=ciscoSVIAutostateGroup, csaGlobal=csaGlobal, csaMIBCompliance=csaMIBCompliance, ciscoSVIAutostateMIB=ciscoSVIAutostateMIB, ciscoSVIAutostateMIBNotifs=ciscoSVIAutostateMIBNotifs, csaTrackedVlansLow=csaTrackedVlansLow, csaIfConfigEntry=csaIfConfigEntry, ciscoSVIAutostateMIBConformance=ciscoSVIAutostateMIBConformance, ciscoSVIAutostateMIBObjects=ciscoSVIAutostateMIBObjects, csaIfConfigTable=csaIfConfigTable, csaTrackedVlansHigh=csaTrackedVlansHigh, csaInterfaceMode=csaInterfaceMode, csaMIBGroups=csaMIBGroups, csaMIBCompliances=csaMIBCompliances, PYSNMP_MODULE_ID=ciscoSVIAutostateMIB, ciscoSVITrackedVlanGroup=ciscoSVITrackedVlanGroup, csaInterface=csaInterface)
