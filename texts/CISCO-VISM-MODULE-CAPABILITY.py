#
# PySNMP MIB module CISCO-VISM-MODULE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VISM-MODULE-CAPABILITY
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
ciscoVismModuleCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 458))
ciscoVismModuleCapability.setRevisions(('2005-10-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVismModuleCapability.setRevisionsDescriptions(('Initial version of this capability file.',))
if mibBuilder.loadTexts: ciscoVismModuleCapability.setLastUpdated('200510180000Z')
if mibBuilder.loadTexts: ciscoVismModuleCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVismModuleCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoVismModuleCapability.setDescription('The capabilities description of \n                 CISCO-VISM-MODULE-MIB.')
cVismModuleCapabilityV3325 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 458, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVismModuleCapabilityV3325 = cVismModuleCapabilityV3325.setProductRelease('Cisco VISM Release 3.3.25')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVismModuleCapabilityV3325 = cVismModuleCapabilityV3325.setStatus('current')
if mibBuilder.loadTexts: cVismModuleCapabilityV3325.setDescription('CISCO-VISM-MODULE-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-VISM-MODULE-CAPABILITY", cVismModuleCapabilityV3325=cVismModuleCapabilityV3325, PYSNMP_MODULE_ID=ciscoVismModuleCapability, ciscoVismModuleCapability=ciscoVismModuleCapability)
