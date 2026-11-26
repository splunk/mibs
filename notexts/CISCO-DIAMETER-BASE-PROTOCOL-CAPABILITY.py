#
# PySNMP MIB module CISCO-DIAMETER-BASE-PROTOCOL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DIAMETER-BASE-PROTOCOL-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
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
ciscoDiameterBasePCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 517))
ciscoDiameterBasePCapability.setRevisions(('2006-09-06 11:30',))
if mibBuilder.loadTexts: ciscoDiameterBasePCapability.setLastUpdated('200609061130Z')
if mibBuilder.loadTexts: ciscoDiameterBasePCapability.setOrganization('Cisco Systems, Inc.')
ciscoDiameterBasePCapabilityV12R0409XG = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 517, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDiameterBasePCapabilityV12R0409XG = ciscoDiameterBasePCapabilityV12R0409XG.setProductRelease('Cisco IOS 12.4(9)XG.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDiameterBasePCapabilityV12R0409XG = ciscoDiameterBasePCapabilityV12R0409XG.setStatus('current')
mibBuilder.exportSymbols("CISCO-DIAMETER-BASE-PROTOCOL-CAPABILITY", ciscoDiameterBasePCapability=ciscoDiameterBasePCapability, ciscoDiameterBasePCapabilityV12R0409XG=ciscoDiameterBasePCapabilityV12R0409XG, PYSNMP_MODULE_ID=ciscoDiameterBasePCapability)
