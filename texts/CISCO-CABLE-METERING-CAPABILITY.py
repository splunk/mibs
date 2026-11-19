#
# PySNMP MIB module CISCO-CABLE-METERING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-CABLE-METERING-CAPABILITY
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
ciscoCableMeteringCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 582))
ciscoCableMeteringCapability.setRevisions(('2009-06-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCableMeteringCapability.setRevisionsDescriptions(('Initial version of this MIB Module.',))
if mibBuilder.loadTexts: ciscoCableMeteringCapability.setLastUpdated('200906160000Z')
if mibBuilder.loadTexts: ciscoCableMeteringCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCableMeteringCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-ubr@cisco.com')
if mibBuilder.loadTexts: ciscoCableMeteringCapability.setDescription('Agent capabilities for CISCO-CABLE-METERING-MIB')
ciscoCableMeteringCapabilityV122R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 582, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableMeteringCapabilityV122R01 = ciscoCableMeteringCapabilityV122R01.setProductRelease('Cisco IOS 12.2S')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableMeteringCapabilityV122R01 = ciscoCableMeteringCapabilityV122R01.setStatus('current')
if mibBuilder.loadTexts: ciscoCableMeteringCapabilityV122R01.setDescription('Cisco Cable Metering MIB capabilities.')
mibBuilder.exportSymbols("CISCO-CABLE-METERING-CAPABILITY", ciscoCableMeteringCapabilityV122R01=ciscoCableMeteringCapabilityV122R01, ciscoCableMeteringCapability=ciscoCableMeteringCapability, PYSNMP_MODULE_ID=ciscoCableMeteringCapability)
