#
# PySNMP MIB module CISCO-UBE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-UBE-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:46 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, TimeTicks, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
ciscoUbeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 764))
ciscoUbeMIB.setRevisions(('2010-11-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoUbeMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoUbeMIB.setLastUpdated('201011290000Z')
if mibBuilder.loadTexts: ciscoUbeMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoUbeMIB.setContactInfo('Cisco Systems\n            Customer Service\n\n\n            Postal: 170 W Tasman Drive\n\n            San Jose, CA  95134\n\n            USA\n\n\n            Tel: +1 800 553-NETS\n\n\n            E-mail: cs-cube@cisco.com')
if mibBuilder.loadTexts: ciscoUbeMIB.setDescription('This MIB describes objects used for managing Cisco\n        Unified Border Element (CUBE).\n\n        The Cisco Unified Border Element (CUBE) is a Cisco \n        IOS Session Border Controller (SBC) that interconnects\n        independent voice over IP (VoIP) and video over IP \n        networks for data, voice, and video transport')
ciscoUbeMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 764, 0))
ciscoUbeMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 764, 1))
cubeEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 764, 0, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cubeEnabled.setStatus('current')
if mibBuilder.loadTexts: cubeEnabled.setDescription("This object represents, whether the Cisco\n        Unified Border Element (CUBE) is enabled \n        on the device or not.\n\n        The value 'true' means that the CUBE feature \n        is enabled on the device.\n\n        The value 'false' means that the CUBE feature \n        is disabled.")
cubeVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 764, 0, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cubeVersion.setStatus('current')
if mibBuilder.loadTexts: cubeVersion.setDescription('This object represents the version of Cisco\n        Unified Border Element on the device.')
cubeTotalSessionAllowed = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 764, 0, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 999999))).setUnits('session').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cubeTotalSessionAllowed.setStatus('current')
if mibBuilder.loadTexts: cubeTotalSessionAllowed.setDescription('This object provides the total number of CUBE\n        session allowed on the device. The value zero \n        means no sessions are allowed with CUBE.')
ciscoUbeMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 764, 1, 1))
ciscoUbeMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 764, 1, 2))
ciscoCubeMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 764, 1, 1, 1)).setObjects(("CISCO-UBE-MIB", "ciscoUbeMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCubeMIBCompliance = ciscoCubeMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoCubeMIBCompliance.setDescription('The compliance statement for Cisco\n        Unified Border Element (CUBE) MIB.')
ciscoUbeMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 764, 1, 2, 1)).setObjects(("CISCO-UBE-MIB", "cubeEnabled"), ("CISCO-UBE-MIB", "cubeVersion"), ("CISCO-UBE-MIB", "cubeTotalSessionAllowed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUbeMIBGroup = ciscoUbeMIBGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoUbeMIBGroup.setDescription('A collection of objects which provides the\n        capabilities of the CUBE feature.')
mibBuilder.exportSymbols("CISCO-UBE-MIB", ciscoUbeMIBGroup=ciscoUbeMIBGroup, PYSNMP_MODULE_ID=ciscoUbeMIB, ciscoUbeMIBObjects=ciscoUbeMIBObjects, ciscoUbeMIBCompliances=ciscoUbeMIBCompliances, cubeVersion=cubeVersion, ciscoUbeMIBConform=ciscoUbeMIBConform, ciscoUbeMIB=ciscoUbeMIB, ciscoCubeMIBCompliance=ciscoCubeMIBCompliance, cubeEnabled=cubeEnabled, ciscoUbeMIBGroups=ciscoUbeMIBGroups, cubeTotalSessionAllowed=cubeTotalSessionAllowed)
