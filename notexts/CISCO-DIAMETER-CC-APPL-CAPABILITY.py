#
# PySNMP MIB module CISCO-DIAMETER-CC-APPL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DIAMETER-CC-APPL-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
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
ciscoDiameterCCACapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 516))
ciscoDiameterCCACapability.setRevisions(('2006-09-06 00:00',))
if mibBuilder.loadTexts: ciscoDiameterCCACapability.setLastUpdated('200609060000Z')
if mibBuilder.loadTexts: ciscoDiameterCCACapability.setOrganization('Cisco Systems, Inc.')
ciscoDiameterCCACapabilityV12R0409XG = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 516, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDiameterCCACapabilityV12R0409XG = ciscoDiameterCCACapabilityV12R0409XG.setProductRelease('Cisco IOS 12.4(9)XG.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDiameterCCACapabilityV12R0409XG = ciscoDiameterCCACapabilityV12R0409XG.setStatus('current')
mibBuilder.exportSymbols("CISCO-DIAMETER-CC-APPL-CAPABILITY", PYSNMP_MODULE_ID=ciscoDiameterCCACapability, ciscoDiameterCCACapabilityV12R0409XG=ciscoDiameterCCACapabilityV12R0409XG, ciscoDiameterCCACapability=ciscoDiameterCCACapability)
