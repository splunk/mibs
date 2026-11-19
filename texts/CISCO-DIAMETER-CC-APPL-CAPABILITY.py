#
# PySNMP MIB module CISCO-DIAMETER-CC-APPL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DIAMETER-CC-APPL-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:14 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDiameterCCACapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 516))
ciscoDiameterCCACapability.setRevisions(('2006-09-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDiameterCCACapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoDiameterCCACapability.setLastUpdated('200609060000Z')
if mibBuilder.loadTexts: ciscoDiameterCCACapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDiameterCCACapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-aaa@cisco.com')
if mibBuilder.loadTexts: ciscoDiameterCCACapability.setDescription('The capabilities description of\n            CISCO-DIAMETER-CC-AAPL-MIB.')
ciscoDiameterCCACapabilityV12R0409XG = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 516, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDiameterCCACapabilityV12R0409XG = ciscoDiameterCCACapabilityV12R0409XG.setProductRelease('Cisco IOS 12.4(9)XG.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDiameterCCACapabilityV12R0409XG = ciscoDiameterCCACapabilityV12R0409XG.setStatus('current')
if mibBuilder.loadTexts: ciscoDiameterCCACapabilityV12R0409XG.setDescription('Cisco Diameter Credit Control Application MIB capabilities')
mibBuilder.exportSymbols("CISCO-DIAMETER-CC-APPL-CAPABILITY", ciscoDiameterCCACapabilityV12R0409XG=ciscoDiameterCCACapabilityV12R0409XG, PYSNMP_MODULE_ID=ciscoDiameterCCACapability, ciscoDiameterCCACapability=ciscoDiameterCCACapability)
