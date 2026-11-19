#
# PySNMP MIB module CISCO-POLICY-GROUP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-POLICY-GROUP-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:44 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "iso", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPolicyGroupCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 512))
ciscoPolicyGroupCapability.setRevisions(('2006-06-26 00:00',))
if mibBuilder.loadTexts: ciscoPolicyGroupCapability.setLastUpdated('200606260000Z')
if mibBuilder.loadTexts: ciscoPolicyGroupCapability.setOrganization('Cisco Systems, Inc.')
ciscoPolicyGroupCapV08R0601 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 512, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPolicyGroupCapV08R0601 = ciscoPolicyGroupCapV08R0601.setProductRelease('Cisco CatOS 8.6(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPolicyGroupCapV08R0601 = ciscoPolicyGroupCapV08R0601.setStatus('current')
mibBuilder.exportSymbols("CISCO-POLICY-GROUP-CAPABILITY", ciscoPolicyGroupCapV08R0601=ciscoPolicyGroupCapV08R0601, PYSNMP_MODULE_ID=ciscoPolicyGroupCapability, ciscoPolicyGroupCapability=ciscoPolicyGroupCapability)
