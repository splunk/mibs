#
# PySNMP MIB module CISCO-BRIDGE-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-BRIDGE-EXT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:44 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoBridgeExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 459))
ciscoBridgeExtCapability.setRevisions(('2013-07-26 00:00', '2010-11-18 00:00', '2009-07-24 00:00', '2007-07-03 00:00', '2005-10-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoBridgeExtCapability.setRevisionsDescriptions(('Added capability statement cbeCapNxOSV06R0202PN7k.', 'Added capability statement cbeCapV12R0250SYPCat6K.', 'Added VARIATION for cbeDot1dTpGlobalAgingTime\n        and cbeDot1dTpVlanAgingTime in \n        cbeCapV12R0233SXHPCat6K statement.', 'Added cbeCapV12R0233SXHPCat6K for Cisco IOS\n        12.2(33)SXH.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoBridgeExtCapability.setLastUpdated('201307260000Z')
if mibBuilder.loadTexts: ciscoBridgeExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoBridgeExtCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoBridgeExtCapability.setDescription('Agent capabilities for CISCO-BRIDGE-EXT-MIB.')
cbeCapV12R0218SXEPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 459, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbeCapV12R0218SXEPCat6K = cbeCapV12R0218SXEPCat6K.setProductRelease('Cisco IOS 12.2(18)SXE on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbeCapV12R0218SXEPCat6K = cbeCapV12R0218SXEPCat6K.setStatus('current')
if mibBuilder.loadTexts: cbeCapV12R0218SXEPCat6K.setDescription('CISCO-BRIDGE-EXT-MIB agent capabilities.')
cbeCapV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 459, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbeCapV12R0233SXHPCat6K = cbeCapV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbeCapV12R0233SXHPCat6K = cbeCapV12R0233SXHPCat6K.setStatus('current')
if mibBuilder.loadTexts: cbeCapV12R0233SXHPCat6K.setDescription('CISCO-BRIDGE-EXT-MIB agent capabilities.')
cbeCapV12R0250SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 459, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbeCapV12R0250SYPCat6K = cbeCapV12R0250SYPCat6K.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbeCapV12R0250SYPCat6K = cbeCapV12R0250SYPCat6K.setStatus('current')
if mibBuilder.loadTexts: cbeCapV12R0250SYPCat6K.setDescription('CISCO-BRIDGE-EXT-MIB agent capabilities.')
cbeCapNxOSV06R0202PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 459, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbeCapNxOSV06R0202PN7k = cbeCapNxOSV06R0202PN7k.setProductRelease('Cisco NX-OS 6.2(2) on Nexus 7000 \n                        series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbeCapNxOSV06R0202PN7k = cbeCapNxOSV06R0202PN7k.setStatus('current')
if mibBuilder.loadTexts: cbeCapNxOSV06R0202PN7k.setDescription('CISCO-BRIDGE-EXT-MIB agent capabilities.')
mibBuilder.exportSymbols("CISCO-BRIDGE-EXT-CAPABILITY", cbeCapV12R0218SXEPCat6K=cbeCapV12R0218SXEPCat6K, cbeCapV12R0233SXHPCat6K=cbeCapV12R0233SXHPCat6K, cbeCapV12R0250SYPCat6K=cbeCapV12R0250SYPCat6K, ciscoBridgeExtCapability=ciscoBridgeExtCapability, PYSNMP_MODULE_ID=ciscoBridgeExtCapability, cbeCapNxOSV06R0202PN7k=cbeCapNxOSV06R0202PN7k)
