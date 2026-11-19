#
# PySNMP MIB module CISCO-IPV6-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IPV6-CAPABILITY
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
cipv6Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 503))
cipv6Capability.setRevisions(('2006-05-17 00:00',))
if mibBuilder.loadTexts: cipv6Capability.setLastUpdated('200605170000Z')
if mibBuilder.loadTexts: cipv6Capability.setOrganization('Cisco Systems, Inc.')
ciscoIpv6CapCRS1V3R3R1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 503, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpv6CapCRS1V3R3R1 = ciscoIpv6CapCRS1V3R3R1.setProductRelease('Cisco IOS XR 3.3.1 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpv6CapCRS1V3R3R1 = ciscoIpv6CapCRS1V3R3R1.setStatus('current')
mibBuilder.exportSymbols("CISCO-IPV6-CAPABILITY", PYSNMP_MODULE_ID=cipv6Capability, ciscoIpv6CapCRS1V3R3R1=ciscoIpv6CapCRS1V3R3R1, cipv6Capability=cipv6Capability)
