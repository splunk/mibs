#
# PySNMP MIB module CISCO-Q-BRIDGE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-Q-BRIDGE-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:46 2026
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
ciscoQBridgeCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 389))
ciscoQBridgeCapability.setRevisions(('2011-09-27 00:00', '2011-07-27 00:00', '2008-10-28 00:00', '2004-01-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoQBridgeCapability.setRevisionsDescriptions(('Added capability statement ciscoQBridgeCapV15R0001SYPCat6K.', 'Added capability statement ciscoQBridgeCapNxOSV05R0201PN7K.', 'Added ciscoQBridgeCapV12R0233SXIPCat6K.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoQBridgeCapability.setLastUpdated('201109270000Z')
if mibBuilder.loadTexts: ciscoQBridgeCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoQBridgeCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoQBridgeCapability.setDescription('The capabilities description of\n        Q-BRIDGE-MIB.')
ciscoQBridgeCapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 389, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQBridgeCapCatOSV08R0301 = ciscoQBridgeCapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQBridgeCapCatOSV08R0301 = ciscoQBridgeCapCatOSV08R0301.setStatus('current')
if mibBuilder.loadTexts: ciscoQBridgeCapCatOSV08R0301.setDescription('Q-BRIDGE-MIB capabilities.')
ciscoQBridgeCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 389, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQBridgeCapV12R0233SXIPCat6K = ciscoQBridgeCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQBridgeCapV12R0233SXIPCat6K = ciscoQBridgeCapV12R0233SXIPCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoQBridgeCapV12R0233SXIPCat6K.setDescription('Q-BRIDGE-MIB capabilities.')
ciscoQBridgeCapNxOSV05R0201PN7K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 389, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQBridgeCapNxOSV05R0201PN7K = ciscoQBridgeCapNxOSV05R0201PN7K.setProductRelease('Cisco NX-OS 5.2(1) on Nexus 7000\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQBridgeCapNxOSV05R0201PN7K = ciscoQBridgeCapNxOSV05R0201PN7K.setStatus('current')
if mibBuilder.loadTexts: ciscoQBridgeCapNxOSV05R0201PN7K.setDescription('Q-BRIDGE-MIB capabilities.')
ciscoQBridgeCapV15R0001SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 389, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQBridgeCapV15R0001SYPCat6K = ciscoQBridgeCapV15R0001SYPCat6K.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQBridgeCapV15R0001SYPCat6K = ciscoQBridgeCapV15R0001SYPCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoQBridgeCapV15R0001SYPCat6K.setDescription('Q-BRIDGE-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-Q-BRIDGE-CAPABILITY", ciscoQBridgeCapability=ciscoQBridgeCapability, ciscoQBridgeCapV12R0233SXIPCat6K=ciscoQBridgeCapV12R0233SXIPCat6K, ciscoQBridgeCapV15R0001SYPCat6K=ciscoQBridgeCapV15R0001SYPCat6K, ciscoQBridgeCapCatOSV08R0301=ciscoQBridgeCapCatOSV08R0301, ciscoQBridgeCapNxOSV05R0201PN7K=ciscoQBridgeCapNxOSV05R0201PN7K, PYSNMP_MODULE_ID=ciscoQBridgeCapability)
