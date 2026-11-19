#
# PySNMP MIB module CISCO-DOT11-WIDS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DOT11-WIDS-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:06 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cDot11WidsCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 426))
if mibBuilder.loadTexts: cDot11WidsCapability.setLastUpdated('200501240000Z')
if mibBuilder.loadTexts: cDot11WidsCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cDot11WidsCapability.setContactInfo('             Cisco Systems\n                              Customer Service\n\n                              Postal: 170 W Tasman Drive\n                              San Jose, CA  95134\n                              USA\n  \n                              Tel: +1 800 553-NETS\n \n                              E-mail: cs-dot11@cisco.com')
if mibBuilder.loadTexts: cDot11WidsCapability.setDescription('Agent capabilities for \n                 CISCO-DOT11-WIDS-MIB')
cDot11WidsCapabilityV12R0304JA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 426, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11WidsCapabilityV12R0304JA = cDot11WidsCapabilityV12R0304JA.setProductRelease('Cisco IOS 12.3(4) JA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11WidsCapabilityV12R0304JA = cDot11WidsCapabilityV12R0304JA.setStatus('current')
if mibBuilder.loadTexts: cDot11WidsCapabilityV12R0304JA.setDescription('Cisco DOT11 WIDS MIB capabilities')
mibBuilder.exportSymbols("CISCO-DOT11-WIDS-CAPABILITY", cDot11WidsCapability=cDot11WidsCapability, cDot11WidsCapabilityV12R0304JA=cDot11WidsCapabilityV12R0304JA, PYSNMP_MODULE_ID=cDot11WidsCapability)
