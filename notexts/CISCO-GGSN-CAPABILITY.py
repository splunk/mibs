#
# PySNMP MIB module CISCO-GGSN-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-GGSN-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cggsnCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 296))
cggsnCapability.setRevisions(('2006-10-09 01:00', '2003-04-08 03:30',))
if mibBuilder.loadTexts: cggsnCapability.setLastUpdated('200610090100Z')
if mibBuilder.loadTexts: cggsnCapability.setOrganization('Cisco Systems, Inc.')
cggsnCapabilityV12R2M8YD = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 296, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cggsnCapabilityV12R2M8YD = cggsnCapabilityV12R2M8YD.setProductRelease('Cisco IOS 12.2(4)MX & 12.2(8)YD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cggsnCapabilityV12R2M8YD = cggsnCapabilityV12R2M8YD.setStatus('current')
cggsnCapabilityV12R2M8YY1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 296, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cggsnCapabilityV12R2M8YY1 = cggsnCapabilityV12R2M8YY1.setProductRelease('Cisco IOS 12.2(8)YY1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cggsnCapabilityV12R2M8YY1 = cggsnCapabilityV12R2M8YY1.setStatus('current')
cggsnCapabilityV12R2M8YW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 296, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cggsnCapabilityV12R2M8YW = cggsnCapabilityV12R2M8YW.setProductRelease('Cisco IOS 12.2(8)YW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cggsnCapabilityV12R2M8YW = cggsnCapabilityV12R2M8YW.setStatus('current')
cggsnCapabilityV12R4M9XG = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 296, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cggsnCapabilityV12R4M9XG = cggsnCapabilityV12R4M9XG.setProductRelease('Cisco IOS 12.4(9)XG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cggsnCapabilityV12R4M9XG = cggsnCapabilityV12R4M9XG.setStatus('current')
mibBuilder.exportSymbols("CISCO-GGSN-CAPABILITY", cggsnCapabilityV12R2M8YD=cggsnCapabilityV12R2M8YD, cggsnCapabilityV12R2M8YY1=cggsnCapabilityV12R2M8YY1, PYSNMP_MODULE_ID=cggsnCapability, cggsnCapability=cggsnCapability, cggsnCapabilityV12R4M9XG=cggsnCapabilityV12R4M9XG, cggsnCapabilityV12R2M8YW=cggsnCapabilityV12R2M8YW)
