#
# PySNMP MIB module CISCO-PING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-PING-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPingCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 36))
ciscoPingCapability.setRevisions(('2006-03-15 00:00', '2004-06-14 00:00', '2004-01-19 00:00', '1994-08-18 00:00',))
if mibBuilder.loadTexts: ciscoPingCapability.setLastUpdated('200603150000Z')
if mibBuilder.loadTexts: ciscoPingCapability.setOrganization('Cisco Systems, Inc.')
ciscoPingCapabilityV10R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 36, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPingCapabilityV10R02 = ciscoPingCapabilityV10R02.setProductRelease('Cisco IOS 10.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPingCapabilityV10R02 = ciscoPingCapabilityV10R02.setStatus('current')
ciscoPingCapabilityCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 36, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPingCapabilityCatOSV08R0301 = ciscoPingCapabilityCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPingCapabilityCatOSV08R0301 = ciscoPingCapabilityCatOSV08R0301.setStatus('current')
mibBuilder.exportSymbols("CISCO-PING-CAPABILITY", ciscoPingCapabilityV10R02=ciscoPingCapabilityV10R02, ciscoPingCapability=ciscoPingCapability, PYSNMP_MODULE_ID=ciscoPingCapability, ciscoPingCapabilityCatOSV08R0301=ciscoPingCapabilityCatOSV08R0301)
