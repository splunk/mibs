#
# PySNMP MIB module CISCO-VISM-DSX1-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VISM-DSX1-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:46 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoVismDsx1Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 450))
ciscoVismDsx1Capability.setRevisions(('2005-09-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVismDsx1Capability.setRevisionsDescriptions(('Initial version of this capability file.',))
if mibBuilder.loadTexts: ciscoVismDsx1Capability.setLastUpdated('200509260000Z')
if mibBuilder.loadTexts: ciscoVismDsx1Capability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVismDsx1Capability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoVismDsx1Capability.setDescription('Agent capabilities for \n                 CISCO-VISM-DSX1-MIB.')
cVismDsx1CapabilityV3325 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 450, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVismDsx1CapabilityV3325 = cVismDsx1CapabilityV3325.setProductRelease('Cisco VISM Release 3.3.25')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVismDsx1CapabilityV3325 = cVismDsx1CapabilityV3325.setStatus('current')
if mibBuilder.loadTexts: cVismDsx1CapabilityV3325.setDescription('CISCO-VISM-DSX1-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-VISM-DSX1-CAPABILITY", PYSNMP_MODULE_ID=ciscoVismDsx1Capability, cVismDsx1CapabilityV3325=cVismDsx1CapabilityV3325, ciscoVismDsx1Capability=ciscoVismDsx1Capability)
