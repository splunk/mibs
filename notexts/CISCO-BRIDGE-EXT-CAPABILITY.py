#
# PySNMP MIB module CISCO-BRIDGE-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-BRIDGE-EXT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoBridgeExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 459))
ciscoBridgeExtCapability.setRevisions(('2013-07-26 00:00', '2010-11-18 00:00', '2009-07-24 00:00', '2007-07-03 00:00', '2005-10-20 00:00',))
if mibBuilder.loadTexts: ciscoBridgeExtCapability.setLastUpdated('201307260000Z')
if mibBuilder.loadTexts: ciscoBridgeExtCapability.setOrganization('Cisco Systems, Inc.')
cbeCapV12R0218SXEPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 459, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbeCapV12R0218SXEPCat6K = cbeCapV12R0218SXEPCat6K.setProductRelease('Cisco IOS 12.2(18)SXE on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbeCapV12R0218SXEPCat6K = cbeCapV12R0218SXEPCat6K.setStatus('current')
cbeCapV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 459, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbeCapV12R0233SXHPCat6K = cbeCapV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbeCapV12R0233SXHPCat6K = cbeCapV12R0233SXHPCat6K.setStatus('current')
cbeCapV12R0250SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 459, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbeCapV12R0250SYPCat6K = cbeCapV12R0250SYPCat6K.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbeCapV12R0250SYPCat6K = cbeCapV12R0250SYPCat6K.setStatus('current')
cbeCapNxOSV06R0202PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 459, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbeCapNxOSV06R0202PN7k = cbeCapNxOSV06R0202PN7k.setProductRelease('Cisco NX-OS 6.2(2) on Nexus 7000 \n                        series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbeCapNxOSV06R0202PN7k = cbeCapNxOSV06R0202PN7k.setStatus('current')
mibBuilder.exportSymbols("CISCO-BRIDGE-EXT-CAPABILITY", cbeCapV12R0250SYPCat6K=cbeCapV12R0250SYPCat6K, PYSNMP_MODULE_ID=ciscoBridgeExtCapability, cbeCapV12R0233SXHPCat6K=cbeCapV12R0233SXHPCat6K, cbeCapNxOSV06R0202PN7k=cbeCapNxOSV06R0202PN7k, cbeCapV12R0218SXEPCat6K=cbeCapV12R0218SXEPCat6K, ciscoBridgeExtCapability=ciscoBridgeExtCapability)
