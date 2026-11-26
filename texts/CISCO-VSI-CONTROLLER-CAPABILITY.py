#
# PySNMP MIB module CISCO-VSI-CONTROLLER-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VSI-CONTROLLER-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:45 2026
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
ciscoVsiControllerCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 9999))
ciscoVsiControllerCapability.setRevisions(('2002-05-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVsiControllerCapability.setRevisionsDescriptions(('Initial version of the MIB module.',))
if mibBuilder.loadTexts: ciscoVsiControllerCapability.setLastUpdated('200205020000Z')
if mibBuilder.loadTexts: ciscoVsiControllerCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVsiControllerCapability.setContactInfo('       Cisco Systems\n\n                Customer Service\n\n           Postal: 170 West Tasman Drive\n           San Jose, CA  95134\n           USA\n\n           Tel: +1 800 553-NETS\n\n          E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoVsiControllerCapability.setDescription('Agent capabilities for CISCO-VSI-CONTROLLER-MIB.')
ciscoVsiControllerCapabilityVR200 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVsiControllerCapabilityVR200 = ciscoVsiControllerCapabilityVR200.setProductRelease('MGX8850 Release 2.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVsiControllerCapabilityVR200 = ciscoVsiControllerCapabilityVR200.setStatus('current')
if mibBuilder.loadTexts: ciscoVsiControllerCapabilityVR200.setDescription('The agent capabilities for \n                CISCO-VSI-CONTROLLER-MIB.')
mibBuilder.exportSymbols("CISCO-VSI-CONTROLLER-CAPABILITY", PYSNMP_MODULE_ID=ciscoVsiControllerCapability, ciscoVsiControllerCapability=ciscoVsiControllerCapability, ciscoVsiControllerCapabilityVR200=ciscoVsiControllerCapabilityVR200)
