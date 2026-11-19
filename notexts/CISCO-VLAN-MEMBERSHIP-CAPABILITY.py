#
# PySNMP MIB module CISCO-VLAN-MEMBERSHIP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VLAN-MEMBERSHIP-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:24 2026
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
ciscoVlanMembershipCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 316))
ciscoVlanMembershipCapability.setRevisions(('2010-10-29 00:00', '2010-03-21 00:00', '2007-07-12 00:00', '2004-01-15 00:00', '2003-09-15 00:00',))
if mibBuilder.loadTexts: ciscoVlanMembershipCapability.setLastUpdated('201010290000Z')
if mibBuilder.loadTexts: ciscoVlanMembershipCapability.setOrganization('Cisco Systems, Inc.')
cVlanMembershipCapV12R0119ECat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 316, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanMembershipCapV12R0119ECat6K = cVlanMembershipCapV12R0119ECat6K.setProductRelease('Cisco IOS 12.1(19E) on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanMembershipCapV12R0119ECat6K = cVlanMembershipCapV12R0119ECat6K.setStatus('current')
cVlanMembershipCapV12R0217SXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 316, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanMembershipCapV12R0217SXCat6K = cVlanMembershipCapV12R0217SXCat6K.setProductRelease('Cisco IOS 12.2(17SX) on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanMembershipCapV12R0217SXCat6K = cVlanMembershipCapV12R0217SXCat6K.setStatus('current')
ciscoVlanMembershipCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 316, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanMembershipCapCatOSV08R0101 = ciscoVlanMembershipCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanMembershipCapCatOSV08R0101 = ciscoVlanMembershipCapCatOSV08R0101.setStatus('current')
ciscoVlanMembershipCapCatOSV08R0201 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 316, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanMembershipCapCatOSV08R0201 = ciscoVlanMembershipCapCatOSV08R0201.setProductRelease('Cisco CatOS 8.2(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanMembershipCapCatOSV08R0201 = ciscoVlanMembershipCapCatOSV08R0201.setStatus('current')
cVlanMembershipCapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 316, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanMembershipCapCatOSV08R0301 = cVlanMembershipCapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanMembershipCapCatOSV08R0301 = cVlanMembershipCapCatOSV08R0301.setStatus('current')
cVlanMemberCapV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 316, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanMemberCapV12R0233SXHPCat6K = cVlanMemberCapV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanMemberCapV12R0233SXHPCat6K = cVlanMemberCapV12R0233SXHPCat6K.setStatus('current')
cVlanMemberCapV12R0233SXI4PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 316, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanMemberCapV12R0233SXI4PCat6K = cVlanMemberCapV12R0233SXI4PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst \n                    6000/6500 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanMemberCapV12R0233SXI4PCat6K = cVlanMemberCapV12R0233SXI4PCat6K.setStatus('current')
cVlanMemberCapV12R0250SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 316, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanMemberCapV12R0250SYPCat6K = cVlanMemberCapV12R0250SYPCat6K.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst \n                    6000/6500 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanMemberCapV12R0250SYPCat6K = cVlanMemberCapV12R0250SYPCat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-VLAN-MEMBERSHIP-CAPABILITY", PYSNMP_MODULE_ID=ciscoVlanMembershipCapability, cVlanMembershipCapV12R0217SXCat6K=cVlanMembershipCapV12R0217SXCat6K, cVlanMemberCapV12R0233SXHPCat6K=cVlanMemberCapV12R0233SXHPCat6K, ciscoVlanMembershipCapCatOSV08R0101=ciscoVlanMembershipCapCatOSV08R0101, cVlanMembershipCapV12R0119ECat6K=cVlanMembershipCapV12R0119ECat6K, cVlanMembershipCapCatOSV08R0301=cVlanMembershipCapCatOSV08R0301, cVlanMemberCapV12R0250SYPCat6K=cVlanMemberCapV12R0250SYPCat6K, ciscoVlanMembershipCapability=ciscoVlanMembershipCapability, cVlanMemberCapV12R0233SXI4PCat6K=cVlanMemberCapV12R0233SXI4PCat6K, ciscoVlanMembershipCapCatOSV08R0201=ciscoVlanMembershipCapCatOSV08R0201)
