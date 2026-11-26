#
# PySNMP MIB module CISCO-GGSN-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-GGSN-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:46 2026
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
cggsnCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 296))
cggsnCapability.setRevisions(('2006-10-09 01:00', '2003-04-08 03:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cggsnCapability.setRevisionsDescriptions(('Added cggsnCapabilityV12R4M9XG.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: cggsnCapability.setLastUpdated('200610090100Z')
if mibBuilder.loadTexts: cggsnCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cggsnCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                        Postal: 170 West Tasman Drive\n                                San Jose, CA  95134\n                                USA\n                                Tel: +1 800 553-NETS\n\n                        E-mail: cs-gprs@cisco.com')
if mibBuilder.loadTexts: cggsnCapability.setDescription('Agent capabilities for CISCO-GGSN-MIB')
cggsnCapabilityV12R2M8YD = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 296, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cggsnCapabilityV12R2M8YD = cggsnCapabilityV12R2M8YD.setProductRelease('Cisco IOS 12.2(4)MX & 12.2(8)YD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cggsnCapabilityV12R2M8YD = cggsnCapabilityV12R2M8YD.setStatus('current')
if mibBuilder.loadTexts: cggsnCapabilityV12R2M8YD.setDescription('Cisco GGSN MIB capabilities.')
cggsnCapabilityV12R2M8YY1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 296, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cggsnCapabilityV12R2M8YY1 = cggsnCapabilityV12R2M8YY1.setProductRelease('Cisco IOS 12.2(8)YY1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cggsnCapabilityV12R2M8YY1 = cggsnCapabilityV12R2M8YY1.setStatus('current')
if mibBuilder.loadTexts: cggsnCapabilityV12R2M8YY1.setDescription('Cisco GGSN MIB capabilities.')
cggsnCapabilityV12R2M8YW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 296, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cggsnCapabilityV12R2M8YW = cggsnCapabilityV12R2M8YW.setProductRelease('Cisco IOS 12.2(8)YW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cggsnCapabilityV12R2M8YW = cggsnCapabilityV12R2M8YW.setStatus('current')
if mibBuilder.loadTexts: cggsnCapabilityV12R2M8YW.setDescription('Cisco GGSN MIB capabilities.')
cggsnCapabilityV12R4M9XG = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 296, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cggsnCapabilityV12R4M9XG = cggsnCapabilityV12R4M9XG.setProductRelease('Cisco IOS 12.4(9)XG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cggsnCapabilityV12R4M9XG = cggsnCapabilityV12R4M9XG.setStatus('current')
if mibBuilder.loadTexts: cggsnCapabilityV12R4M9XG.setDescription('Cisco GGSN MIB capabilities.')
mibBuilder.exportSymbols("CISCO-GGSN-CAPABILITY", cggsnCapability=cggsnCapability, cggsnCapabilityV12R2M8YW=cggsnCapabilityV12R2M8YW, PYSNMP_MODULE_ID=cggsnCapability, cggsnCapabilityV12R2M8YD=cggsnCapabilityV12R2M8YD, cggsnCapabilityV12R2M8YY1=cggsnCapabilityV12R2M8YY1, cggsnCapabilityV12R4M9XG=cggsnCapabilityV12R4M9XG)
