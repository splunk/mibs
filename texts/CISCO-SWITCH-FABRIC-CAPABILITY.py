#
# PySNMP MIB module CISCO-SWITCH-FABRIC-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SWITCH-FABRIC-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:45 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSwitchFabricCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 618))
ciscoSwitchFabricCapability.setRevisions(('2014-09-16 00:00', '2013-07-17 00:00', '2013-07-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSwitchFabricCapability.setRevisionsDescriptions(('Added capability statement\n        ciscoSwitchFabricCapNxOSV06R0210PN7k.', 'Added capability statement\n        ciscoSwitchFabricCapV15R0102SYPCat6K.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSwitchFabricCapability.setLastUpdated('201409160000Z')
if mibBuilder.loadTexts: ciscoSwitchFabricCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSwitchFabricCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSwitchFabricCapability.setDescription('The capabilities description of\n        CISCO-SWITCH-FABRIC-MIB.')
ciscoSwitchFabricCapNxOSV06R0104PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 618, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchFabricCapNxOSV06R0104PN7k = ciscoSwitchFabricCapNxOSV06R0104PN7k.setProductRelease('Cisco NX-OS 6.1(4) on Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchFabricCapNxOSV06R0104PN7k = ciscoSwitchFabricCapNxOSV06R0104PN7k.setStatus('current')
if mibBuilder.loadTexts: ciscoSwitchFabricCapNxOSV06R0104PN7k.setDescription('CISCO-SWITCH-FABRIC-MIB capabilities.')
ciscoSwitchFabricCapNxOSV06R0201PMds = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 618, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchFabricCapNxOSV06R0201PMds = ciscoSwitchFabricCapNxOSV06R0201PMds.setProductRelease('Cisco NX-OS 6.2(1) on MDS series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchFabricCapNxOSV06R0201PMds = ciscoSwitchFabricCapNxOSV06R0201PMds.setStatus('current')
if mibBuilder.loadTexts: ciscoSwitchFabricCapNxOSV06R0201PMds.setDescription('CISCO-SWITCH-FABRIC-MIB capabilities.')
ciscoSwitchFabricCapV15R0102SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 618, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchFabricCapV15R0102SYPCat6K = ciscoSwitchFabricCapV15R0102SYPCat6K.setProductRelease('Cisco IOS 15.1(2)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchFabricCapV15R0102SYPCat6K = ciscoSwitchFabricCapV15R0102SYPCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoSwitchFabricCapV15R0102SYPCat6K.setDescription('CISCO-SWITCH-FABRIC-MIB capabilities.')
ciscoSwitchFabricCapNxOSV06R0210PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 618, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchFabricCapNxOSV06R0210PN7k = ciscoSwitchFabricCapNxOSV06R0210PN7k.setProductRelease('Cisco NX-OS 6.2(10) on Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchFabricCapNxOSV06R0210PN7k = ciscoSwitchFabricCapNxOSV06R0210PN7k.setStatus('current')
if mibBuilder.loadTexts: ciscoSwitchFabricCapNxOSV06R0210PN7k.setDescription('CISCO-SWITCH-FABRIC-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SWITCH-FABRIC-CAPABILITY", ciscoSwitchFabricCapNxOSV06R0104PN7k=ciscoSwitchFabricCapNxOSV06R0104PN7k, ciscoSwitchFabricCapNxOSV06R0201PMds=ciscoSwitchFabricCapNxOSV06R0201PMds, ciscoSwitchFabricCapV15R0102SYPCat6K=ciscoSwitchFabricCapV15R0102SYPCat6K, PYSNMP_MODULE_ID=ciscoSwitchFabricCapability, ciscoSwitchFabricCapNxOSV06R0210PN7k=ciscoSwitchFabricCapNxOSV06R0210PN7k, ciscoSwitchFabricCapability=ciscoSwitchFabricCapability)
