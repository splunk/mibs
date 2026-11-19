#
# PySNMP MIB module CISCO-CABLE-SPECTRUM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-CABLE-SPECTRUM-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:07 2026
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
ciscoCableSpectrumCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 999))
ciscoCableSpectrumCapability.setRevisions(('2002-12-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCableSpectrumCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoCableSpectrumCapability.setLastUpdated('200212180000Z')
if mibBuilder.loadTexts: ciscoCableSpectrumCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCableSpectrumCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W. Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                Tel: +1 800 553-NETS\n\n                E-mail: cs-ubr@cisco.com')
if mibBuilder.loadTexts: ciscoCableSpectrumCapability.setDescription('Agent capabilities for CISCO-CABLE-SPECTRUM-MIB')
ciscoCableSpectrumCapabilityV12R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableSpectrumCapabilityV12R00 = ciscoCableSpectrumCapabilityV12R00.setProductRelease('Cisco IOS 12.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableSpectrumCapabilityV12R00 = ciscoCableSpectrumCapabilityV12R00.setStatus('current')
if mibBuilder.loadTexts: ciscoCableSpectrumCapabilityV12R00.setDescription('Cisco Cable Spectrum Management MIB capabilities.')
ciscoCableSpectrumCapabilityV12R01Rev1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableSpectrumCapabilityV12R01Rev1 = ciscoCableSpectrumCapabilityV12R01Rev1.setProductRelease('Cisco IOS 12.1(05)EC and 12.2 BC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableSpectrumCapabilityV12R01Rev1 = ciscoCableSpectrumCapabilityV12R01Rev1.setStatus('current')
if mibBuilder.loadTexts: ciscoCableSpectrumCapabilityV12R01Rev1.setDescription('Cisco Cable Spectrum Management MIB capabilities.')
mibBuilder.exportSymbols("CISCO-CABLE-SPECTRUM-CAPABILITY", ciscoCableSpectrumCapabilityV12R00=ciscoCableSpectrumCapabilityV12R00, PYSNMP_MODULE_ID=ciscoCableSpectrumCapability, ciscoCableSpectrumCapability=ciscoCableSpectrumCapability, ciscoCableSpectrumCapabilityV12R01Rev1=ciscoCableSpectrumCapabilityV12R01Rev1)
